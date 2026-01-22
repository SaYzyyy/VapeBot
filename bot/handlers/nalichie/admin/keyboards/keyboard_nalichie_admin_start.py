from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def first_choose_admin():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text="Одноразки 🔫", callback_data="add_odn"),
             InlineKeyboardButton(text="Жидкости 💣", callback_data="add_zh"),],
            [InlineKeyboardButton(text="Вернуться в юзер-панель <-", callback_data="back_to_choose"),]
        ]
    )

    return keyboard