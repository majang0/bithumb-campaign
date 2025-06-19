import os
import shutil
from datetime import datetime

# Google Drive 경로 (보통 G: 드라이브)
GDRIVE_PATH = r"G:\내 드라이브\bithumb-campaign"
LOCAL_PATH = r"C:\bithumb-campaign"

def backup_to_gdrive():
    """로컬 파일을 Google Drive로 백업"""
    
    if not os.path.exists(GDRIVE_PATH):
        print(f"Google Drive 경로를 찾을 수 없습니다: {GDRIVE_PATH}")
        print("Google Drive 데스크톱이 설치되어 있는지 확인하세요.")
        return
    
    # contents 폴더 백업
    local_contents = os.path.join(LOCAL_PATH, "contents")
    gdrive_contents = os.path.join(GDRIVE_PATH, "contents")
    
    if os.path.exists(local_contents):
        shutil.copytree(local_contents, gdrive_contents, dirs_exist_ok=True)
        print(f"백업 완료: contents → {gdrive_contents}")
    
    # 리포트 백업
    local_reports = os.path.join(LOCAL_PATH, "reports")
    gdrive_reports = os.path.join(GDRIVE_PATH, "reports")
    
    if os.path.exists(local_reports):
        shutil.copytree(local_reports, gdrive_reports, dirs_exist_ok=True)
        print(f"백업 완료: reports → {gdrive_reports}")
    
    # 백업 로그
    with open(os.path.join(GDRIVE_PATH, "last_backup.txt"), "w") as f:
        f.write(f"마지막 백업: {datetime.now()}")
    
    print("Google Drive 백업 완료!")

if __name__ == "__main__":
    backup_to_gdrive()
