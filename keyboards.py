import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# --- ГЛАВНОЕ МЕНЮ ---
def get_main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📜 ІСТОРІЯ КАМІННЯ", callback_data='stones_menu')],
        [InlineKeyboardButton("💡 Порада від нас", callback_data='advice')],
        [InlineKeyboardButton("⏱️ Графік роботи", callback_data='schedule')],
        [InlineKeyboardButton("📦 Доставка й оплата", callback_data='delivery')],
        [InlineKeyboardButton("📝 Пам'ятка по догляду", callback_data='care_memo')],
        [InlineKeyboardButton("💬 Зв'язок з майстром", callback_data='contact')]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- МЕНЮ КАМНЕЙ ---
def get_stones_menu_keyboard():
    stones_keyboard = [
        [InlineKeyboardButton("💧 Аквамарин", callback_data='stone_aquamarine')],
        [InlineKeyboardButton("💜 Аметист", callback_data='stone_amethist')],
        [InlineKeyboardButton("🟦 Бірюза", callback_data='stone_turquoise')],
        [InlineKeyboardButton("🧡 Гранат", callback_data='stone_garnet')],
        [InlineKeyboardButton("✨ Лабрадорит", callback_data='stone_labradorite')],
        [InlineKeyboardButton("⚫ Онікс", callback_data='stone_onyx')],
        [InlineKeyboardButton("⚪ Перли", callback_data='stone_pearls')],
        [InlineKeyboardButton("💗 Рожевий кварц", callback_data='stone_rose_quartz')],
        [InlineKeyboardButton("💚 Смарагд", callback_data='stone_emerald')],
        [InlineKeyboardButton("💙 Топаз", callback_data='stone_topaz')],
        [InlineKeyboardButton("🔴 Турмалін", callback_data='stone_tourmaline')],
        [InlineKeyboardButton("💛 Цитрин", callback_data='stone_citrine')],
        [InlineKeyboardButton("⬅️ Повернутися до Меню", callback_data='menu_back')]
    ]
    return InlineKeyboardMarkup(stones_keyboard)

# --- ДРУГИЕ КЛАВИАТУРЫ ---
def get_back_button(target_menu='stones_menu'):
    """Универсальная кнопка назад"""
    if target_menu == 'stones_menu':
        text = "⬅️ Назад до Списку Каміння"
    else:
        text = "⬅️ Повернутися до Меню"
        
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, callback_data=target_menu)]])