import os
import shutil
from datetime import datetime
import json
from pathlib import Path

class GoogleDriveSync:
    """Google Drive 데스크톱 앱을 활용한 동기화"""
    
    def __init__(self):
        # Google Drive 데스크톱 경로 (보통 여기 있음)
        self.gdrive_paths = [
            r"G:\내 드라이브",  # Google Drive 기본 경로
            r"C:\Users\%USERNAME%\Google Drive",
            r"C:\Users\%USERNAME%\GoogleDrive"
        ]
        
        self.gdrive_path = None
        self.campaign_folder = None
        
        # Google Drive 경로 찾기
        for path in self.gdrive_paths:
            expanded_path = os.path.expandvars(path)
            if os.path.exists(expanded_path):
                self.gdrive_path = expanded_path
                break
        
        if self.gdrive_path:
            self.campaign_folder = os.path.join(self.gdrive_path, "bithumb-campaign")
            os.makedirs(self.campaign_folder, exist_ok=True)
            print(f"Google Drive 폴더 찾음: {self.campaign_folder}")
        else:
            print("Google Drive 데스크톱이 설치되어 있지 않습니다.")
    
    def backup_content(self, local_file, subfolder="contents"):
        """로컬 파일을 Google Drive로 백업"""
        if not self.campaign_folder:
            return False
        
        # 대상 폴더 생성
        target_folder = os.path.join(self.campaign_folder, subfolder)
        os.makedirs(target_folder, exist_ok=True)
        
        # 파일 복사
        filename = os.path.basename(local_file)
        target_path = os.path.join(target_folder, filename)
        
        try:
            shutil.copy2(local_file, target_path)
            print(f"백업 완료: {filename} → Google Drive")
            
            # 백업 로그 기록
            self._log_backup(filename, subfolder)
            return True
        except Exception as e:
            print(f"백업 실패: {e}")
            return False
    
    def sync_folder(self, local_folder, gdrive_subfolder):
        """전체 폴더 동기화"""
        if not self.campaign_folder:
            return False
        
        target_folder = os.path.join(self.campaign_folder, gdrive_subfolder)
        
        try:
            # 폴더 전체 복사 (미러링)
            if os.path.exists(target_folder):
                shutil.rmtree(target_folder)
            shutil.copytree(local_folder, target_folder)
            
            print(f"폴더 동기화 완료: {local_folder} → {gdrive_subfolder}")
            return True
        except Exception as e:
            print(f"동기화 실패: {e}")
            return False
    
    def _log_backup(self, filename, subfolder):
        """백업 이력 기록"""
        log_file = os.path.join(self.campaign_folder, "backup_log.json")
        
        # 기존 로그 읽기
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
        else:
            log_data = {"backups": []}
        
        # 새 백업 기록 추가
        log_data["backups"].append({
            "filename": filename,
            "subfolder": subfolder,
            "timestamp": datetime.now().isoformat(),
            "size": os.path.getsize(os.path.join("C:\\bithumb-campaign", subfolder, filename))
        })
        
        # 로그 저장
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)

# 사용 예시
if __name__ == "__main__":
    sync = GoogleDriveSync()
    
    # 테스트: pending 폴더의 모든 파일 백업
    local_path = r"C:\bithumb-campaign\contents\pending"
    if os.path.exists(local_path):
        for file in os.listdir(local_path):
            if file.endswith('.json'):
                file_path = os.path.join(local_path, file)
                sync.backup_content(file_path, "contents/pending")
