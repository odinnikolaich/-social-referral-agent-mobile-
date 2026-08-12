# referral_tracker.py
import json
import os
from datetime import datetime

TRACKING_FILE = "referrals.json"

def load_tracking():
    if os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"total_clicks": 0, "today": 0, "last_update": ""}

def save_tracking(data):
    data["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TRACKING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def track_click():
    data = load_tracking()
    data["total_clicks"] += 1
    today = datetime.now().strftime("%Y-%m-%d")
    if data.get("date_today") == today:
        data["today"] += 1
    else:
        data["date_today"] = today
        data["today"] = 1
    save_tracking(data)
    return data

def show_stats():
    data = load_tracking()
    print(f"\n📊 Статистика рефералов:")
    print(f"  • Всего кликов: {data['total_clicks']}")
    print(f"  • Сегодня: {data['today']}")
    print(f"  • Последнее обновление: {data['last_update']}")

if __name__ == "__main__":
    print("🔍 Отслеживание реферальных кликов...")
    track_click()
    show_stats()
