import asyncio # aiogram - асинхронная библиотека
import logging # Для работы бота и функций
from aiogram import Bot, Dispatcher # Для работы бота и функций
from handlers import commands, different_types, OpenRouter
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(os.getenv('BOT_TOKEN'))

# Диспетчер
dp = Dispatcher()

# Подключаем хэндленры к диспетчеру через роутер
# Важен порядок импортов. Если мы поменяем местами регистрацию роутеров,
# то, например, команда /start передасться хэндлеру из OpenRouter,
# поскольку она первой успешно пройдёт все фильтры.
dp.include_routers(commands.router, different_types.router, OpenRouter.router)

# Пропускаем все накопленные входящие сообщения
# и запускаем процесс поллинга новых апдейтов
async def main():

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
