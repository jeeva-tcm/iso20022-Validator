---
description: How to run the Pre-SWIFT ISO 20022 Message Validation Platform
---

Follow these steps to get the application up and running:

1. **Prerequisites**
   - Node.js (v18+)
   - Python (3.11+)
   - MySQL (or use Docker)

2. **Backend Setup**
   - Go to `backend/` folder
   - Create a virtual environment: `python -m venv venv`
   - Activate it: `venv\Scripts\activate` (Windows)
   - Install dependencies: `pip install -r requirements.txt`
   - Run the server: `python run.py`

3. **Frontend Setup**
   - Go to `frontend/` folder
   - Install dependencies: `npm install`
   - Start Angular: `npm start`

4. **Access the App**
   - Portal: `http://localhost:4200`
   - API Docs: `http://localhost:8000/docs`

**Note:** If you have Docker installed, you can simply run `docker-compose up`.
