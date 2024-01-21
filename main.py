import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

#variables
from settings import TG_TOKEN

BOT_TOKEN = TG_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main ():
	logging.basicConfig(level=logging.INFO)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())

