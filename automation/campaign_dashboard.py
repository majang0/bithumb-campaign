import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

class CampaignDashboard:
    """캠페인 통합 대시보드 및 리포팅"""
    
    def __init__(self, db_path="C:/bithumb-campaign/data/campaign.db"):
        self.db_path = db_path
        
    def generate_daily_report(self):
        """일일 성과 리포트 생성"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        today = datetime.now().date()
        
        # 플랫폼별 성과 집계
        cursor.execute('''
            SELECT platform, 
                   COUNT(*) as posts,
                   SUM(views) as total_views,
                   SUM(clicks) as total_clicks,
                   SUM(conversions) as total_conversions
            FROM platform_performance
            WHERE DATE(posted_at) = ?
            GROUP BY platform
        ''', (today,))
        
        platform_stats = cursor.fetchall()
        
        # 전체 추천인 수
        cursor.execute('''
            SELECT COUNT(*) FROM referrals
            WHERE DATE(created_at) = ?
        ''', (today,))
        
        daily_referrals = cursor.fetchone()[0]
        
        # 리포트 생성
        report = {
            "date": str(today),
            "summary": {
                "total_referrals": daily_referrals,
                "target": 50,  # 일일 목표
                "achievement_rate": (daily_referrals / 50) * 100
            },
            "platforms": {},
            "top_content": [],
            "recommendations": []
        }
        
        # 플랫폼별 상세 정보
        for platform, posts, views, clicks, conversions in platform_stats:
            report["platforms"][platform] = {
                "posts": posts,
                "views": views or 0,
                "clicks": clicks or 0,
                "conversions": conversions or 0,
                "conversion_rate": (conversions / clicks * 100) if clicks else 0
            }
        
        # 추천사항 생성
        if daily_referrals < 30:
            report["recommendations"].append("포스팅 빈도를 늘려주세요")
            report["recommendations"].append("커뮤니티 활동을 강화해주세요")
        
        conn.close()
        return report
    
    def generate_weekly_analytics(self):
        """주간 분석 리포트"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 지난 7일간 데이터
        week_ago = datetime.now() - timedelta(days=7)
        
        cursor.execute('''
            SELECT DATE(created_at) as date, COUNT(*) as count
            FROM referrals
            WHERE created_at >= ?
            GROUP BY DATE(created_at)
            ORDER BY date
        ''', (week_ago,))
        
        daily_trends = cursor.fetchall()
        
        # 플랫폼별 효율성
        cursor.execute('''
            SELECT platform,
                   COUNT(*) as total_posts,
                   SUM(conversions) as total_conversions,
                   AVG(conversion_rate) as avg_conversion_rate
            FROM platform_performance
            WHERE posted_at >= ?
            GROUP BY platform
            ORDER BY total_conversions DESC
        ''', (week_ago,))
        
        platform_efficiency = cursor.fetchall()
        
        # 최고 성과 콘텐츠
        cursor.execute('''
            SELECT post_title, platform, conversions
            FROM platform_performance
            WHERE posted_at >= ? AND conversions > 0
            ORDER BY conversions DESC
            LIMIT 5
        ''', (week_ago,))
        
        top_content = cursor.fetchall()
        
        analytics = {
            "period": f"{week_ago.date()} ~ {datetime.now().date()}",
            "total_referrals": sum([count for _, count in daily_trends]),
            "daily_average": sum([count for _, count in daily_trends]) / 7,
            "daily_trends": [{"date": date, "count": count} for date, count in daily_trends],
            "platform_efficiency": [
                {
                    "platform": platform,
                    "posts": posts,
                    "conversions": conversions or 0,
                    "efficiency": (conversions / posts) if posts else 0
                }
                for platform, posts, conversions, _ in platform_efficiency
            ],
            "top_performing_content": [
                {"title": title, "platform": platform, "conversions": conversions}
                for title, platform, conversions in top_content
            ]
        }
        
        conn.close()
        return analytics
    
    def send_slack_report(self, report_type="daily"):
        """Slack으로 리포트 전송"""
        if report_type == "daily":
            report = self.generate_daily_report()
            message = f"""
📊 *빗썸 캠페인 일일 리포트* ({report['date']})

*오늘의 성과*
• 신규 추천인: {report['summary']['total_referrals']}명
• 목표 달성률: {report['summary']['achievement_rate']:.1f}%

*플랫폼별 성과*
"""
            for platform, stats in report['platforms'].items():
                message += f"• {platform}: {stats['conversions']}명 (전환율 {stats['conversion_rate']:.1f}%)\n"
            
            if report['recommendations']:
                message += "\n*개선 제안*\n"
                for rec in report['recommendations']:
                    message += f"• {rec}\n"
                    
        else:  # weekly
            analytics = self.generate_weekly_analytics()
            message = f"""
📈 *빗썸 캠페인 주간 분석* ({analytics['period']})

*주간 총 추천인*: {analytics['total_referrals']}명
*일 평균*: {analytics['daily_average']:.1f}명

*플랫폼 효율성 TOP 3*
"""
            for i, platform in enumerate(analytics['platform_efficiency'][:3]):
                message += f"{i+1}. {platform['platform']}: {platform['conversions']}명\n"
        
        # Slack 전송 코드 (실제 구현 시)
        return message
    
    def export_report(self, report_type="daily", format="json"):
        """리포트 파일로 내보내기"""
        if report_type == "daily":
            data = self.generate_daily_report()
            filename = f"daily_report_{data['date']}"
        else:
            data = self.generate_weekly_analytics()
            filename = f"weekly_report_{datetime.now().strftime('%Y-%m-%d')}"
        
        filepath = Path(f"C:/bithumb-campaign/reports/{filename}.{format}")
        filepath.parent.mkdir(exist_ok=True)
        
        if format == "json":
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        
        return filepath

if __name__ == "__main__":
    dashboard = CampaignDashboard()
    
    # 일일 리포트 생성
    daily = dashboard.generate_daily_report()
    print("일일 리포트:", json.dumps(daily, ensure_ascii=False, indent=2))
    
    # Slack 메시지 미리보기
    slack_msg = dashboard.send_slack_report("daily")
    print("\nSlack 메시지:\n", slack_msg)