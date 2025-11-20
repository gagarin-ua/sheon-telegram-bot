import os
import logging

# --- КОНФИГУРАЦИЯ ---
TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.environ.get("PORT", "8000"))
WEBHOOK_URL = "https://sheon-telegram-bot.onrender.com"
WEBHOOK_PATH = f"/webhook/{TOKEN}"

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)