import requests
from datetime import datetime
import json

class SEOOptimizer:
    """SEO 최적화 및 키워드 전략 도구"""
    
    def __init__(self):
        self.primary_keywords = [
            "빗썸 추천인",
            "빗썸 추천코드", 
            "빗썸 이벤트",
            "빗썸 7만원",
            "빗썸 가입 혜택"
        ]
        
        self.secondary_keywords = [
            "가상화폐 시작",
            "비트코인 거래소",
            "암호화폐 투자",
            "재테크 꿀팁",
            "대학생 용돈벌이"
        ]
        
        self.long_tail_keywords = [
            "빗썸 신규가입 7만원 받는법",
            "빗썸 추천인 코드 W1HGATYGVW",
            "빗썸 친구초대 이벤트 2025",
            "빗썸 가입 혜택 정리",
            "빗썸 첫가입 보너스"
        ]
        
    def generate_seo_title(self, platform="blog"):
        """플랫폼별 SEO 최적화 제목 생성"""
        templates = {
            "blog": [
                "{primary} 2025년 최신 정보 총정리",
                "{primary} {secondary} 완벽 가이드",
                "{long_tail} (실제 후기)",
                "솔직후기: {primary} 직접 해본 결과"
            ],
            "community": [
                "{primary} 아직도 모르는 사람?",
                "방금 {primary} 해봤는데",
                "{secondary} 시작하려면 {primary} 필수"
            ],
            "sns": [
                "💰 {primary} 💰",
                "🔥 {long_tail} 🔥",
                "✅ {primary} ✅ {secondary}"
            ]
        }
        
        import random
        template = random.choice(templates.get(platform, templates["blog"]))
        
        title = template.format(
            primary=random.choice(self.primary_keywords),
            secondary=random.choice(self.secondary_keywords),
            long_tail=random.choice(self.long_tail_keywords)
        )
        
        return title
    
    def analyze_keyword_density(self, content):
        """키워드 밀도 분석"""
        words = content.lower().split()
        total_words = len(words)
        
        keyword_counts = {}
        all_keywords = self.primary_keywords + self.secondary_keywords
        
        for keyword in all_keywords:
            count = content.lower().count(keyword.lower())
            density = (count / total_words) * 100 if total_words > 0 else 0
            keyword_counts[keyword] = {
                "count": count,
                "density": round(density, 2)
            }
            
        return keyword_counts
    
    def optimize_content(self, content, target_platform="blog"):
        """콘텐츠 SEO 최적화"""
        optimized = content
        
        # 추천코드 강조
        optimized = optimized.replace(
            "W1HGATYGVW", 
            "**W1HGATYGVW**" if target_platform == "blog" else "W1HGATYGVW"
        )
        
        # 키워드 자연스럽게 추가
        if "빗썸" not in content[:50]:
            optimized = "빗썸 " + optimized
            
        # 메타 설명 생성
        meta_description = self._generate_meta_description(content)
        
        return {
            "content": optimized,
            "meta_description": meta_description,
            "suggested_tags": self._generate_tags(target_platform)
        }
    
    def _generate_meta_description(self, content):
        """메타 설명 생성"""
        description = content[:150].replace("\n", " ")
        if "W1HGATYGVW" not in description:
            description += " 추천코드: W1HGATYGVW"
        return description
    
    def _generate_tags(self, platform):
        """플랫폼별 태그 생성"""
        base_tags = ["빗썸", "빗썸이벤트", "가상화폐", "비트코인", "재테크"]
        
        platform_tags = {
            "blog": base_tags + ["빗썸추천인", "빗썸가입", "암호화폐거래소"],
            "instagram": ["#" + tag for tag in base_tags] + ["#용돈벌이", "#대학생재테크"],
            "youtube": base_tags + ["빗썸가입방법", "빗썸7만원", "코인거래소"]
        }
        
        return platform_tags.get(platform, base_tags)

# 사용 예시
if __name__ == "__main__":
    seo = SEOOptimizer()
    
    # SEO 제목 생성
    print("블로그 제목:", seo.generate_seo_title("blog"))
    print("커뮤니티 제목:", seo.generate_seo_title("community"))
    print("SNS 제목:", seo.generate_seo_title("sns"))