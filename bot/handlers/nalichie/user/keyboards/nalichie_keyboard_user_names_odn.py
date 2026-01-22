from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
import json


def nalichie_keyboard_names_user_odn(folder, number):
    builder = InlineKeyboardBuilder()
    for i, item in enumerate(folder[number-10:number+1]):
        price = 0
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki/{item}","r") as f:
            data = json.load(f)
            products = data.get("products")
            for product in products:
                price = product["price"]
                break
        if int(price * 1.4) < 500:
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " 500р 💸",
                callback_data=f"no_{item[:-11].replace(' ', '_')}")
            )
        else:
            builder.add(InlineKeyboardButton(
                text=item[:-5] + f" {int(price * 1.4)}р 💸",
                callback_data=f"no_{item[:-11].replace(' ', '_').replace('( ', ' ').replace(' )', '')}"))
        if i == 10 and number == 10:
             builder.add(InlineKeyboardButton(
                 text="Далее ->",
                 callback_data="next_odn_nal"
             )),
             builder.add(InlineKeyboardButton(
                 text="Назад к выбору типа <-",
                 callback_data="v_nalichii"
             ))
        elif i == 10 and number > 10 and (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal")) > number):
            builder.add(InlineKeyboardButton(
                text="Назад <-",
                callback_data="back_odn_nal"
            ))
            builder.add(InlineKeyboardButton(
                text="Далее ->",
                callback_data="next_odn_nal"
            ))
            builder.add(InlineKeyboardButton(
                text="Назад к выбору типа <-",
                callback_data="v_nalichii"
            ))
    if (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal")) < number) and number == 10:
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="v_nalichii"
        ))
    elif (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal")) < number) or (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal")) == number):
        builder.add(InlineKeyboardButton(
            text="Назад <-",
            callback_data="back_odn_nal"
        ))
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="v_nalichii"
        ))
    builder.adjust(1)
    return builder.as_markup()