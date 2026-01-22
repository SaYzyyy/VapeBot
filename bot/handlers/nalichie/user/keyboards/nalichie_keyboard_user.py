from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def first_choose_user():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text="Одноразки 🔫", callback_data="nal_odn"),
             InlineKeyboardButton(text="Жидкости 💣", callback_data="nal_zh")],
            [InlineKeyboardButton(text="Назад к наличию <-", callback_data="back_to_choose"),]
        ]
    )

    return keyboard