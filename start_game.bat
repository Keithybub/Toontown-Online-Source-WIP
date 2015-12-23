@echo off
echo Starting  Toontown Online...
set /P PYTHON=<PYTHON.txt
%PYTHON% -m toontown.toonbase.ToontownStart
pause
