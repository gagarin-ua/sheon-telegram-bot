from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import CALLBACK_DATA_CATALOG, CALLBACK_DATA_STONES

# --- Инлайн-клавиатура для главного меню ---

def get_main_menu_keyboard(catalog_url: str) -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру для приветственного сообщения."""
    
    # 1. Первая строка: кнопка с внешней ссылкой (Каталог)
    catalog_button = InlineKeyboardButton(
        text="Каталог і ціни",
        url=catalog_url
    )
    
    # 2. Вторая строка: кнопка с колбэком (История камней)
    stones_button = InlineKeyboardButton(
        text="ІСТОРІЯ КАМІННЯ",
        callback_data=CALLBACK_DATA_STONES
    )
    
    # 3. Собираем клавиатуру
    keyboard = [
        [catalog_button],  # Первая строка
        [stones_button]    # Вторая строка
    ]
    
    return InlineKeyboardMarkup(keyboard)