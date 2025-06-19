@echo off
echo Google Drive 백업 시작...

REM Python 스크립트 실행
python C:\bithumb-campaign\backup_to_gdrive.py

REM 또는 robocopy 사용 (Python 없이)
REM robocopy "C:\bithumb-campaign\contents" "G:\내 드라이브\bithumb-campaign\contents" /E /MIR

echo 백업 완료!
pause
