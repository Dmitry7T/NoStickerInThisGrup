import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher

from config import Settings
from main_handlers import main_router as router

async def main():

    bot = Bot(token = Settings.TOKEN)
    dp = Dispatcher()
    dp.include_router(
        router
    )

    print('bot start...')
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format="%(asctime)s %(levelname)s %(message)s")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot off...')