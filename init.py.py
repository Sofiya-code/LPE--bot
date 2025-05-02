from aiogram import types
from aiogram.dispatcher import FSMContext

from ..keyboards import get_main_keyboard
from ..data.terms import TERMS


async def search_command(callback: types.CallbackQuery):
    """Обработчик команды поиска"""
    await callback.message.edit_text(
        "Введите термин для поиска:",
        reply_markup=get_back_keyboard()
    )
    await callback.answer()


async def handle_search(message: types.Message, state: FSMContext):
    """Обработчик поиска терминов"""
    search_term = message.text.lower().strip()
    if not search_term:
        await message.answer(
            "Пожалуйста, введите поисковый запрос.",
            reply_markup=get_main_keyboard()
        )
        return

    user_data = await state.get_data()
    current_category = user_data.get('current_category')
    matches = []

    if current_category:
        category_terms = TERMS.get(current_category, {})
        for term, details in category_terms.items():
            if search_term in term.lower():
                matches.append(f"Термин: {term}\n" + "\n".join(f"{k}: {v}" for k, v in details.items()))
    else:
        for category, terms in TERMS.items():
            for term, details in terms.items():
                if search_term in term.lower():
                    matches.append(f"Термин: {term} (категория: {category})\n" + 
                                "\n".join(f"{k}: {v}" for k, v in details.items()))

    if matches:
        await message.answer(
            f"🔍 Найдено терминов: {len(matches)}",
            reply_markup=get_main_keyboard()
        )
        
        for match in matches:
            await message.answer(match)
    else:
        await message.answer(
            "❌ Термин не найден. Попробуйте другой запрос.",
            reply_markup=get_main_keyboard()
        )


def register_search_handlers(dp: Dispatcher):
    """Регистрация обработчиков поиска"""
    dp.register_callback_query_handler(search_command, text="search")
    dp.register_message_handler(handle_search, state="*")