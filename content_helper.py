# Claude MCP 콘텐츠 생성 헬퍼
# Claude에게 다음과 같이 요청하세요:
# "빗썸 이벤트 블로그 글 작성해서 pending 폴더에 저장해줘"

import json
from datetime import datetime

def create_blog_content(title, content_body, tags=None):
    """블로그 콘텐츠 JSON 생성"""
    
    if tags is None:
        tags = ["빗썸", "가상자산", "이벤트", "7만원", "신규가입"]
    
    content = {
        "id": f"blog_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "title": title,
        "content": content_body,
        "type": "blog",
        "platform": "naver",
        "tags": tags,
        "referral_code": "MAJANG2025",
        "cta": "지금 바로 가입하고 7만원 받기",
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "author": "마장",
        "seo_keywords": ["빗썸 추천인", "빗썸 이벤트", "7만원 지급", "가상자산 초대코드"]
    }
    
    return content

# 사용 예시:
# content = create_blog_content(
#     "오늘만! 빗썸 가입하고 7만원 받는 방법",
#     "본문 내용..."
# )
