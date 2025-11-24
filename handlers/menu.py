from telegram.error import BadRequest
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from keyboards import get_main_menu_keyboard, get_stones_menu_keyboard, get_back_button
async def safe_edit_message(query, text, reply_markup, parse_mode='Markdown'):
    try:
        await query.edit_message_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )
    except BadRequest:
        pass
        
# --- ТЕКСТИ В ОДНОМУ МОДУЛІ ---
WELCOME_TEXT = (
    "ВІТАЄМО\n\n"
    "Ласкаво просимо у світ автентичної біжутерії з натурального каміння SHEON!✨\n\n"
    "Наші вироби створені для жінок, які цінують унікальність та витонченість.\n\n"
    "Це не просто аксесуари – це деталі, що підкреслюють ваш стиль і особистість, залишаючи легкий акцент на вашій впевненості.\n\n"
    
    "Будьте певні: кожна прикраса існує в єдиному екземплярі і створена саме для вас.\n⭐ Ми можемо відтворити настрій, палітру та матеріали попереднього виробу, але точний повтор неможливий. Кожне замовлення - унікальна композиція.\n⭐ SHEON не гарантує відсутності схожих виробів третіх осіб і не несе відповідальності за дії/продукцію інших виробників."
)

STONES_INTRO_TEXT = (
    "💎 ОБЕРІТЬ СВІЙ КАМІНЬ\n\n"
    "Кожне каміння має власну історію, характер та неповторну красу.\n\n"
    
    "Ми підбираємо тільки натуральне каміння, щоб кожен виріб був унікальним і створював особливий акцент у вашому стилі.\n\n"
    
    "Зверніть увагу: і надаються виключно в ознайомчих цілях. Ми не гарантуємо певних ефектів або результатів при використанні каміння.\n\n"
    
    "Наведені властивості каменів відображають 'наш погляд та досвід' і допомагають краще розкрити їхню красу та особливості.\n\n"
    
    "Це радше рекомендації, ніж обов'язкові правила.\n\n"
    
    "Оберіть камінь, щоб прочитати його історію:"
)
ADVICE_TEXT = (
    "💡 **ПОРАДА ВІД НАС**\n\n"
    "Носіть каміння так, щоб воно підкреслювало ваш характер, а не тільки колір або тренд.\n\n"
    "Кожен виріб існує **в єдиному екземплярі**, тому це не просто прикраса, а маленька деталь вашої індивідуальності."
)

SCHEDULE_TEXT = (
    "⏱️ **ГРАФІК РОБОТИ**\n\n"
    "Відповідаємо на ваші звернення щодня **з 10:00 до 20:00** в порядку черги."
)

DELIVERY_TEXT = (
    "📦 **ДОСТАВКА Й ОПЛАТА**\n\n"
    "Доставка здійснюється у відділення Нової пошти за 'попередньою 100% оплатою'."
)

CONTACT_TEXT = (
    "💬 **ЗВ'ЯЗОК З МАЙСТРОМ**\n\n"
    "Щодня **з 10:00 до 20:00**\n"
    "Щоб зробити замовлення, уточнити деталі або поставити запитання, напишіть нам:\n\n"
    "✨ *Майстер відповідить протягом кількох годин.*\n\n"
    "✨ *Або напишіть нам у соцмережах за допомогою кнопок нижче.*"
)

CARE_MEMO_INTRO_TEXT = (
    "📝 **ПАМ'ЯТКА ПО ДОГЛЯДУ**\n\n"
    "Оберіть розділ, про який ви хочете дізнатися детальніше:"
)

CARE_MEMO_PART1_TEXT = (
    "1 ПОВСЯКДЕННЕ КОРИСТУВАННЯ\n\n"
    
    "Повсякденне користування\n"
    "Правило останнього штриха: косметика/парфум → потім прикраси.\n\n"
    
    "Знімати перед:\n"
    "- Спортом, сном, душем/ванною, басейном/морем, сауною/солярієм.\n"
    "- Прибиранням і роботою з хімією.\n"
    
    "Після використання протирайте м'якою сухою мікрофіброю.\n\n"
    
    "Фурнітура класу люкс.\n"
    "Ми використовуємо якісну фурнітуру (Позолота 18K/PVD, преміум‑сталь 304/316L).\n"
    "Вона не любить тривалий прямий контакт із водою, потом, парфумами, хлором і солоною водою. Перед тренуванням і водними процедурами — знімайте. Після вологи — відразу витріть насухо."
)

CARE_MEMO_PART2_TEXT = (
    "2. ЗБЕРІГАННЯ ТА ДОГЛЯД\n\n"
    
    "Зберігання\n"
    "Зберігайте прикраси окремо:\n"
    "- У м'яких мішечках або скриньках із перегородками, щоб уникнути подряпин.\n"
    "- Уникайте прямого сонця, надмірної вологості або пересушеного повітря.\n\n"
    
    "Догляд за камінням:\n"
    "- Кварц, агат, онікс, яшма, авантюрин: тепла вода + крапля нейтрального мила, коротко, без замочувань - ополоснути - насухо.\n"
    "- Місячний камінь, лабрадорит: швидке ополіскування, без перепадів температур.\n"
    "- Малахіт, бірюза, лазурит, корал, опал, перли: лише злегка волога м'яка серветка, без хімії - швидко висушити.\n"
    "- Позолота: тільки суха мікрофібра (без паст і полірувань).\n"
    "- Сталь 304/316L: протерти насухо після води.\n\n"
    
    "Наші прикраси не люблять:\n"
    "Спирт, ацетон, оцет, аміак, хлор, абразиви, ультразвук та пар, різкі удари, різкі перепади температур."
)
# --- ОБРОБНИКИ МЕНЮ ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник команди /start з підтримкою deep linking"""
    if context.args and context.args[0] == "care":
        return await handle_care_memo(update, context)  # ← ИСПОЛЬЗУЕМ СУЩЕСТВУЮЩИЙ
    
    await update.message.reply_text(
        WELCOME_TEXT, 
        reply_markup=get_main_menu_keyboard(), 
        parse_mode='Markdown'
    )

#async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    """Обробник команди /start"""
#    """Обробник команди /start з підтримкою deep linking"""
#    if context.args and context.args[0] == "care":
#        # Відкриваємо розділ "Пам'ятка по догляду" напряму
#        from handlers.menu import get_care_guide_keyboard
#        keyboard = get_care_guide_keyboard()
#        await update.message.reply_text(
#            "📖 *ПАМ'ЯТКА ПО ДОГЛЯДУ*\\n\\nОберіть розділ:",
#            reply_markup=keyboard,
#            parse_mode='Markdown'
#        )
#        return
#    await update.message.reply_text(
#        WELCOME_TEXT, 
#        reply_markup=get_main_menu_keyboard(), 
#        parse_mode='Markdown'
#    )

async def handle_menu_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Повернення в головне меню"""
    query = update.callback_query
    await query.answer()
    await safe_edit_message(
        query=query,
        text=WELCOME_TEXT,
        reply_markup=get_main_menu_keyboard()
    )

async def handle_stones_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Меню каменів"""
    query = update.callback_query
    await query.answer()
    await safe_edit_message(
        query=query,
        text=STONES_INTRO_TEXT,
        reply_markup=get_stones_menu_keyboard()
    )
async def handle_advice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Порада від нас"""
    query = update.callback_query
    await query.answer()
    await safe_edit_message(
        query=query,
        text=ADVICE_TEXT,
        reply_markup=get_back_button('menu_back'),
    )

async def handle_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Графік роботи"""
    query = update.callback_query
    await query.answer()
    await safe_edit_message(
        query=query,
        text=SCHEDULE_TEXT,
        reply_markup=get_back_button('menu_back')
    )

async def handle_delivery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Доставка й оплата"""
    query = update.callback_query
    await query.answer()
    await safe_edit_message(
        query=query,
        text=DELIVERY_TEXT,
        reply_markup=get_back_button('menu_back')
    )

async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Зв'язок з майстром"""
    query = update.callback_query
    await query.answer()
    
    contact_keyboard = [
        [InlineKeyboardButton("📷 Instagram Майстра", url="https://instagram.com/sheon_jewelry")],
        [InlineKeyboardButton("⬅️ Повернутися до Меню", callback_data='menu_back')]
    ]
    
    await safe_edit_message(
        query=query,
        text=CONTACT_TEXT,
        reply_markup=InlineKeyboardMarkup(contact_keyboard)
    )
#async def handle_care_memo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#3    """Пам'ятка по догляду - ДИАГНОСТИКА"""
#    query = update.callback_query
#    print("🟢 ДИАГНОСТИКА: handle_care_memo ВЫЗВАНА!")
#    print(f"🔴 callback_data: {query.data}")
#    print(f"🔴 Message ID: {query.message.message_id}")
#    print(f"🔴 Chat ID: {query.message.chat_id}")
    
 #   await query.answer("Обрабатываю запрос...")
    
    # СУПЕР-ПРОСТАЯ клавиатура
 #   care_memo_keyboard = [
 #       [InlineKeyboardButton("ТЕСТ 1", callback_data='care_memo_part1')],
 #       [InlineKeyboardButton("ТЕСТ 2", callback_data='care_memo_part2')],
 #   ]
    
    # СУПЕР-ПРОСТОЙ текст
 #   simple_text = "ТЕСТ"
    
 #   try:
 #       print("🟡 Пытаемся отправить САМОЕ ПРОСТОЕ сообщение...")
 #       result = await query.edit_message_text(
 #           text=simple_text,
 #           reply_markup=InlineKeyboardMarkup(care_memo_keyboard)
            # НИКАКОГО parse_mode!
 #       )
 #       print("✅ УСПЕХ: Сообщение отредактировано!")
 #       return result
 #   except Exception as e:
 #       print(f"🔴 ОШИБКА: {e}")
 #       print(f"🔴 Тип ошибки: {type(e)}")
        # Попробуем отправить новое сообщение вместо редактирования
 #       try:
 #           print("🟡 Пробуем отправить НОВОЕ сообщение...")
 #           await query.message.reply_text(
 #               text="НОВОЕ СООБЩЕНИЕ: ТЕСТ",
 #               reply_markup=InlineKeyboardMarkup(care_memo_keyboard)
 #           )
 #           print("✅ УСПЕХ: Новое сообщение отправлено!")
 #       except Exception as e2:
 #           print(f"🔴 ОШИБКА и в новом сообщении: {e2}")
 #       return None

#async def handle_care_memo_part1(update: Update, context: ContextTypes.DEFAULT_TYPE):
 #   """Часть 1 памятки"""
 #   query = update.callback_query
 #   await query.answer()
    
 #   back_button = [[InlineKeyboardButton("⬅️ Назад до Пам'ятки", callback_data='care_memo')]]
 #   await safe_edit_message(
 #       query=query,
 #       text=CARE_MEMO_PART1_TEXT,
 #       reply_markup=InlineKeyboardMarkup(back_button)
 #   )

#async def handle_care_memo_part2(update: Update, context: ContextTypes.DEFAULT_TYPE):
 #   """Часть 2 памятки"""
 #   query = update.callback_query
 #   await query.answer()
    
 #   back_button = [[InlineKeyboardButton("⬅️ Назад до Пам'ятки", callback_data='care_memo')]]
 #   await safe_edit_message(
 #       query=query,
 #       text=CARE_MEMO_PART2_TEXT,
 #       reply_markup=InlineKeyboardMarkup(back_button)
 #   )

async def handle_care_memo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Пам'ятка по догляду - главное меню"""
    query = update.callback_query
    await query.answer()
    
    care_memo_keyboard = [
        [InlineKeyboardButton("1. Повсякденне користування", callback_data='care_memo_part1')],
        [InlineKeyboardButton("2. Зберігання та Догляд", callback_data='care_memo_part2')],
        [InlineKeyboardButton("⬅️ Повернутися до Меню", callback_data='menu_back')]
    ]
    
    await safe_edit_message(
        query=query,
        text=CARE_MEMO_INTRO_TEXT,
        reply_markup=InlineKeyboardMarkup(care_memo_keyboard)
    )

async def handle_care_memo_part1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Часть 1 памятки"""
    query = update.callback_query
    await query.answer()
    
    back_button = [[InlineKeyboardButton("⬅️ Назад до Пам'ятки", callback_data='care_memo')]]
    await safe_edit_message(
        query=query,
        text=CARE_MEMO_PART1_TEXT,
        reply_markup=InlineKeyboardMarkup(back_button)
    )

async def handle_care_memo_part2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Часть 2 памятки"""
    query = update.callback_query
    await query.answer()
    
    back_button = [[InlineKeyboardButton("⬅️ Назад до Пам'ятки", callback_data='care_memo')]]
    await safe_edit_message(
        query=query,
        text=CARE_MEMO_PART2_TEXT,
        reply_markup=InlineKeyboardMarkup(back_button)
    )
