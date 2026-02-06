# How to Run the ISO 20022 Validator

It looks like **Python is not installed** or not added to your system PATH. You have two options to run the application:

## Option 1: Use Docker (Easiest Integration)
If you have Docker Desktop installed, you don't need to install Python or Node.js manually.

1. Open a terminal in the project folder.
2. Run:
   ```cmd
   docker-compose up --build
   ```
3. Open `http://localhost:4200`

## Option 2: Install Python (Manual Setup)
If you want to run it locally without Docker:

1. **Download Python**:
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Download the latest version for Windows.
   - **IMPORTANT**: During installation, check the box **"Add Python to PATH"**.

2. **Verify Installation**:
   - Open a new terminal and run: `python --version`

3. **Run the App**:
   - Double-click `start-dev.bat` again.

## Troubleshooting
If you have installed Python but it still says "Python was not found", you might need to fix your PATH environment variable or restart your computer.
