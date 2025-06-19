# Google Drive MCP 서버 확인 스크립트
import subprocess
import json

def check_mcp_packages():
    """사용 가능한 MCP 패키지 확인"""
    
    print("MCP 관련 패키지 검색 중...")
    
    # npm search 명령 실행
    searches = [
        "@modelcontextprotocol/server",
        "mcp-server",
        "google-drive mcp"
    ]
    
    for search_term in searches:
        print(f"\n검색: {search_term}")
        try:
            result = subprocess.run(
                ["npm", "search", search_term, "--json"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                packages = json.loads(result.stdout)
                for pkg in packages[:5]:  # 상위 5개만
                    print(f"- {pkg.get('name', 'N/A')}: {pkg.get('description', 'N/A')[:50]}...")
        except Exception as e:
            print(f"  오류: {e}")

if __name__ == "__main__":
    check_mcp_packages()
