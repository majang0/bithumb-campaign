@echo off
echo 빗썸 캠페인 자동화 시스템 초기 설정
echo =====================================
echo.

echo 1. Python 패키지 설치 중...
pip install -r requirements.txt

echo.
echo 2. 로그 폴더 생성 중...
if not exist "logs" mkdir logs

echo.
echo 3. 데이터베이스 확인 중...
python -c "import sqlite3; conn = sqlite3.connect('data/campaign.db'); print('DB 연결 성공'); conn.close()"

echo.
echo 4. 설정 파일 확인...
if exist "config.json" (
    echo config.json 파일이 있습니다. API 키를 입력해주세요.
) else (
    echo config.json 파일이 없습니다!
)

echo.
echo =====================================
echo 초기 설정 완료!
echo.
echo 다음 단계:
echo 1. config.json 파일에 API 키 입력
echo 2. run.bat 실행하여 시스템 시작
echo.
pause
