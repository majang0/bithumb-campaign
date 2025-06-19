import json
import datetime
import random
from pathlib import Path

class ContentScheduler:
    """플랫폼별 콘텐츠 발행 스케줄러"""
    
    def __init__(self):
        self.platforms = {
            "naver_blog": {
                "times": ["09:00", "14:00", "19:00"],
                "daily_limit": 3,
                "priority": 1
            },
            "youtube": {
                "times": ["10:00", "15:00", "20:00"],
                "daily_limit": 3,
                "priority": 1
            },
            "communities": {
                "dcinside": {"weekly_limit": 3, "best_times": ["12:00-14:00", "19:00-21:00"]},
                "clien": {"weekly_limit": 2, "best_times": ["10:00-12:00", "20:00-22:00"]},
                "ppomppu": {"weekly_limit": 3, "best_times": ["11:00-13:00", "18:00-20:00"]},
                "theqoo": {"weekly_limit": 2, "best_times": ["14:00-16:00", "21:00-23:00"]}
            },
            "sns": {
                "instagram": {"daily_limit": 2, "times": ["12:00", "18:00"]},
                "facebook": {"daily_limit": 1, "times": ["19:00"]}
            }
        }
        
    def generate_weekly_schedule(self):
        """주간 포스팅 스케줄 생성"""
        schedule = {}
        start_date = datetime.datetime.now()
        
        for day in range(7):
            date = start_date + datetime.timedelta(days=day)
            date_str = date.strftime("%Y-%m-%d")
            schedule[date_str] = {
                "naver_blog": self._get_daily_posts("naver_blog"),
                "youtube": self._get_daily_posts("youtube"),
                "communities": self._get_community_posts(date.weekday()),
                "sns": self._get_sns_posts()
            }
            
        return schedule
    
    def _get_daily_posts(self, platform):
        """일일 포스팅 시간 결정"""
        config = self.platforms[platform]
        times = random.sample(config["times"], 
                            min(len(config["times"]), config["daily_limit"]))
        return sorted(times)
    
    def _get_community_posts(self, weekday):
        """커뮤니티 포스팅 일정"""
        posts = {}
        for community, config in self.platforms["communities"].items():
            # 주중/주말 구분
            if weekday < 5:  # 평일
                if random.random() < config["weekly_limit"] / 5:
                    time_range = random.choice(config["best_times"])
                    posts[community] = self._random_time_in_range(time_range)
            else:  # 주말
                if random.random() < 0.3:  # 주말은 확률 낮춤
                    time_range = random.choice(config["best_times"])
                    posts[community] = self._random_time_in_range(time_range)
        return posts
    
    def _get_sns_posts(self):
        """SNS 포스팅 일정"""
        posts = {}
        for sns, config in self.platforms["sns"].items():
            times = random.sample(config["times"], 
                                min(len(config["times"]), config["daily_limit"]))
            posts[sns] = sorted(times)
        return posts
    
    def _random_time_in_range(self, time_range):
        """시간 범위 내 랜덤 시간 생성"""
        start, end = time_range.split("-")
        start_hour = int(start.split(":")[0])
        end_hour = int(end.split(":")[0])
        hour = random.randint(start_hour, end_hour-1)
        minute = random.randint(0, 59)
        return f"{hour:02d}:{minute:02d}"
    
    def save_schedule(self, filename="weekly_schedule.json"):
        """스케줄 저장"""
        schedule = self.generate_weekly_schedule()
        filepath = Path("C:/bithumb-campaign/schedules") / filename
        filepath.parent.mkdir(exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, ensure_ascii=False, indent=2)
        
        return filepath

if __name__ == "__main__":
    scheduler = ContentScheduler()
    filepath = scheduler.save_schedule()
    print(f"주간 스케줄 생성 완료: {filepath}")