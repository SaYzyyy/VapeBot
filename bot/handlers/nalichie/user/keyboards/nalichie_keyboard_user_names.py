from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os


def nalichie_keyboard_names_user(folder, number):
    builder = InlineKeyboardBuilder()
    for i, item in enumerate(folder[number-10:number+1]):
        if ("( 20 MG )" in item) or ("( 30 MG )" in item) or ("( 40 MG )" in item):
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " 450р 💸",
                callback_data=f"n_{item[:-11].replace(' ', '_')}")
            )
        elif ("( 50 MG )" in item) or ("( 60 MG )" in item) or ("( 70 MG )" in item) or ("( 80 MG )" in item):
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " 500р 💸",
                callback_data=f"n_{item[:-11].replace(' ', '_').replace('( ', ' ').replace(' )', '')}"))
        if i == 10 and number == 10:
             builder.add(InlineKeyboardButton(
                 text="Далее ->",
                 callback_data="next_zhizha_nal"
             )),
             builder.add(InlineKeyboardButton(
                 text="Назад к выбору типа <-",
                 callback_data="v_nalichii"
             ))
        elif i == 10 and number > 10 and (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal")) > number):
            builder.add(InlineKeyboardButton(
                text="Назад <-",
                callback_data="back_zhizha_nal"
            ))
            builder.add(InlineKeyboardButton(
                text="Далее ->",
                callback_data="next_zhizha_nal"
            ))
            builder.add(InlineKeyboardButton(
                text="Назад к выбору типа <-",
                callback_data="v_nalichii"
            ))
    if (len(os.listdir(
            "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal")) < number) and number == 10:
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="v_nalichii"
        ))
    elif (len(os.listdir(
            "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal")) < number) or (
            len(os.listdir(
                    "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal")) == number):
        builder.add(InlineKeyboardButton(
            text="Назад <-",
            callback_data="back_zhizha_nal"
        ))
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="v_nalichii"
        ))
    builder.adjust(1)
    return builder.as_markup()