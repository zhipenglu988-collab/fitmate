@echo off
echo Enabling Windows Subsystem for Linux...
dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all
echo.
echo WSL feature enabled. Please REBOOT your computer.
echo After reboot, run: wsl --install -d Ubuntu
pause
