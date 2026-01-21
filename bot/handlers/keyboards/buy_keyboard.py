from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def buy_keyboard(file):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=item, callback_data=f"show_{item}")]
            for item in file
        ]
    )
    return keyboard