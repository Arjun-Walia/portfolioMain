@echo off
REM Production deployment script for Windows systems

echo Starting Flask Portfolio production deployment...

REM Set production environment
set FLASK_ENV=production

REM Install production dependencies
echo Installing production dependencies...
pip install -r requirements-prod.txt

REM Start with Waitress (better for Windows)
echo Starting Waitress server...
python waitress_server.py