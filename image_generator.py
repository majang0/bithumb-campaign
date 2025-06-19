# 이미지 생성 헬퍼 스크립트
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

class ThumbnailGenerator:
    def __init__(self, base_path=r"C:\bithumb-campaign"):
        self.base_path = base_path
        self.assets_path = os.path.join(base_path, "assets")
        self.output_path = os.path.join(base_path, "images")
        
        # 폴더 생성
        os.makedirs(self.assets_path, exist_ok=True)
        os.makedirs(self.output_path, exist_ok=True)
    
    def create_blog_thumbnail(self, title, subtitle="빗썸 7만원 이벤트"):
        """블로그 썸네일 이미지 생성"""
        
        # 이미지 크기 (네이버 블로그 권장)
        width, height = 1200, 630
        
        # 배경 이미지 생성
        img = Image.new('RGB', (width, height), color='#0052FF')  # 빗썸 블루
        draw = ImageDraw.Draw(img)
        
        # 폰트 설정 (시스템 폰트 사용)
        try:
            title_font = ImageFont.truetype("arial.ttf", 60)
            subtitle_font = ImageFont.truetype("arial.ttf", 40)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
        
        # 텍스트 그리기
        draw.text((50, 200), title, fill='white', font=title_font)
        draw.text((50, 300), subtitle, fill='#FFD700', font=subtitle_font)
        
        # 7만원 강조
        draw.text((50, 400), "7만원", fill='#FFD700', font=ImageFont.truetype("arial.ttf", 120))
        
        # 파일명 생성
        filename = f"thumb_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_path, filename)
        
        # 이미지 저장
        img.save(filepath)
        
        return filepath
    
    def create_sns_image(self, message, platform="instagram"):
        """SNS용 정사각형 이미지 생성"""
        
        # 플랫폼별 크기
        sizes = {
            "instagram": (1080, 1080),
            "twitter": (1200, 675),
            "telegram": (800, 800)
        }
        
        width, height = sizes.get(platform, (1080, 1080))
        
        # 이미지 생성
        img = Image.new('RGB', (width, height), color='#0052FF')
        draw = ImageDraw.Draw(img)
        
        # 메시지 그리기
        draw.text((50, height//2), message, fill='white', font=ImageFont.load_default())
        
        # 저장
        filename = f"{platform}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_path, filename)
        img.save(filepath)
        
        return filepath

# 사용 예시
if __name__ == "__main__":
    generator = ThumbnailGenerator()
    
    # 블로그 썸네일 생성
    thumb = generator.create_blog_thumbnail("지금 가입하면 7만원?!")
    print(f"썸네일 생성됨: {thumb}")
    
    # SNS 이미지 생성
    sns = generator.create_sns_image("빗썸 7만원 받으러 가기 >>", "instagram")
    print(f"SNS 이미지 생성됨: {sns}")
