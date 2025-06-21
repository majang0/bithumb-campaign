# 카멜레온 프로토콜 v3.0 n8n 워크플로우 설정

## 🔄 워크플로우 A: 앵커 콘텐츠 생성 (주 2회, 월/목)

### 노드 구성:
1. **Cron Trigger** - 월요일, 목요일 09:00 실행
2. **HTTP Request** - 카멜레온 엔진 호출
3. **Code** - 응답 파싱 및 다음 단계 준비
4. **Slack Notification** - 완료 알림

### 설정 상세:

#### 1. Cron Trigger 설정
```
Cron Expression: 0 9 * * 1,4
설명: 매주 월요일, 목요일 오전 9시 실행
```

#### 2. HTTP Request 설정
```javascript
Method: POST
URL: http://localhost:5000/generate_anchor
Headers:
- Content-Type: application/json

Body:
{
  "topic": "빗썸 신규가입 7만원 이벤트 완벽 가이드",
  "seo_focus": true,
  "target_length": 1500
}
```

#### 3. Code 노드 (앵커 응답 처리)
```javascript
// 카멜레온 엔진에서 받은 앵커 콘텐츠 처리
const anchorData = $input.first().json;

const result = {
  type: "anchor_content",
  platform: anchorData.platform,
  topic: anchorData.topic,
  content: anchorData.content,
  length: anchorData.length,
  referral_code: anchorData.referral_code,
  next_actions: [
    "midjourney_image_generation",
    "canva_design_creation", 
    "google_drive_storage",
    "puppeteer_blog_publishing"
  ],
  generated_at: new Date().toISOString()
};

console.log(`✅ 앵커 콘텐츠 생성 완료: ${anchorData.topic}`);
console.log(`📝 길이: ${anchorData.length}자`);
console.log(`🎯 추천코드: ${anchorData.referral_code}`);

return [{ json: result }];
```

---

## 🔄 워크플로우 B: 위성 콘텐츠 확산 (3분마다 50% 확률)

### 노드 구성:
1. **Schedule Trigger** - 3분마다 실행
2. **IF** - 50% 확률 체크
3. **HTTP Request** - 카멜레온 엔진 호출
4. **Code** - 응답 파싱 및 포스팅 준비
5. **HTTP Request** - Puppeteer 자동 포스팅 (옵션)
6. **SQLite** - 로그 기록

### 설정 상세:

#### 1. Schedule Trigger 설정
```
Interval: Every 3 minutes
Cron Expression: */3 * * * *
```

#### 2. IF 노드 (50% 확률 체크)
```javascript
Condition Type: Expression
Expression: {{Math.random() < 0.5}}
설명: 50% 확률로 위성 콘텐츠 생성
```

#### 3. HTTP Request 설정 (위성 콘텐츠)
```javascript
Method: POST
URL: http://localhost:5000/generate_satellite
Headers:
- Content-Type: application/json

Body:
{
  "platform": "auto_select",
  "apply_cameleon_rules": true,
  "include_trending": true
}
```

#### 4. Code 노드 (위성 응답 처리)
```javascript
// 카멜레온 엔진에서 받은 위성 콘텐츠 처리
const satelliteData = $input.first().json;

const result = {
  type: "satellite_content",
  platform: satelliteData.platform,
  content: satelliteData.content,
  persona: satelliteData.persona,
  length: satelliteData.length,
  referral_code: satelliteData.referral_code,
  execution_id: satelliteData.execution_id,
  ready_to_post: true,
  cameleon_rules_applied: [
    "persona_emulation",
    "context_mimicry", 
    "camouflage_technique",
    "natural_anchor_linking",
    "subtle_referral_placement"
  ],
  generated_at: new Date().toISOString()
};

console.log(`🛰️ 위성 콘텐츠 생성: ${satelliteData.platform}`);
console.log(`👤 페르소나: ${satelliteData.persona}`);
console.log(`📝 내용: ${satelliteData.content.substring(0, 100)}...`);
console.log(`🎯 추천코드: ${satelliteData.referral_code}`);

return [{ json: result }];
```

#### 5. Puppeteer 자동 포스팅 (옵션)
```javascript
Method: POST
URL: http://localhost:3000/puppeteer/post
Headers:
- Content-Type: application/json

Body:
{
  "platform": "{{$json.platform}}",
  "content": "{{$json.content}}",
  "execution_id": "{{$json.execution_id}}",
  "security": {
    "rotate_ip": true,
    "human_behavior": true,
    "random_delay": true
  }
}
```

---

## 🎯 통합 모니터링 워크플로우

### 노드 구성:
1. **Schedule Trigger** - 매일 18:00 실행
2. **HTTP Request** - 통계 조회
3. **Code** - 리포트 생성
4. **Slack** - 일일 성과 리포트

#### HTTP Request (통계 조회)
```javascript
Method: GET
URL: http://localhost:5000/cameleon_stats
```

#### Code 노드 (리포트 생성)
```javascript
// 카멜레온 프로토콜 일일 성과 리포트
const stats = $input.first().json;

const report = {
  date: new Date().toLocaleDateString('ko-KR'),
  protocol_version: "카멜레온 v3.0",
  daily_summary: {
    total_content: stats.today_content_count,
    anchor_content: "2회 예정",
    satellite_content: stats.today_content_count,
    referral_code: stats.referral_code
  },
  platform_breakdown: stats.platform_usage,
  performance: {
    target_daily: "20-30개 위성 콘텐츠",
    actual_daily: stats.today_content_count,
    status: stats.today_content_count >= 20 ? "✅ 목표 달성" : "⚠️ 목표 미달"
  },
  next_actions: [
    "앵커 콘텐츠 품질 최적화",
    "위성 콘텐츠 A/B 테스트",
    "플랫폼별 반응률 분석"
  ]
};

console.log("📊 카멜레온 프로토콜 일일 리포트:");
console.log(JSON.stringify(report, null, 2));

return [{ json: report }];
```

---

## 🚀 n8n 워크플로우 활성화 순서

### 1단계: 카멜레온 엔진 실행
```bash
cd C:\bithumb-campaign
python cameleon_protocol_v3.py
```

### 2단계: n8n 워크플로우 생성
1. **"카멜레온_앵커_콘텐츠"** 워크플로우 생성
2. **"카멜레온_위성_확산"** 워크플로우 생성  
3. **"카멜레온_일일_리포트"** 워크플로우 생성

### 3단계: 워크플로우 활성화
- 모든 워크플로우 **"Active"** 상태로 변경
- 실행 로그 모니터링

### 4단계: 실시간 모니터링
```bash
# 카멜레온 엔진 상태 확인
curl http://localhost:5000/health

# 통계 조회
curl http://localhost:5000/cameleon_stats
```

---

## 📊 성공 지표

### 앵커 콘텐츠 (주 2회)
- ✅ 1500자 이상 SEO 최적화된 글
- ✅ 추천코드 자연스럽게 포함
- ✅ 네이버 블로그 발행 완료

### 위성 콘텐츠 (시간당 10회)
- ✅ 플랫폼별 페르소나 완벽 적용
- ✅ 카멜레온 5가지 규칙 준수
- ✅ 자연스러운 추천코드 포함
- ✅ 커뮤니티별 문화 동화

### 전체 목표
- **일일**: 20-30개 위성 콘텐츠
- **주간**: 2-3개 앵커 콘텐츠 + 140-210개 위성 콘텐츠
- **월간**: 추천인 200-300명 증가
- **최종**: 1,000명 달성

이 설정으로 카멜레온 프로토콜 v3.0이 완벽하게 작동합니다! 🔥
