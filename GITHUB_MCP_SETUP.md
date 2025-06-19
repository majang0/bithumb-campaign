# GitHub MCP 설정 가이드

## 1. GitHub Personal Access Token 생성

1. GitHub 로그인 후 Settings > Developer settings > Personal access tokens > Tokens (classic) 로 이동
2. "Generate new token" 클릭
3. 다음 권한 선택:
   - `repo` (전체 선택)
   - `workflow` 
   - `read:org` (조직 사용 시)
4. Token 생성 후 안전한 곳에 복사

## 2. MCP 설정 파일 업데이트

`mcp_full_config.json` 파일에서 GitHub 섹션의 `YOUR_GITHUB_PAT_HERE`를 실제 토큰으로 교체:

```json
"github": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-github"
  ],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_실제토큰값"
  }
}
```

## 3. Claude Desktop 설정

1. Claude Desktop 설정에서 MCP 섹션 찾기
2. 아래 내용을 추가:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_실제토큰값"
      }
    }
  }
}
```

## 4. GitHub 저장소 생성 및 연결

### 로컬에서 Git 초기화:
```bash
cd C:\bithumb-campaign
git init
git add .
git commit -m "Initial commit: 빗썸 캠페인 자동화 시스템"
```

### GitHub에 저장소 생성 후:
```bash
git remote add origin https://github.com/your-username/bithumb-campaign.git
git branch -M main
git push -u origin main
```

## 5. GitHub Actions 워크플로우 (선택사항)

자동 백업이나 CI/CD를 위한 워크플로우는 `.github/workflows/` 폴더에 추가할 수 있습니다.

## 주의사항

- GitHub PAT는 절대 공개 저장소에 커밋하지 마세요
- `.gitignore`에 민감한 파일들이 포함되어 있는지 확인하세요
- 정기적으로 토큰을 갱신하세요
