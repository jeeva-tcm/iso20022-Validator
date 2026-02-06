@echo off
echo Starting ISO 20022 Validator Development Environment...

echo Installing Backend Dependencies...
cd backend
py -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo "pip install failed via 'py'. Trying 'python'..."
    python -m pip install -r requirements.txt
)

echo Starting Backend (Port 8000)...
start "Backend Server" cmd /k "py run.py || python run.py"

cd ..
echo Starting Frontend (Port 4200)...
start "Frontend Server" cmd /k "cd frontend && npm install && npm start"

echo.
echo Servers are starting...
echo Frontend will be at: http://localhost:4200
echo Backend will be at: http://localhost:8000
echo.
pause
