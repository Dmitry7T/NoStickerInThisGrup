from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart
from config import Settings

main_router = Router()

INSTRUCTION_START = "Bot is active"

@main_router.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(
        text=INSTRUCTION_START
    )

@main_router.message(lambda message: message.sticker and (message.from_user.id == Settings.RESTRICTED_USER_ID))
async def delete_restricted_user_sticker(message: Message):
    await message.delete()

@main_router.message(lambda message: message.animation and message.from_user.id == Settings.RESTRICTED_USER_ID)
async def delete_restricted_user_gif(message: Message):
    await message.delete()