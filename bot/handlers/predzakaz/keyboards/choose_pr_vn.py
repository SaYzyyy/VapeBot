from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def first_choose():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text="Одноразки 🔫", callback_data="odnorazki"),
             InlineKeyboardButton(text="Жидкости 💣", callback_data="zhizhi"),
             InlineKeyboardButton(text="Под-системы 🧨", callback_data="pods"),],
            [InlineKeyboardButton(text="Назад к наличию <-", callback_data="back_to_choose"),],
        ]
    )

    return keyboard