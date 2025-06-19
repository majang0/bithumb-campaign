import os
import json
import sqlite3
from datetime import datetime
import schedule
import time

class BithumbCampaignAutomation:
    def __init__(self):
        self.base_path = r"C:\bithumb-campaign"
        self.pending_path = os.path.join(self.base_path, "contents", "pending")
        self.published_path = os.path.join(self.base_path, "contents", "published")
        self.db_path = os.path.join(self.base_path, "data", "campaign.db")
        
    def process_pending_contents(self):
        """pending 폴더의 콘텐츠를 처리"""
        print(f"[{datetime.now()}] 콘텐츠 처리 시작...")
        
        # pending 폴더의 JSON 파일 목록
        files = [f for f in os.listdir(self.pending_path) if f.endswith('.json')]
        
        for filename in files:
            filepath = os.path.join(self.pending_path, filename)
            
            # JSON 파일 읽기
            with open(filepath, 'r', encoding='utf-8') as f:
                content = json.load(f)
            
            # 여기에 실제 게시 로직 추가
            # 예: API 호출, 웹 스크래핑 등
            print(f"게시 중: {content['title']}")
            
            # 게시 완료 후 published로 이동
            new_path = os.path.join(self.published_path, filename)
            os.rename(filepath, new_path)
            
            # DB에 기록
            self.log_to_database(content, filename)
            
            print(f"완료: {filename}")
    
    def log_to_database(self, content, filename):
        """게시 이력을 DB에 저장"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO contents (title, content, type, platform, status, published_at)
            VALUES (?, ?, ?, ?, 'published', datetime('now'))
        """, (content['title'], content['content'], content['type'], content['platform']))
        
        conn.commit()
        conn.close()
    
    def create_content_from_template(self, title, body):
        """Claude가 호출할 수 있는 콘텐츠 생성 함수"""
        content = {
            "id": f"blog_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "title": title,
            "content": body,
            "type": "blog",
            "platform": "naver",
            "tags": ["빗썸", "가상자산", "이벤트", "7만원"],
            "referral_code": "MAJANG2025",
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "author": "마장"
        }
        
        filename = f"{content['id']}.json"
        filepath = os.path.join(self.pending_path, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        
        return filename
    
    def run_scheduler(self):
        """스케줄러 실행"""
        # 매일 9시, 14시, 19시에 실행
        schedule.every().day.at("09:00").do(self.process_pending_contents)
        schedule.every().day.at("14:00").do(self.process_pending_contents)
        schedule.every().day.at("19:00").do(self.process_pending_contents)
        
        print("스케줄러 시작됨. Ctrl+C로 종료하세요.")
        while True:
            schedule.run_pending()
            time.sleep(60)  # 1분마다 체크

if __name__ == "__main__":
    automation = BithumbCampaignAutomation()
    
    # 수동 실행 테스트
    # automation.process_pending_contents()
    
    # 스케줄러 실행
    automation.run_scheduler()
