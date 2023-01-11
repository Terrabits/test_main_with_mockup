@echo off
SET "ROOT_DIR=%~dp0.."
setlocal
cd "%ROOT_DIR%"


SET "DEST_DIR=%ROOT_DIR%\artifacts\packages\win64"

REM clean destination
rmdir /S /Q "%DEST_DIR%"
mkdir "%DEST_DIR%"

REM download python packages
pip download --requirement requirements.txt --dest "%DEST_DIR%"
