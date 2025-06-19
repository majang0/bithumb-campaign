# Knowledge 4: 빗썸 자동화 시스템 환경 정보

## 프로젝트 기본 정보
- **프로젝트명**: 빗썸 친구초대 캠페인 자동화 시스템
- **로컬 경로**: `C:\bithumb-campaign`
- **목표**: 추천인 1,000명 달성
- **추천코드**: W1HGATYGVW
- **추천링크**: https://m.bithumb.com/react/referral/guide?referral=W1HGATYGVW

## GitHub 환경
- **사용자명**: majang0
- **저장소명**: bithumb-campaign
- **저장소 URL**: https://github.com/majang0/bithumb-campaign
- **기본 브랜치**: main
- **저장소 타입**: Private (비공개)
- **협업자**: 없음 (개인 프로젝트)
- **생성일**: 2025-06-19

## Google Cloud Platform 정보
- **프로젝트 ID**: level-unfolding-463403-i9
- **사용자 이메일**: giho0540@gmail.com
- **OAuth 2.0 클라이언트 ID**: 545611496389-92g8nia4n2b90ipjf24nhqml98jrgbru.apps.googleusercontent.com

### 활성화된 Google 서비스
1. **Google Drive**
   - 파일 저장 및 백업
   - 콘텐츠 관리
   - 리포트 저장
   
2. **Google Calendar**
   - 콘텐츠 발행 스케줄 관리
   - 캠페인 일정 추적
   
3. **Google Docs**
   - 콘텐츠 초안 작성
   - 협업 문서 관리

## 개발 환경
- **Python 버전**: 3.13.5
- **운영체제**: Windows
- **가상환경**: 미설정 (추후 설정 필요)

## MCP (Model Context Protocol) 설정
- **설정 파일**: `C:\bithumb-campaign\mcp_full_config.json`
- **활성화된 MCP 서버**:
  - filesystem (로컬 파일 접근)
  - sequential-thinking (사고 과정 도구)
  - sqlite (데이터베이스)
  - github (GitHub 연동)
  - brave-search (웹 검색) - API 키 미설정
  - slack - 미설정

## 프로젝트 구조
```
C:\bithumb-campaign\
├── .github/workflows/     # GitHub Actions 워크플로우 (비어있음)
├── contents/              # 콘텐츠 관리
│   ├── pending/          # 발행 대기 콘텐츠
│   ├── published/        # 발행 완료 콘텐츠
│   └── templates/        # 콘텐츠 템플릿
├── data/                 # 데이터 저장소
│   └── campaign.db       # SQLite 데이터베이스
├── reports/              # 리포트 저장 폴더
├── n8n/                  # n8n 워크플로우 파일
└── log/                  # 로그 파일 저장

```

## 주요 파일 설명
- `automation.py`: 메인 자동화 스크립트 (미구현)
- `report.py`: 리포트 생성 스크립트
- `content_helper.py`: 콘텐츠 생성 도우미
- `config.json`: 프로젝트 설정 파일
- `requirements.txt`: Python 패키지 목록

## Git 설정
- **사용자명**: majang0
- **이메일**: giho0540@gmail.com
- **원격 저장소**: origin (https://github.com/majang0/bithumb-campaign.git)

## 보안 관련
- `.gitignore` 파일이 설정되어 민감한 정보 제외
- 모든 API 키와 인증 정보는 환경 변수나 별도 파일로 관리
- GitHub Personal Access Token은 MCP 설정에 저장

## 향후 구현 예정
1. **API 연동**
   - Telegram Bot API
   - Twitter API
   - 네이버 블로그 API
   - Brave Search API

2. **자동화 워크플로우**
   - n8n 설정 및 워크플로우 구성
   - 스케줄링 설정
   - 멀티 플랫폼 배포 자동화

3. **개발 환경**
   - Python 가상환경 설정
   - 의존성 패키지 설치

## 프로젝트 운영 지침
- 모든 코드는 GitHub에 커밋하여 버전 관리
- Google Drive는 콘텐츠와 리포트 백업용으로 사용
- 민감한 정보는 절대 GitHub에 커밋하지 않음
- 정기적으로 데이터베이스 백업 수행

## 연락처 및 관리자
- **프로젝트 관리자**: 마장 (majang0)
- **이메일**: giho0540@gmail.com
- **GitHub**: https://github.com/majang0

이 문서는 빗썸 자동화 시스템의 환경 설정과 관련된 모든 정보를 담고 있으며, 
프로젝트 진행 시 참조해야 할 핵심 정보들을 포함하고 있다.
