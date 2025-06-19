import logging
from datetime import datetime
import os

def setup_logger(name='bithumb_campaign'):
    """로거 설정"""
    
    # 로그 디렉토리 생성
    log_dir = r'C:\bithumb-campaign\logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 로그 파일명 (날짜별)
    log_file = os.path.join(log_dir, f'{name}_{datetime.now().strftime("%Y%m%d")}.log')
    
    # 로거 생성
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # 파일 핸들러
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 포맷터
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 핸들러 추가
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# 사용 예시
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("로깅 시스템 테스트")
    logger.warning("경고 메시지 테스트")
    logger.error("에러 메시지 테스트")
