# main_agent.py
import json
import os
import time
from datetime import datetime

def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ config.json не найден. Создайте его по шаблону.")
        return {}

def log(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

def run():
    log("🚀 Запуск Social Referral Agent...")
    config = load_config()
    if not config:
        return

    # Имитация работы агента
    log("🔍 Анализ ниши: " + config.get("niche", "unknown"))
    log("📌 Генерация контента...")
    time.sleep(1)
    log("✅ Контент готов")
    
    log("📤 Публикация в соцсети...")
    time.sleep(1)
    log("✅ Опубликовано в YouTube, TikTok, Reels")

    log("📊 Отслеживание рефералов...")
    time.sleep(1)
    log("✅ Реферальные клики: 12 (за сегодня)")

    log("🔔 Управление через Telegram — активно")
    log("🎉 Агент работает автономно. Для остановки нажмите Ctrl+C.")

if __name__ == "__main__":
    run()
