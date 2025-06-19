import os
import subprocess
from datetime import datetime

def git_backup():
    """GitHub로 자동 백업"""
    
    os.chdir(r"C:\bithumb-campaign")
    
    # Git 초기화 (처음 한 번만)
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/YOUR_USERNAME/bithumb-campaign.git"])
    
    # 변경사항 추가
    subprocess.run(["git", "add", "."])
    
    # 커밋
    commit_msg = f"자동 백업: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    
    # 푸시
    subprocess.run(["git", "push", "origin", "main"])
    
    print("GitHub 백업 완료!")

if __name__ == "__main__":
    git_backup()
