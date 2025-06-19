@echo off
echo ============================
echo    Git 설치 확인 도구
echo ============================
echo.

git --version >nul 2>&1

if errorlevel 1 (
    echo [X] Git이 설치되어 있지 않습니다!
    echo.
    echo Git을 설치하려면:
    echo 1. https://git-scm.com/download/win 접속
    echo 2. "Download" 버튼 클릭
    echo 3. 다운로드된 파일 실행
    echo 4. 설치 과정에서 기본값으로 "Next" 클릭
    echo.
    echo 설치 후 이 파일을 다시 실행해주세요.
) else (
    echo [O] Git이 설치되어 있습니다!
    echo.
    git --version
    echo.
    echo 정상적으로 사용할 수 있습니다.
)

echo.
echo 아무 키나 누르면 종료됩니다...
pause >nul
