@echo off
SET "ROOT_DIR=%~dp0.."
setlocal
cd "%ROOT_DIR%"


REM install
pip install --requirement requirements.txt
pip freeze > requirements-win64.txt.lock
