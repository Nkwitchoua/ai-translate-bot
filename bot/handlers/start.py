from aiogram import Router, types
from aiogram.filters import CommandStart
from ..keyboards.inline import translate_keyboard

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    print(message)
    await message.answer("Привет! Я — бот-переводчик. Отправь мне текст, и я переведу его для тебя.", reply_markup=translate_keyboard)
