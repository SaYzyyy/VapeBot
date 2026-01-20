from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from handlers import Register_Routes
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    Register_Routes(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
        print("pizdec")
    except KeyboardInterrupt:
        print("pizdec")

