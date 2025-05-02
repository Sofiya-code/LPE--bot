import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers.common import register_common_handlers
from handlers.search import register_search_handlers


# Настройка логгирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def on_startup(dp: Dispatcher):
    """Действия при запуске бота"""
    logger.info("Бот запущен")


def register_all_handlers(dp: Dispatcher):
    """Регистрация всех обработчиков"""
    register_common_handlers(dp)
    register_search_handlers(dp)


if __name__ == '__main__':
    # Инициализация бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Регистрация обработчиков
    register_all_handlers(dp)

    # Запуск бота
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)