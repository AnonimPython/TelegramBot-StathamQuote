import dotenv
import os
dotenv.load_dotenv()

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from app.handlers import router

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())