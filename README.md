# 빗썸 친구초대 캠페인 자동화 시스템

빗썸 친구초대 이벤트의 추천인 확산을 위한 자동화 시스템입니다.

## 🎯 프로젝트 목표
- **목표**: 추천인 1,000명 달성
- **추천코드**: W1HGATYGVW
- **추천링크**: https://m.bithumb.com/react/referral/guide?referral=W1HGATYGVW

## 📁 프로젝트 구조
```
bithumb-campaign/
├── contents/        # 콘텐츠 생성 및 관리
├── data/           # 데이터 저장소
├── reports/        # 리포트 생성
├── n8n/           # n8n 자동화 워크플로우
├── automation.py   # 메인 자동화 스크립트
├── report.py      # 리포트 생성 스크립트
└── config.json    # 설정 파일
```

## 🛠️ 기술 스택
- Python 3.x
- n8n (자동화 워크플로우)
- Google Drive API
- Telegram Bot API
- Twitter API
- BeautifulSoup4 (웹 스크래핑)
- Selenium (웹 자동화)

## 📋 주요 기능
1. **콘텐츠 자동 생성**
   - 블로그 포스트 생성
   - SNS 콘텐츠 생성
   - 이미지 생성

2. **멀티 플랫폼 배포**
   - 네이버 블로그
   - 트위터
   - 텔레그램
   - 유튜브 쇼츠 (예정)

3. **성과 추적 및 리포팅**
   - 추천인 수 추적
   - 일별/주별 리포트 생성
   - 성과 분석

## 🚀 시작하기

### 1. 환경 설정
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 필요한 패키지 설치
pip install -r requirements.txt
```

### 2. 설정 파일 구성
`config.json.example`을 복사하여 `config.json`을 생성하고 필요한 API 키와 설정을 입력하세요.

### 3. 실행
```bash
# 메인 자동화 실행
python automation.py

# 리포트 생성
python report.py
```

## 📊 캠페인 전략
1. **타겟 오디언스**: 20-30대 투자 관심층
2. **콘텐츠 전략**: 정보성 + 경험담 + 실용적 팁
3. **배포 주기**: 일 3-5회 콘텐츠 배포
4. **성과 지표**: 추천코드 입력 수, 콘텐츠 도달률

## 🔐 보안 주의사항
- API 키와 인증 정보는 절대 커밋하지 마세요
- `.gitignore` 파일을 확인하여 민감한 파일이 제외되었는지 확인하세요

## 📝 라이센스
This project is private and confidential.
