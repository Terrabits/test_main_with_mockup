@echo off
SET "ROOT_DIR=%~dp0.."
setlocal
cd "%ROOT_DIR%"


REM test
python -m unittest
