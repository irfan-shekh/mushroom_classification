@echo off
REM Quick launcher for Mushroom Classification Web Application
echo ===================================================
echo   Mushroom Classification Web Application
echo ===================================================
echo.
echo Starting development server...
echo Access the application at: http://127.0.0.1:8000
echo Press Ctrl+C in this terminal window to stop the server.
echo.
python manage.py runserver 127.0.0.1:8000
pause
