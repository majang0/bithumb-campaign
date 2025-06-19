@echo off
chcp 65001 > nul
echo GitHub Setup Helper
echo ===================
echo.

echo 1. Checking Git installation...
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [OK] Git is installed.
echo.

echo 2. Setting up Git user information...
set /p username="Enter your GitHub username: "
set /p email="Enter your GitHub email: "

git config --global user.name "%username%"
git config --global user.email "%email%"
echo [OK] User information configured.
echo.

echo 3. Initializing Git repository...
git init
echo [OK] Git repository initialized.
echo.

echo 4. Adding files...
git add .
echo [OK] All files added.
echo.

echo 5. Creating first commit...
git commit -m "Initial commit: Bithumb campaign automation system"
echo [OK] First commit created.
echo.

echo 6. Connecting to GitHub repository...
echo.
echo You need your GitHub repository URL.
echo Example: https://github.com/username/bithumb-campaign.git
echo.
set /p repo_url="Enter repository URL: "

git remote add origin %repo_url%
git branch -M main
echo [OK] GitHub repository connected.
echo.

echo 7. Pushing code to GitHub...
git push -u origin main
echo.
echo [OK] Setup complete!
echo.
pause
