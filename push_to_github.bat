@echo off
cd /d "C:\Users\lzp\Desktop\jianshen"
echo This script pushes FitMate to GitHub and triggers APK build.
echo.
echo Step 1: Go to https://github.com/new
echo Step 2: Create repo named "fitmate" (public)
echo Step 3: DO NOT initialize with README
echo Step 4: Run the commands below:
echo.
echo git remote add origin https://github.com/%%USERNAME%%/fitmate.git
echo git push -u origin master
echo.
echo The APK will auto-build in GitHub Actions:
echo https://github.com/%%USERNAME%%/fitmate/actions
echo.
pause
