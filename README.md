# Pre-SWIFT ISO 20022 Message Validation Platform

A robust validation engine for ISO 20022 MX messages with a 5-layer quality gate approach.

## Key Features
- **5-Layer Validation Pipeline**:
  - Layer 1: Format & Safety
  - Layer 2: Schema (XSD) Compliance
  - Layer 3: Business Rules (Semantic)
  - Layer 4: SWIFT Network Readiness
  - Layer 5: Operational Context & Intelligence
- **Enterprise UI**: Built with Angular 17 and Material Design.
- **Fail-Fast Mechanism**: Stops validation as soon as a critical error is found.
- **Audit Traceability**: Every validation is logged with Fix Suggestions and Rule IDs.

## Tech Stack
- **Frontend**: Angular 17, Angular Material, RxJS
- **Backend**: Python 3.11, FastAPI, SQLAlchemy
- **Database**: MySQL (History & Audit Trail)
- **Validation**: lxml (XML/XSD processing)

## Getting Started
See `.agent/workflows/run-app.md` for detailed instructions.

### Quick Start with Docker
```bash
docker-compose up
```

## Dashboard Summary
- **Validate**: Upload or paste XML messages for instant reports.
- **History**: View previous validation results and download reports.
- **Reports**: Clear human-readable errors with fix suggestions.
