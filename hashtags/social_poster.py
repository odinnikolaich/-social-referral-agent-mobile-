# social_poster.py
import json
import random
from datetime import datetime

def load_templates(platform):
    try:
        with open(f"content_templates/{platform}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"title": f"Шаблон {platform} не найден", "script": "Тестовый пост"}]

def post_to_platform(platform):
    templates = load_templates(platform)
    post = random.choice(templates)
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] 📲 Публикация в {platform.upper()}:")
    print(f"  • Заголовок: {post.get('title', '—')}")
    print(f"  • Текст: {post.get('script', post.get('body', '—'))}")
    print(f"  • CTA: {post.get('call_to_action', post.get('ending', '—'))}")
    print("  ✅ Готово\n")

def main():
    for platform in ["youtube_shorts", "tiktok", "instagram_reels"]:
        post_to_platform(platform)

if __name__ == "__main__":
    main()
