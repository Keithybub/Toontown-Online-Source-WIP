@echo off
set /P DISTRICT_NAME="District Name (DEFAULT: Goofyvalley) (spaces are not acceptable): " || ^
set DISTRICT_NAME=Goofyvalley

set /P PPYTHON=<python.txt

echo Starting Toontown Online AI server with name %DISTRICT_NAME%, this may take a while...

:goto
cls
%PPYTHON% -m toontown.ai.ServiceStart --base-channel 409000000 --max-channels 9999999 --stateserver 10000 --district-name %DISTRICT_NAME% --astron-ip "127.0.0.1:7199" --eventlogger-ip "127.0.0.1:7197"
pause
goto :goto