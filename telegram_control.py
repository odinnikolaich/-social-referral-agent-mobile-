# telegram_control.py
import json
import time

def handle_command(cmd):
    cmd = cmd.strip().lower()
    if cmd == "/start":
        return "🤖 Привет! Я Social Referral Agent.\nДоступные команды:\n /post — опубликовать контент\n /stats — статистика\n /help — помощь"
    elif cmd == "/post":
        return "📤 Запуск публикации...\n✅ YouTube, TikTok, Reels — готовы!"
    elif cmd == "/stats":
        return "📊 Статистика:\n• Рефералы сегодня: 12\n• Публикаций: 3\n• Агент работает: 1h 24m"
    elif cmd == "/help":
        return "ℹ️ Инструкция:\n— Установите Termux\n— Клонируйте репозиторий\n— pip install -r requirements.txt\n— Запустите: python3 main_agent.py"
    else:
        return "❌ Неизвестная команда. Напишите /help"

def simulate_telegram_loop():
    print("📡 Telegram-бот запущен (имитация)...")
    print("Напишите команду (например: /post), или 'exit' для выхода:")
    while True:
        cmd = input("> ").strip()
        if cmd == "exit":
            print("👋 Бот остановлен.")
            break
        response = handle_command(cmd)
        print("🤖:", response)
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_telegram_loop()
