from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

translate_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔁 Перевести", callback_data="translate")],
    [InlineKeyboardButton(text="📄 История", callback_data="history")]
])
