import os
import shutil
import json
from datetime import datetime
import zipfile

class BackupManager:
    def __init__(self, base_path=r"C:\bithumb-campaign"):
        self.base_path = base_path
        self.backup_path = os.path.join(base_path, "backups")
        os.makedirs(self.backup_path, exist_ok=True)
    
    def create_backup(self):
        """전체 프로젝트 백업 생성"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}.zip"
        backup_file = os.path.join(self.backup_path, backup_name)
        
        # 백업할 폴더들
        folders_to_backup = ["contents", "data", "reports", "templates"]
        
        with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder in folders_to_backup:
                folder_path = os.path.join(self.base_path, folder)
                if os.path.exists(folder_path):
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, self.base_path)
                            zipf.write(file_path, arcname)
        
        # 백업 메타데이터 저장
        metadata = {
            "timestamp": timestamp,
            "backup_file": backup_name,
            "size": os.path.getsize(backup_file),
            "folders": folders_to_backup
        }
        
        metadata_file = os.path.join(self.backup_path, "backup_metadata.json")
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as f:
                all_backups = json.load(f)
        else:
            all_backups = []
        
        all_backups.append(metadata)
        
        with open(metadata_file, 'w') as f:
            json.dump(all_backups, f, indent=2)
        
        print(f"백업 완료: {backup_file}")
        print(f"크기: {metadata['size'] / 1024 / 1024:.2f} MB")
        
        # 오래된 백업 삭제 (최근 5개만 유지)
        self.cleanup_old_backups(keep=5)
        
        return backup_file
    
    def cleanup_old_backups(self, keep=5):
        """오래된 백업 파일 삭제"""
        backups = []
        for file in os.listdir(self.backup_path):
            if file.startswith("backup_") and file.endswith(".zip"):
                file_path = os.path.join(self.backup_path, file)
                backups.append((file_path, os.path.getctime(file_path)))
        
        # 날짜순 정렬
        backups.sort(key=lambda x: x[1], reverse=True)
        
        # 오래된 백업 삭제
        for backup_path, _ in backups[keep:]:
            os.remove(backup_path)
            print(f"오래된 백업 삭제: {os.path.basename(backup_path)}")
    
    def restore_backup(self, backup_name):
        """백업 복원"""
        backup_file = os.path.join(self.backup_path, backup_name)
        
        if not os.path.exists(backup_file):
            print(f"백업 파일을 찾을 수 없습니다: {backup_name}")
            return False
        
        # 복원 전 현재 상태 백업
        print("복원 전 현재 상태를 백업합니다...")
        self.create_backup()
        
        # 복원
        with zipfile.ZipFile(backup_file, 'r') as zipf:
            zipf.extractall(self.base_path)
        
        print(f"백업 복원 완료: {backup_name}")
        return True
    
    def list_backups(self):
        """백업 목록 표시"""
        metadata_file = os.path.join(self.backup_path, "backup_metadata.json")
        
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as f:
                backups = json.load(f)
            
            print("\n=== 백업 목록 ===")
            for i, backup in enumerate(backups[-10:], 1):  # 최근 10개만
                print(f"{i}. {backup['backup_file']} - {backup['size'] / 1024 / 1024:.2f} MB")
        else:
            print("백업이 없습니다.")

# 사용 예시
if __name__ == "__main__":
    manager = BackupManager()
    
    # 백업 생성
    manager.create_backup()
    
    # 백업 목록 보기
    manager.list_backups()
