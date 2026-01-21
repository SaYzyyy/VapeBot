from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os

def predzakaz_keyboard_names(folder, number):
    builder = InlineKeyboardBuilder()
    for i, item in enumerate(folder[number-10:number+1]):
        if ("( 20 MG )" in item) or ("( 30 MG )" in item) or ("( 40 MG )" in item):
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " 450р 💸",
                callback_data=f"p_{item[:-11].replace(' ', '_')}")
            )
        elif ("( 50 MG )" in item) or ("( 60 MG )" in item) or ("( 70 MG )" in item) or ("( 80 MG )" in item):
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " 500р 💸",
                callback_data=f"p_{item[:-11].replace(' ', '_').replace('( ', ' ').replace(' )', '')}"))
        if i == 10 and number == 10:
            builder.add(InlineKeyboardButton(
                text="Далее ->",
                callback_data="next_zhizha"
            )),
            builder.add(InlineKeyboardButton(
                text="Назад к выбору типа <-",
                callback_data="predzakaz"
            ))
        elif i == 10 and number > 10 and (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/zhizha")) > number):
            builder.add(InlineKeyboardButton(
                text="Назад <-",
                callback_data="back_zhizha"
            ))
            builder.add(InlineKeyboardButton(
                text="Далее ->",
                callback_data="next_zhizha"
            ))
            builder.add(InlineKeyboardButton(
                text="Назад к выбору типа <-",
                callback_data="predzakaz"
            ))


    if (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/zhizha")) < number) or (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/zhizha")) == number):
        builder.add(InlineKeyboardButton(
            text="Назад <-",
            callback_data="back_zhizha"
        ))
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="predzakaz"
        ))


    builder.adjust(1)

    return builder.as_markup()