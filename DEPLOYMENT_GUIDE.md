# ISO 20022 Validator - Global Deployment Guide

This guide explains how to move your application from your local machine to a "Global" environment (AWS, GCP, Azure, or your own server).

## 1. Prepare for Deployment
We have upgraded the application to be **Environment Aware**.
- **The Frontend** automatically detects if it's running on a remote server and adjusts its API calls.
- **The Backend** is now capable of serving the Frontend UI builders directly.

## 2. Option A: Using Docker (Recommended)
The easiest way to run this globally is using the included `docker-compose.yml`.

1. **Upload** the project to your server.
2. **Run**:
   ```bash
   docker-compose up -d --build
   ```
This will start a MySQL database, the Backend, and the Frontend in isolated containers.

## 3. Option B: Unified Deployment (Fastest)
You can run the entire application as a single Python process.

1. **Build the Frontend**:
   ```bash
   cd frontend
   npm install
   npm run build -- --output-path=../backend/app/static --base-href=/
   ```
2. **Run the Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --host 0.0.0.0 --port 80
   ```
Now, anyone can access the app by simply going to your server's Public IP on port 80.

## 4. Key Configurations for Global Access
- **Port Matching**: Ensure your cloud provider's **Security Group** allows inbound traffic on the port you choose (Default: 80 or 8000).
- **Environment Variables**: Create a `.env` file in the `backend` folder to configure your production database credentials.
- **HTTPS**: For production, we recommend using **Nginx** as a reverse proxy with Let's Encrypt for SSL certificates.

---
*Your application is now "Global-Ready"!*
