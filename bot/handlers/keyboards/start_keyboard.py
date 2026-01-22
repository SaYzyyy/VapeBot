from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ПРЕДЗАКАЗ 🕓", callback_data="predzakaz"),
             InlineKeyboardButton(text="В НАЛИЧИИ 👇", callback_data="v_nalichii"),
             InlineKeyboardButton(text="АДМИН ПАНЕЛЬ", callback_data="admin")]
        ]
    )

    return keyboard