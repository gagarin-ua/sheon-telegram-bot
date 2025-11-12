from telegram import Update
from telegram.ext import ContextTypes
from keyboards import get_main_menu_keyboard
from config import WELCOME_TEXT, CATALOG_URL, CALLBACK_DATA_STONES

# --- 1. Обработчик команды /start ---

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет приветственное сообщение с главной клавиатурой."""
    
    # 1. Получаем клавиатуру
    reply_markup = get_main_menu_keyboard(CATALOG_URL)
    
    # 2. Отправляем сообщение
    await update.message.reply_text(
        text=WELCOME_TEXT,
        reply_markup=reply_markup,
        parse_mode='Markdown' # Убедитесь, что Telegram правильно обрабатывает разметку
    )

# --- 2. Обработчик колбэка для кнопки "ІСТОРІЯ КАМІННЯ" ---

async def handle_stones_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает нажатие на кнопку "ІСТОРІЯ КАМІННЯ"."""
    
    query = update.callback_query
    
    # Обязательно отвечаем на callback_query, чтобы убрать часы загрузки
    await query.answer() 
    
    # Отправляем сообщение
    await query.edit_message_text(
        text="Тут будет информация об истории камней и их свойствах. \\n\\n"
             "Пожалуйста, выберите интересующий вас камень из списка...",
        # Здесь вы можете добавить новую клавиатуру с выбором камней
        # reply_markup=get_stones_selection_keyboard() 
    )

# Обратите внимание: handlers/stones.py пока не нужен, так как вся логика с камнями 
# сейчас сводится к одному колбэку, который мы добавили здесь для простоты.
# Если логика камней станет сложнее, вы просто перенесете ее в stones.py.