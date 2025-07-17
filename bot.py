import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

print("Пути поиска в bot.py", sys.path, "\n")
import asyncio
import logging
from aiogram import Bot, Dispatcher

# Все импорты идут от корня проекта
from config import API_TOKEN
from utils.database import create_table
from handlers import quiz_handlers

logging.basicConfig(level=logging.INFO)

# Создаем объекты Бота и Диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Подключаем роутер с хэндлерами из файла quiz_handlers.py
dp.include_router(quiz_handlers.router)

# Главная функция для запуска бота
async def main():
    await create_table()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())