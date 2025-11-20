import os
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Импортируем наши новые модули
from handlers.menu import (
    start, 
    handle_menu_back, 
    handle_stones_menu,
    handle_advice, 
    handle_schedule,
    handle_delivery,
    handle_contact,
    handle_care_memo,
    handle_care_memo_part1,
    handle_care_memo_part2
)
from handlers.stones import handle_stone

# --- КОНФИГУРАЦИЯ ДЛЯ WEBHOOK ---
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

def main():
    """ВЕРСИЯ ДЛЯ ПРОДАКШЕНА С WEBHOOK"""
    application = Application.builder().token(TOKEN).build()

    # Регистрируем ВСЕ обработчики (ТОЧНО ТАК ЖЕ КАК В ТЕСТОВОМ)
    application.add_handler(CallbackQueryHandler(handle_care_memo_part1, pattern='care_memo_part1'))
    application.add_handler(CallbackQueryHandler(handle_care_memo_part2, pattern='care_memo_part2'))
    application.add_handler(CallbackQueryHandler(handle_care_memo, pattern='care_memo'))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_menu_back, pattern='menu_back'))
    application.add_handler(CallbackQueryHandler(handle_stones_menu, pattern='stones_menu'))
    application.add_handler(CallbackQueryHandler(handle_stone, pattern='^stone_'))
    application.add_handler(CallbackQueryHandler(handle_advice, pattern='advice'))
    application.add_handler(CallbackQueryHandler(handle_schedule, pattern='schedule'))
    application.add_handler(CallbackQueryHandler(handle_delivery, pattern='delivery'))
    application.add_handler(CallbackQueryHandler(handle_contact, pattern='contact'))

    # ЗАПУСК В РЕЖИМЕ WEBHOOK (КАК В СТАРОМ КОДЕ)
    logger.info(f"Starting webhook on port {PORT} at path {WEBHOOK_PATH}")
    logger.info(f"Full Webhook URL: {WEBHOOK_URL}{WEBHOOK_PATH}")

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=WEBHOOK_PATH,
        webhook_url=f"{WEBHOOK_URL}{WEBHOOK_PATH}", 
    )

if __name__ == '__main__':
    main()