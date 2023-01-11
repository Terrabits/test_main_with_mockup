@echo off
SET "ROOT_DIR=%~dp0.."
setlocal
cd "%ROOT_DIR%"


REM start
python -m project.main
