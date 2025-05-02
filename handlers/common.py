from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext

from ..keyboards import get_main_keyboard, get_categories_keyboard, get_back_keyboard
from ..data.terms import TERMS


async def start_command(message: types.Message):
    """Обработчик команды /start"""
    await message.answer(
        "👋 Привет! Я бот-словарь терминов\n\nВыберите действие:",
        reply_markup=get_main_keyboard()
    )


async def help_command(callback: types.CallbackQuery):
    """Обработчик команды помощи"""
    help_text = (
        "📖 Руководство по использованию бота\n\n"
        "🔍 Как искать термины:\n"
        "1. Нажмите '🔍 Поиск термина'\n"
        "2. Введите слово или часть слова\n"
        "3. Бот найдет все совпадения\n\n"
        "📚 Можно выбрать конкретную категорию:\n"
        "1. Нажмите '📚 Категории терминов'\n"
        "2. Выберите нужную категорию\n"
        "3. Введите термин для поиска\n\n"
        "✨ Разработано студентами курса «Цифровой переводчик»"
    )
    await callback.message.edit_text(
        help_text,
        reply_markup=get_back_keyboard()
    )
    await callback.answer()


async def info_command(callback: types.CallbackQuery):
    """Обработчик команды информации"""
    info_text = (
        "💡 Это разработка студентов курса «Цифровой переводчик».\n\n"
        "🎯 Цель проекта: оптимизировать поиск терминов, их значений в паре языков "
        "(русский-английский) для обеспечения их адекватного/эквивалентного перевода "
        "в области лингвистики, педагогики и экономики.\n\n"
        "🚀 Основные преимущества:\n"
        "1️⃣ Постоянная доступность ✅\n"
        "2️⃣ Учет контекста вводимого термина 💡\n"
        "3️⃣ Экономия времени при переводе в узкоспециальной отрасли⏱️\n\n"
        "👨‍💻 Создатели проекта:\n"
        "- Цандер София, 139 (тимлид);\n"
        "- Тимофеева Виталия, 139;\n"
        "- Махмутова Залина, 139;\n"
        "- Мухаметзянова Аделя, 139;\n"
        "- Баянов Данил, 139;\n"
        "- Амиров Рамиль, 139."
    )
    await callback.message.edit_text(
        info_text,
        reply_markup=get_back_keyboard()
    )
    await callback.answer()


async def categories_command(callback: types.CallbackQuery):
    """Обработчик команды категорий"""
    await callback.message.edit_text(
        "Выберите категорию:",
        reply_markup=get_categories_keyboard()
    )
    await callback.answer()


async def handle_category(callback: types.CallbackQuery, state: FSMContext):
    """Обработчик выбора категории"""
    category = callback.data.split("_")[1]
    category_mapping = {
        "linguistics": "лингвистика",
        "pedagogy": "педагогика", 
        "economics": "экономика"
    }
    mapped_category = category_mapping.get(category)
    
    if mapped_category in TERMS:
        await state.update_data(current_category=mapped_category)
        await callback.message.edit_text(
            f"Вы выбрали категорию: {mapped_category}\nВведите термин для поиска:",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton("К категориям", callback_data="categories")
            ]])
        )
    else:
        await callback.message.edit_text(
            "Извините, категория не найдена.",
            reply_markup=get_categories_keyboard()
        )
    await callback.answer()


async def back_to_main(callback: types.CallbackQuery, state: FSMContext):
    """Обработчик возврата в главное меню"""
    await state.reset_data()
    await callback.message.edit_text(
        "Выберите действие:",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()


def register_common_handlers(dp: Dispatcher):
    """Регистрация обработчиков"""
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(help_command, text="help")
    dp.register_callback_query_handler(info_command, text="info")
    dp.register_callback_query_handler(categories_command, text="categories")
    dp.register_callback_query_handler(handle_category, text_startswith="cat_")
    dp.register_callback_query_handler(back_to_main, text="back_to_main")
