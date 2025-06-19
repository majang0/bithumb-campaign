"""
Google Drive 백업 자동화 스크립트
빗썸 캠페인 콘텐츠를 Google Drive에 자동 백업
"""

def backup_to_gdrive_instruction():
    """
    Claude에게 Google Drive 백업을 요청하는 방법
    """
    
    instructions = [
        # 1. 폴더 생성
        "Google Drive에 'bithumb-campaign-backup' 폴더가 있는지 확인해줘",
        
        # 2. 오늘 생성된 콘텐츠 백업
        "C:\\bithumb-campaign\\contents\\pending 폴더의 모든 JSON 파일을 "
        "Google Drive의 bithumb-campaign-backup/pending 폴더에 백업해줘",
        
        # 3. 리포트 백업
        "C:\\bithumb-campaign\\reports 폴더의 최신 리포트를 "
        "Google Drive의 bithumb-campaign-backup/reports 폴더에 백업해줘",
        
        # 4. 데이터베이스 백업
        "campaign.db 파일의 현재 상태를 요약해서 "
        "Google Drive에 'db_backup_summary_날짜.txt'로 저장해줘"
    ]
    
    return instructions

# Claude에게 요청할 명령어 예시
print("=== Google Drive 백업 명령어 ===")
for i, instruction in enumerate(backup_to_gdrive_instruction(), 1):
    print(f"{i}. {instruction}")
    
print("\n또는 한 번에:")
print("빗썸 캠페인의 모든 중요 파일을 Google Drive에 백업해줘")
