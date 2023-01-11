@echo off
SET "ROOT_DIR=%~dp0.."
setlocal
cd "%ROOT_DIR%"


SET "PACKAGE_DIR=%ROOT_DIR%\artifacts\packages\win64"


REM install from artifacts
pip install --no-index --find-links "%PACKAGE_DIR%" --requirement requirements-win64.txt.lock
