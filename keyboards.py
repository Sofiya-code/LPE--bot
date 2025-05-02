from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_keyboard():
    """Главная клавиатура"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔍 Поиск термина", callback_data="search")],
        [InlineKeyboardButton("📚 Категории терминов", callback_data="categories")],
        [InlineKeyboardButton("ℹ️ Помощь", callback_data="help")],
        [InlineKeyboardButton("✨ Информация", callback_data="info")]
    ])


def get_categories_keyboard():
    """Клавиатура категорий"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton("🔤 Лингвистика", callback_data="cat_linguistics"),
            InlineKeyboardButton("📚 Педагогика", callback_data="cat_pedagogy")
        ],
        [
            InlineKeyboardButton("💰 Экономика", callback_data="cat_economics"),
            InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")
        ]
    ])


def get_back_keyboard():
    """Клавиатура с кнопкой назад"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Назад", callback_data="back_to_main")]
    ])
