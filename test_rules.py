
import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), "backend"))

from app.services.validator import ISOValidator

async def test_validation():
    v = ISOValidator()
    
    # 1. Test Malformed XML (REG-002)
    malformed_xml = "<Document><MalformedTag>content</OtherTag></Document>"
    print("\n--- Testing Malformed XML ---")
    report = await v.validate(malformed_xml, mode="Full 1-5", message_type="pacs.008.001.08")
    for issue in report.issues:
        if issue['code'] == 'REG-002':
            print(f"[{issue['severity']}] {issue['code']} | {issue['path']} | {issue['message']}")

    # 2. Test Address Mandate (E001) - Simulate post-2026 if necessary, 
    # but currently we can force the date in logic if we wanted.
    # For now let's just use a valid payload with missing town.
    valid_pacs008_missing_town = """
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08">
        <FIToFICstmrCdtTrf>
            <GrpHdr><MsgId>TX123</MsgId><CreDtTm>2026-02-05T10:00:00</CreDtTm></GrpHdr>
            <CdtTrfTxInf>
                <PmtId><EndToEndId>E2E-1</EndToEndId></PmtId>
                <IntrBkSttlmAmt Ccy="USD">100.00</IntrBkSttlmAmt>
                <Cdtr>
                    <Nm>John Doe</Nm>
                    <PstlAdr>
                        <Ctry>US</Ctry>
                    </PstlAdr>
                </Cdtr>
            </CdtTrfTxInf>
        </FIToFICstmrCdtTrf>
    </Document>
    """
    # Note: check_address logic uses datetime.now() > 2026-11-01.
    # Today is 2026-02-05, so it's BEFORE the strict mandate.
    # To test E001, let's temporarily mock the date or just check if it's there.
    
    print("\n--- Testing Address Rule (Pre-Nov 2026) ---")
    report = await v.validate(valid_pacs008_missing_town, mode="Full 1-5", message_type="pacs.008.001.08")
    # Should be valid/warning depending on logic.
    found = False
    for issue in report.issues:
        if issue['code'] == 'E001':
            print(f"[{issue['severity']}] {issue['code']} | {issue['path']} | {issue['message']}")
            found = True
    if not found: print("No E001 (as expected, Nov 2026 threshold not met)")

    # 3. Test Long Instruction ID (W005)
    long_instr_id_xml = valid_pacs008_missing_town.replace("<EndToEndId>E2E-1</EndToEndId>", 
                                                            "<EndToEndId>E2E-1</EndToEndId><InstrId>" + "A"*40 + "</InstrId>")
    print("\n--- Testing Instruction ID Length (W005) ---")
    report = await v.validate(long_instr_id_xml, mode="Full 1-5", message_type="pacs.008.001.08")
    for issue in report.issues:
        if issue['code'] == 'W005':
             print(f"[{issue['severity']}] {issue['code']} | {issue['path']} | {issue['message']}")

if __name__ == "__main__":
    asyncio.run(test_validation())
