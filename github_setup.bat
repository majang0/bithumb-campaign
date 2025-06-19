@echo off
echo GitHub 연결 도우미
echo ===================
echo.

echo 1. Git 설치 확인 중...
git --version >nul 2>&1
if errorlevel 1 (
    echo [오류] Git이 설치되지 않았습니다!
    echo https://git-scm.com/download/win 에서 Git을 먼저 설치하세요.
    pause
    exit /b 1
)

echo [확인] Git이 설치되어 있습니다.
echo.

echo 2. Git 사용자 정보 설정...
set /p username="GitHub 사용자명을 입력하세요: "
set /p email="GitHub 이메일을 입력하세요: "

git config --global user.name "%username%"
git config --global user.email "%email%"
echo [완료] 사용자 정보가 설정되었습니다.
echo.

echo 3. Git 저장소 초기화...
git init
echo [완료] Git 저장소가 초기화되었습니다.
echo.

echo 4. 파일 추가...
git add .
echo [완료] 모든 파일이 추가되었습니다.
echo.

echo 5. 첫 번째 커밋...
git commit -m "Initial commit: 빗썸 캠페인 자동화 시스템"
echo [완료] 첫 번째 커밋이 생성되었습니다.
echo.

echo 6. GitHub 저장소 연결...
echo.
echo GitHub에서 만든 저장소 주소가 필요합니다.
echo 예시: https://github.com/사용자명/bithumb-campaign.git
echo.
set /p repo_url="저장소 주소를 입력하세요: "

git remote add origin %repo_url%
git branch -M main
echo [완료] GitHub 저장소가 연결되었습니다.
echo.

echo 7. 코드 업로드...
git push -u origin main
echo.
echo [완료] 모든 설정이 완료되었습니다!
echo.
pause
