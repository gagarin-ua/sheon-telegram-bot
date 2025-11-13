import os
import telebot
import telrgram
from flask import Flask, request, abort
import logging

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Получение токена бота из переменных окружения
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Получение URL вебхука из переменных окружения (для развертывания на Render)
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

# Проверка наличия токена
if not BOT_TOKEN:
    logging.error("Переменная окружения BOT_TOKEN не установлена.")
    # Для целей этого примера, если токен отсутствует, мы не сможем запустить бота
    # В реальном приложении это приведет к остановке
    exit()

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# ===============================================
# Обработчики команд и сообщений бота
# ===============================================

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Обработчик команды /start
    """
    user_name = message.from_user.first_name or "Пользователь"
    bot.reply_to(message, f"Привет, {user_name}! Я бот, работающий через вебхук. Используйте команду /help для получения дополнительной информации.")
    logging.info(f"Получена команда /start от {message.chat.id}")

@bot.message_handler(commands=['help'])
def send_help(message):
    """
    Обработчик команды /help
    """
    help_text = "Доступные команды:\n"
    help_text += "/start - Начать взаимодействие\n"
    help_text += "/help - Показать это сообщение\n"
    help_text += "Любое другое сообщение будет повторено."
    bot.reply_to(message, help_text)
    logging.info(f"Получена команда /help от {message.chat.id}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """
    Обработчик для всех остальных текстовых сообщений
    """
    bot.reply_to(message, f"Вы сказали: {message.text}")
    logging.info(f"Повтор сообщения: '{message.text}' для {message.chat.id}")

# ===============================================
# Настройка Flask и вебхука
# ===============================================

# Инициализация Flask-приложения
app = Flask(__name__)

# Секретный токен для проверки подлинности вебхука
# В реальном приложении лучше генерировать уникальный SECRET_TOKEN
SECRET_TOKEN = BOT_TOKEN 

@app.route('/' + SECRET_TOKEN, methods=['POST'])
def webhook():
    """
    Точка входа для вебхука Telegram
    """
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'ok', 200
    else:
        # Неверный Content-Type
        abort(403)

# ===============================================
# Запуск приложения
# ===============================================

if WEBHOOK_URL:
    # Режим работы с вебхуком (для Render или других платформ)
    # Установка вебхука при запуске
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + SECRET_TOKEN)
    
    # Render обычно предоставляет порт через переменную окружения PORT
    PORT = os.environ.get('PORT', 5000)
    logging.info(f"Запуск в режиме Webhook на порту {PORT}")
    
    # Запуск Flask-приложения
    # host='0.0.0.0' необходим для прослушивания всех внешних интерфейсов
    app.run(host='0.0.0.0', port=PORT)

else:
    # Режим работы с Polling (для локального тестирования)
    logging.warning("Переменная окружения WEBHOOK_URL не установлена. Запуск в режиме Polling (подходит только для локального тестирования).")
    try:
        bot.remove_webhook()
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Ошибка при запуске в режиме Polling: {e}")

