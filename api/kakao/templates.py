"""
카카오톡 챗봇 메시지 템플릿 관리 모듈
다양한 상황별 응답 메시지 템플릿 제공
"""

from typing import Dict, List, Any
from datetime import datetime

class KakaoMessageTemplates:
    """카카오톡 메시지 템플릿 클래스"""
    
    def __init__(self, referral_code: str = "W1HGATYGVW", referral_link: str = None):
        self.referral_code = referral_code
        self.referral_link = referral_link or f"https://m.bithumb.com/react/referral/guide?referral={referral_code}"
    
    def get_welcome_message(self) -> Dict[str, Any]:
        """환영 메시지 템플릿"""
        return {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": f"🎉 빗썸 친구초대 이벤트에 오신 것을 환영합니다!\n\n💰 최대 7만원 혜택\n📱 간편한 3단계 가입\n🎫 추천코드: {self.referral_code}\n\n시작하려면 \"메뉴\"를 입력해주세요!"
                    }
                }],
                "quickReplies": [
                    {"label": "📋 메뉴 보기", "action": "message", "messageText": "메뉴"},
                    {"label": "🎫 추천코드", "action": "message", "messageText": "추천코드"}
                ]
            }
        }
    
    def get_event_summary(self) -> Dict[str, Any]:
        """이벤트 요약 템플릿"""
        return {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": "📊 빗썸 친구초대 이벤트 요약\n\n💵 신규 가입자: 최대 7만원\n   • 기본 5만원 + 웰컴 미션 2만원\n\n👥 추천한 사람: 인당 3만원\n   • 최대 3,333명까지 추천 가능\n\n⏰ 조건: 가입 후 7일 내 완료\n📅 사용기한: 지급 후 30일 내\n\n자세한 내용을 원하시면 해당 메뉴를 선택해주세요!"
                    }
                }],
                "quickReplies": [
                    {"label": "📱 가입 방법", "action": "message", "messageText": "가입방법"},
                    {"label": "🎫 추천코드", "action": "message", "messageText": "추천코드"},
                    {"label": "❓ 주의사항", "action": "message", "messageText": "주의사항"}
                ]
            }
        }
    
    def get_step_by_step_guide(self) -> List[Dict[str, Any]]:
        """단계별 가입 안내 (여러 메시지로 분할)"""
        return [
            {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": "📱 빗썸 가입 1단계: 링크 접속\n\n🔗 아래 링크를 클릭하세요\n(추천코드가 자동으로 입력됩니다)\n\n" + self.referral_link + "\n\n✅ 링크를 클릭하면 자동으로 빗썸 앱이 열립니다.\n\n다음 단계를 보려면 \"2단계\"를 입력해주세요!"
                        }
                    }],
                    "quickReplies": [
                        {"label": "➡️ 2단계", "action": "message", "messageText": "2단계"},
                        {"label": "🎫 코드만 받기", "action": "message", "messageText": "추천코드"}
                    ]
                }
            },
            {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": f"📝 빗썸 가입 2단계: 회원가입\n\n1️⃣ \"회원가입\" 버튼 클릭\n2️⃣ 휴대폰 번호 입력 후 인증\n3️⃣ 추천코드 입력란에 입력:\n\n**{self.referral_code}**\n\n⚠️ 추천코드를 꼭 입력해야 혜택을 받을 수 있어요!\n\n다음 단계를 보려면 \"3단계\"를 입력해주세요!"
                        }
                    }],
                    "quickReplies": [
                        {"label": "➡️ 3단계", "action": "message", "messageText": "3단계"},
                        {"label": "🔄 1단계로", "action": "message", "messageText": "1단계"}
                    ]
                }
            },
            {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": "🆔 빗썸 가입 3단계: 본인인증 & 계좌연결\n\n📋 본인인증 (KYC):\n• 신분증 촬영\n• 얼굴 인증\n• 개인정보 입력\n\n🏦 계좌 연결:\n• KB국민은행 계좌만 가능\n• 계좌 소유자 = 가입자 동일해야 함\n\n✅ 모든 단계 완료 후 7일 내 조건 충족 시 최대 7만원 지급!\n\n궁금한 점이 있으시면 언제든 물어보세요!"
                        }
                    }],
                    "quickReplies": [
                        {"label": "❓ 자주 묻는 질문", "action": "message", "messageText": "FAQ"},
                        {"label": "🔄 처음부터", "action": "message", "messageText": "시작"}
                    ]
                }
            }
        ]
    
    def get_quick_referral(self) -> Dict[str, Any]:
        """빠른 추천코드 제공 템플릿"""
        return {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": f"⚡ 빠른 추천코드 안내\n\n🎫 **{self.referral_code}**\n\n📱 빠른 가입 링크:\n{self.referral_link}\n\n💡 위 링크 클릭 → 즉시 가입 가능\n💰 최대 7만원 혜택 받기\n\n더 자세한 안내가 필요하시면 \"가입방법\"을 입력해주세요!"
                    }
                }],
                "quickReplies": [
                    {"label": "📱 가입 방법", "action": "message", "messageText": "가입방법"},
                    {"label": "❓ 주의사항", "action": "message", "messageText": "주의사항"}
                ]
            }
        }
    
    def get_warning_notices(self) -> Dict[str, Any]:
        """주의사항 템플릿"""
        return {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": "⚠️ 꼭 알아야 할 주의사항\n\n🚫 제외 대상:\n• 기존 빗썸 회원 (탈퇴 후 재가입 포함)\n• 만 14세 미만\n\n⏰ 시간 제한:\n• 가입 후 7일 내 모든 조건 완료\n• 리워드 지급 후 30일 내 사용\n\n🏦 필수 조건:\n• KB국민은행 계좌 연결 필수\n• 본인명의 계좌만 가능\n\n💡 팁: 가입 후 바로 인증과 계좌연결을 완료하세요!"
                    }
                }],
                "quickReplies": [
                    {"label": "📱 지금 가입하기", "action": "message", "messageText": "가입방법"},
                    {"label": "❓ 더 궁금한 점", "action": "message", "messageText": "FAQ"}
                ]
            }
        }
    
    def get_faq_detailed(self) -> List[Dict[str, Any]]:
        """상세 FAQ (여러 메시지로 분할)"""
        return [
            {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": "❓ 자주 묻는 질문 1/3\n\nQ1. 재가입도 이벤트 대상인가요?\nA1. ❌ 생애 첫 가입자만 해당됩니다. 탈퇴 후 재가입도 제외입니다.\n\nQ2. 추천코드를 나중에 입력해도 되나요?\nA2. ❌ 회원가입 시에만 입력 가능합니다. 가입 후 추가 입력은 불가능해요.\n\nQ3. 다른 은행 계좌도 연결 가능한가요?\nA3. ❌ KB국민은행 계좌만 연결 가능합니다."
                        }
                    }],
                    "quickReplies": [
                        {"label": "➡️ FAQ 2/3", "action": "message", "messageText": "FAQ2"},
                        {"label": "🎫 추천코드", "action": "message", "messageText": "추천코드"}
                    ]
                }
            },
            {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": "❓ 자주 묻는 질문 2/3\n\nQ4. 7일 내 조건을 못 채우면 어떻게 되나요?\nA4. ❌ 혜택을 받을 수 없습니다. 가입 후 즉시 진행하세요!\n\nQ5. 리워드는 언제까지 사용해야 하나요?\nA5. ⏰ 지급 후 30일 내 사용하지 않으면 자동 소멸됩니다.\n\nQ6. KYC 인증이 뭔가요?\nA6. 📷 신분증 촬영과 얼굴 인증을 통한 본인확인 절차입니다."
                        }
                    }],
                    "quickReplies": [
                        {"label": "➡️ FAQ 3/3", "action": "message", "messageText": "FAQ3"},
                        {"label": "⬅️ FAQ 1/3", "action": "message", "messageText": "FAQ"}
                    ]
                }
            },
            {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": f"❓ 자주 묻는 질문 3/3\n\nQ7. 추천코드를 까먹었어요!\nA7. 📝 {self.referral_code} 입니다. 언제든 물어보세요!\n\nQ8. 가입 링크가 안 열려요.\nA8. 📱 빗썸 앱을 먼저 설치한 후 링크를 클릭해보세요.\n\nQ9. 혜택은 언제 받을 수 있나요?\nA9. ✅ 모든 조건 완료 후 7일 이내 지급됩니다.\n\n추가 문의사항이 있으시면 언제든 말씀해주세요!"
                        }
                    }],
                    "quickReplies": [
                        {"label": "📱 가입하기", "action": "message", "messageText": "가입방법"},
                        {"label": "🔄 처음부터", "action": "message", "messageText": "시작"}
                    ]
                }
            }
        ]
    
    def get_success_message(self) -> Dict[str, Any]:
        """가입 완료 축하 메시지"""
        return {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": "🎉 빗썸 가입을 완료하셨군요! 축하드립니다!\n\n✅ 이제 남은 단계:\n1. KYC 본인인증 완료\n2. KB국민은행 계좌 연결\n3. 웰컴 미션 수행 (선택사항)\n\n💰 모든 조건 완료 시 최대 7만원 지급!\n⏰ 가입 후 7일 내 완료하세요.\n\n주변 친구들에게도 추천해보세요! 🚀"
                    }
                }],
                "quickReplies": [
                    {"label": "📋 체크리스트", "action": "message", "messageText": "체크리스트"},
                    {"label": "❓ 궁금한 점", "action": "message", "messageText": "FAQ"}
                ]
            }
        }
    
    def get_checklist(self) -> Dict[str, Any]:
        """가입 후 체크리스트"""
        return {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": "📋 빗썸 가입 후 체크리스트\n\n✅ 회원가입 완료\n✅ 추천코드 입력 완료\n\n⏳ 남은 할 일:\n□ KYC 본인인증\n   • 신분증 촬영\n   • 얼굴 인증\n\n□ KB국민은행 계좌 연결\n   • 본인명의 계좌만 가능\n\n□ 웰컴 미션 (선택, +2만원)\n\n💡 모든 항목을 7일 내 완료하세요!\n⏰ 완료 후 7일 내 혜택 지급됩니다."
                    }
                }],
                "quickReplies": [
                    {"label": "❓ 인증 방법", "action": "message", "messageText": "인증방법"},
                    {"label": "🏦 계좌연결", "action": "message", "messageText": "계좌연결"}
                ]
            }
        }