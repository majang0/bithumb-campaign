@echo off
echo === 빗썸 캠페인 백업 시스템 ===
echo.
echo 1. 즉시 백업
echo 2. 백업 목록 보기
echo 3. 백업 복원
echo 4. Google Drive 폴더 열기 (수동 복사)
echo.
set /p choice=선택하세요 (1-4): 

if %choice%==1 (
    python backup_manager.py
    echo.
    echo 백업 완료! backups 폴더를 확인하세요.
) else if %choice%==2 (
    python -c "from backup_manager import BackupManager; BackupManager().list_backups()"
) else if %choice%==3 (
    echo 백업 파일명을 입력하세요:
    set /p backup_name=
    python -c "from backup_manager import BackupManager; BackupManager().restore_backup('%backup_name%')"
) else if %choice%==4 (
    explorer "https://drive.google.com"
    echo.
    echo Google Drive가 열렸습니다. 
    echo backups 폴더의 zip 파일을 수동으로 업로드하세요.
)

pause
