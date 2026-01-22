import json

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os


def nalichie_keyboard_names_odn(folder, number):
    builder = InlineKeyboardBuilder()
    for i, item in enumerate(folder[number-10:number+1]):
        price = 0
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki/{item}", "r") as f:
            data = json.load(f)
            products = data.get("products")
            for product in products:
                price = product["price"]
                break
        if int(price*1.4) < 500:
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " 500р 💸",
                callback_data=f"ao_{item[:-11].replace(' ', '_')}")
            )
        else:
            builder.add(InlineKeyboardButton(
                text=item[:-5] + f" {int(price*1.4)}р 💸",
                callback_data=f"ao_{item[:-11].replace(' ', '_').replace('( ', ' ').replace(' )', '')}"))
        if i == 10 and number == 10:
             builder.add(InlineKeyboardButton(
                 text="Далее ->",
                 callback_data="next_odn_add"
             )),
             builder.add(InlineKeyboardButton(
                 text="Назад к выбору типа <-",
                 callback_data="admin"
             ))
        elif i == 10 and number > 10 and (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki")) > number):
            builder.add(InlineKeyboardButton(
                text="Назад <-",
                callback_data="back_odn_add"
            ))
            builder.add(InlineKeyboardButton(
                text="Далее ->",
                callback_data="next_odn_add"
            ))
            builder.add(InlineKeyboardButton(
                text="Назад к выбору типа <-",
                callback_data="admin"
            ))
    if (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki")) < number) and number == 10:
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="admin"
        ))
    elif (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki")) < number) or (len(os.listdir("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki")) == number):
        builder.add(InlineKeyboardButton(
            text="Назад <-",
            callback_data="back_odn_add"
        ))
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="admin"
        ))
    builder.adjust(1)
    return builder.as_markup()