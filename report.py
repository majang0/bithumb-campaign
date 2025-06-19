import sqlite3
import json
from datetime import datetime, timedelta
import os

def generate_report():
    """성과 리포트 생성"""
    base_path = r"C:\bithumb-campaign"
    db_path = os.path.join(base_path, "data", "campaign.db")
    
    # DB 연결
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 최근 7일간 게시된 콘텐츠
    cursor.execute("""
        SELECT COUNT(*), platform 
        FROM contents 
        WHERE published_at > datetime('now', '-7 days')
        GROUP BY platform
    """)
    
    recent_posts = cursor.fetchall()
    
    # 전체 통계
    cursor.execute("SELECT COUNT(*) FROM contents WHERE status = 'published'")
    total_published = cursor.fetchone()[0]
    
    # pending 콘텐츠 수
    pending_path = os.path.join(base_path, "contents", "pending")
    pending_count = len([f for f in os.listdir(pending_path) if f.endswith('.json')])
    
    # 리포트 생성
    report = {
        "generated_at": datetime.now().isoformat(),
        "total_published": total_published,
        "pending_contents": pending_count,
        "recent_7days": dict(recent_posts) if recent_posts else {},
        "next_actions": [
            f"{pending_count}개의 대기 중인 콘텐츠가 있습니다." if pending_count > 0 else "새 콘텐츠 생성이 필요합니다.",
            "다음 자동 실행: 오늘 14:00 (또는 19:00)"
        ]
    }
    
    # 리포트 저장
    report_path = os.path.join(base_path, "reports", f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    # 콘솔 출력
    print("\n=== 빗썸 캠페인 리포트 ===")
    print(f"총 게시 콘텐츠: {total_published}개")
    print(f"대기 중 콘텐츠: {pending_count}개")
    print(f"최근 7일 게시: {sum(count for count, _ in recent_posts) if recent_posts else 0}개")
    print(f"\n리포트 저장됨: {report_path}")
    
    conn.close()
    return report

if __name__ == "__main__":
    generate_report()
