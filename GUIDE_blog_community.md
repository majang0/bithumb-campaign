# 빗썸 캠페인 블로그/커뮤니티 홍보 실행 가이드

## 🚀 빠른 시작 가이드

### 1단계: 플랫폼 계정 준비
- [ ] 네이버 블로그 (기존 운영중)
- [ ] 네이버 카페 회원가입 (재테크 카페 5개)
- [ ] 디시인사이드 계정
- [ ] 클리앙 계정
- [ ] 뽐뿌 계정
- [ ] 에브리타임 계정 (대학 인증)
- [ ] 인스타그램 계정
- [ ] 페이스북 계정

### 2단계: 초기 콘텐츠 준비
```bash
# 콘텐츠 템플릿 확인
cat C:\bithumb-campaign\contents\templates\platform_templates.md

# 첫 콘텐츠 생성 (각 플랫폼별 3개씩)
python C:\bithumb-campaign\content_helper.py --platform all --count 3
```

### 3단계: 자동화 스케줄 설정
```bash
# 주간 스케줄 생성
python C:\bithumb-campaign\automation\content_scheduler.py

# 스케줄 확인
cat C:\bithumb-campaign\schedules\weekly_schedule.json
```

## 📝 일일 운영 체크리스트

### 오전 (09:00-12:00)
1. **네이버 블로그 포스팅**
   - SEO 최적화 제목 사용
   - 이미지 2-3개 포함
   - 추천코드 3회 이상 언급

2. **커뮤니티 모니터링**
   - 전날 포스팅 반응 확인
   - 댓글 응대
   - 추가 정보 제공

### 오후 (14:00-17:00)
1. **커뮤니티 포스팅**
   - 점심시간 후 활동 시간대 활용
   - 각 커뮤니티별 톤 맞춤
   - 자연스러운 대화 유도

2. **경쟁사 모니터링**
   ```bash
   python C:\bithumb-campaign\automation\competitor_monitor.py
   ```

### 저녁 (19:00-21:00)
1. **SNS 포스팅**
   - 인스타그램 스토리/피드
   - 페이스북 그룹 공유

2. **일일 리포트 확인**
   ```bash
   python C:\bithumb-campaign\automation\campaign_dashboard.py
   ```

## 🎯 주요 전략 포인트

### 콘텐츠 작성 시
1. **신뢰성 구축**
   - 실제 인증 스크린샷 활용
   - 구체적인 날짜와 금액 명시
   - 주의사항 투명하게 공개

2. **차별화 포인트**
   - 7만원 vs 타사 5천원 비교
   - 즉시 현금 지급 강조
   - 간단한 가입 절차 (10분)

3. **행동 유도**
   - 추천코드 복사하기 쉽게 표시
   - 긴급성 부여 (이벤트 종료 가능성)
   - 질문 유도로 댓글 활성화

### 플랫폼별 최적 시간대
- **블로그**: 09:00, 14:00, 19:00
- **디시인사이드**: 12:00-14:00, 19:00-21:00
- **클리앙**: 10:00-12:00, 20:00-22:00
- **에브리타임**: 12:00-13:00, 18:00-19:00
- **인스타그램**: 12:00, 18:00-20:00

## 📊 성과 측정 및 개선

### 일일 KPI
- 신규 추천인: 30-50명 목표
- 포스팅 수: 10-15개
- 전환율: 10-15%

### 주간 분석
```bash
# 주간 리포트 생성
python -c "from automation.campaign_dashboard import CampaignDashboard; d=CampaignDashboard(); d.export_report('weekly')"
```

### A/B 테스트 항목
1. **제목 테스트**
   - 금액 강조 vs 간편함 강조
   - 긴급성 vs 신뢰성

2. **콘텐츠 형식**
   - 경험담 vs 정보 전달
   - 짧은 글 vs 상세 가이드

3. **CTA 문구**
   - "지금 바로" vs "천천히 확인"
   - 추천코드 위치 (상단/중간/하단)

## 🚨 주의사항

1. **스팸 방지**
   - 동일 내용 반복 게시 금지
   - 각 플랫폼별 변형 필수
   - 자연스러운 활동 패턴 유지

2. **규정 준수**
   - 각 커뮤니티 규칙 확인
   - 광고성 표시 (필요시)
   - 과장/허위 정보 금지

3. **계정 관리**
   - 여러 계정 사용 시 IP 주의
   - 활동 기록 문서화
   - 정기적 비밀번호 변경

## 🔧 문제 해결

### 전환율이 낮을 때
1. 콘텐츠 신뢰도 점검
2. CTA 문구 수정
3. 타겟 커뮤니티 재선정

### 계정 제재 시
1. 해당 플랫폼 규정 재확인
2. 콘텐츠 톤 조정
3. 활동 빈도 감소

### 경쟁사 대응
1. 차별화 포인트 강화
2. 비교 콘텐츠 제작
3. 독점 혜택 강조

## 📞 지원 및 문의

- 프로젝트 관리: 마장 (majang0)
- GitHub: https://github.com/majang0/bithumb-campaign
- Slack: 새-워크스페이스 #bithumb-campaign

---

마지막 업데이트: 2025-06-19
추천코드: **W1HGATYGVW**