import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import BOT_TOKEN, WEBHOOK_URL
from handlers.menu import start_command, handle_stones_callback

# Получаем логгер из config.py
logger = logging.getLogger(__name__)

def main() -> None:
    """Запуск бота и диспетчера."""
    
    # 1. Проверяем наличие токена
    if not BOT_TOKEN:
        logger.error("Запуск невозможен: BOT_TOKEN не найден.")
        return

    # 2. Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # 3. Регистрируем обработчики (Handlers)
    
    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start_command))
    
    # Обработчик колбэков, связанных с главным меню
    # Мы используем CALLBACK_DATA_STONES из config, чтобы фильтровать колбэки
    application.add_handler(CallbackQueryHandler(handle_stones_callback, pattern='^stones_menu$'))
    
    # 4. Запуск бота (Webhooks или Polling)
    
    if WEBHOOK_URL:
        # --- Режим Webhook (для Render Web Service) ---
        
        # Получаем номер порта из переменных окружения (Render требует)
        PORT = int(os.environ.get('PORT', 8000))

        # Устанавливаем Webhook
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path='/',  # Путь, по которому принимает Telegram (должен совпадать с тем, что вы дали BotFather)
            webhook_url=f"{WEBHOOK_URL}/" 
            # WEBHOOK_URL - это ваш домен https://sheon-telegram-bot.onrender.com
        )
        logger.info(f"Бот запущен в режиме Webhook на порту {PORT}")

    #else:
        # --- Режим Long Polling (для Render Background Worker) ---
        
        #logger.info("Бот запущен в режиме Long Polling.")
        #application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':

    main()

