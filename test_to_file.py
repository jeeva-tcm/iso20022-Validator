
import asyncio
import sys
import os

sys.path.append(os.path.join(os.getcwd(), "backend"))

from app.services.validator import ISOValidator

async def test_validation():
    with open("validation_output.txt", "w") as out:
        out.write("Initializing Validator...\n")
        v = ISOValidator()
        out.write("Initialized.\n")
        
        # Test malformed
        out.write("\n--- Testing Malformed XML ---\n")
        malformed_xml = "<Document><MalformedTag>content</OtherTag></Document>"
        report = await v.validate(malformed_xml)
        for issue in report.issues:
            out.write(f"[{issue['severity']}] {issue['code']} | {issue['path']} | {issue['message']}\n")

        # Test valid-ish with rules
        out.write("\n--- Testing pacs.008 with Rules ---\n")
        sample_xml = """<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08">
            <FIToFICstmrCdtTrf>
                <GrpHdr><MsgId>TX123</MsgId><CreDtTm>2026-02-05T10:00:00</CreDtTm></GrpHdr>
                <CdtTrfTxInf>
                    <PmtId><EndToEndId>E2E-1</EndToEndId><InstrId>""" + "A"*40 + """</InstrId></PmtId>
                    <IntrBkSttlmAmt Ccy="USD">100.00</IntrBkSttlmAmt>
                    <Cdtr><Nm>X</Nm><PstlAdr><Ctry>US</Ctry></PstlAdr></Cdtr>
                </CdtTrfTxInf>
            </FIToFICstmrCdtTrf>
        </Document>"""
        report = await v.validate(sample_xml, message_type="pacs.008.001.08")
        for issue in report.issues:
            out.write(f"[{issue['severity']}] {issue['code']} | {issue['path']} | {issue['message']}\n")

if __name__ == "__main__":
    asyncio.run(test_validation())
