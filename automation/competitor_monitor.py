from datetime import datetime
import json
import sqlite3

class CompetitorMonitor:
    """경쟁사 이벤트 모니터링 시스템"""
    
    def __init__(self, db_path="C:/bithumb-campaign/data/campaign.db"):
        self.db_path = db_path
        self.competitors = {
            "upbit": {
                "keywords": ["업비트 추천", "업비트 이벤트", "업비트 가입"],
                "benefits": "추천인당 5천원",
                "url": "https://upbit.com"
            },
            "coinone": {
                "keywords": ["코인원 추천", "코인원 이벤트", "코인원 가입"],
                "benefits": "가입시 1만원",
                "url": "https://coinone.co.kr"
            },
            "korbit": {
                "keywords": ["코빗 추천", "코빗 이벤트", "코빗 가입"],
                "benefits": "수수료 할인",
                "url": "https://korbit.co.kr"
            },
            "gopax": {
                "keywords": ["고팍스 추천", "고팍스 이벤트", "고팍스 가입"],
                "benefits": "KLAY 에어드랍",
                "url": "https://gopax.co.kr"
            }
        }
        self._init_db()
    
    def _init_db(self):
        """데이터베이스 초기화"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS competitor_monitoring (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                competitor VARCHAR(50),
                event_type VARCHAR(100),
                event_details TEXT,
                benefits TEXT,
                start_date DATE,
                end_date DATE,
                source_url TEXT,
                monitored_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS competitor_content (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                competitor VARCHAR(50),
                platform VARCHAR(50),
                content_url TEXT,
                content_title TEXT,
                engagement_score INTEGER,
                found_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def search_competitor_content(self, competitor, platform="all"):
        """경쟁사 콘텐츠 검색"""
        # 실제로는 Brave Search API를 사용
        search_queries = []
        
        if platform == "all" or platform == "blog":
            for keyword in self.competitors[competitor]["keywords"]:
                search_queries.append(f"{keyword} site:blog.naver.com")
                search_queries.append(f"{keyword} site:tistory.com")
        
        if platform == "all" or platform == "community":
            for keyword in self.competitors[competitor]["keywords"]:
                search_queries.append(f"{keyword} site:dcinside.com")
                search_queries.append(f"{keyword} site:clien.net")
        
        return search_queries
    
    def analyze_competitor_strategy(self, competitor):
        """경쟁사 전략 분석"""
        analysis = {
            "competitor": competitor,
            "current_benefits": self.competitors[competitor]["benefits"],
            "our_benefits": "최대 7만원 (기본 5만원 + 웰컴미션 2만원)",
            "our_advantages": [],
            "recommendations": []
        }
        
        # 빗썸의 장점 분석
        if "5천원" in self.competitors[competitor]["benefits"]:
            analysis["our_advantages"].append("빗썸이 14배 더 높은 혜택 제공")
            analysis["recommendations"].append("금액 차이를 강조한 비교 콘텐츠 제작")
        
        if "수수료" in self.competitors[competitor]["benefits"]:
            analysis["our_advantages"].append("즉시 현금 지급 vs 수수료 할인")
            analysis["recommendations"].append("즉시성과 확실성 강조")
        
        return analysis
    
    def generate_counter_content(self, competitor):
        """경쟁사 대응 콘텐츠 생성 가이드"""
        templates = {
            "comparison": f"""
[비교 콘텐츠 템플릿]

제목: 빗썸 vs {competitor.upper()} 가입 혜택 완벽 비교 (2025년)

내용 구조:
1. 객관적 비교표
   - 빗썸: 최대 7만원 현금
   - {competitor.upper()}: {self.competitors[competitor]['benefits']}

2. 빗썸의 차별점
   - 업계 최고 수준의 현금 혜택
   - 간단한 가입 절차 (10분 이내)
   - 즉시 사용 가능한 현금 지급

3. 실제 후기
   "저는 두 거래소 모두 사용해봤는데, 빗썸의 혜택이 압도적이었습니다."

4. 추천 결론
   단기 혜택을 원한다면 → 빗썸 (추천코드: W1HGATYGVW)
   장기 투자를 원한다면 → 빗썸으로 시작 후 타 거래소 추가 이용
""",
            "highlight": f"""
[차별화 콘텐츠 템플릿]

제목: {competitor.upper()}보다 빗썸을 선택해야 하는 이유

1. 혜택 규모의 차이
   - 빗썸: 7만원 (현금)
   - {competitor.upper()}: {self.competitors[competitor]['benefits']}
   
2. 지급 방식의 차이
   - 빗썸: 조건 충족 즉시 현금 지급
   - 일반적인 타사: 포인트, 쿠폰, 할인 형태

3. 사용 제한의 차이
   - 빗썸: 30일 내 자유롭게 사용
   - 타사: 거래 조건, 기간 제한 등 복잡

추천코드: W1HGATYGVW
"""
        }
        
        return templates
    
    def save_monitoring_result(self, competitor, event_details):
        """모니터링 결과 저장"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO competitor_monitoring 
            (competitor, event_type, event_details, benefits, source_url)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            competitor,
            event_details.get('event_type', 'referral'),
            json.dumps(event_details, ensure_ascii=False),
            event_details.get('benefits', ''),
            event_details.get('source_url', '')
        ))
        
        conn.commit()
        conn.close()

if __name__ == "__main__":
    monitor = CompetitorMonitor()
    
    # 업비트 전략 분석
    analysis = monitor.analyze_competitor_strategy("upbit")
    print("업비트 대응 전략:", json.dumps(analysis, ensure_ascii=False, indent=2))
    
    # 대응 콘텐츠 템플릿
    templates = monitor.generate_counter_content("upbit")
    print("\n비교 콘텐츠 템플릿:", templates["comparison"])