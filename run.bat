@echo off
echo 빗썸 캠페인 자동화 시스템
echo ========================
echo.
echo 1. 수동으로 콘텐츠 처리
echo 2. 스케줄러 시작 (자동 실행)
echo 3. 새 콘텐츠 생성
echo 4. 성과 리포트 확인
echo.
set /p choice=선택하세요 (1-4): 

if %choice%==1 (
    python -c "from automation import BithumbCampaignAutomation; BithumbCampaignAutomation().process_pending_contents()"
) else if %choice%==2 (
    python automation.py
) else if %choice%==3 (
    echo Claude에게 콘텐츠 생성을 요청하세요
) else if %choice%==4 (
    python report.py
)

pause
