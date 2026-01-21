from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
import json

def predzakaz_keyboard_names(folder, number):
    builder = InlineKeyboardBuilder()
    for i, item in enumerate(folder[number-10:number+1]):
        with open(f"../parsers/odnorazki/{item}") as f:
            data = json.load(f)
        products = data.get("products")
        price = 0
        for product in products[:2]:
            price = int(product["price"])
        if int(price*1.4) < 450:
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " 500" + "р 💸",
                callback_data=f"o_{item[:-11].replace(' ', '_').replace("(_", "(").replace("_)", ")")}")
            )
        else:
            builder.add(InlineKeyboardButton(
                text=item[:-5] + " " + str(int(price*1.4)) + "р 💸",
                callback_data=f"o_{item[:-11].replace(' ', '_').replace("(_", "(").replace("_)", ")")}")
            )
        if i == 10 and number == 10:
            builder.add(InlineKeyboardButton(
                text="Далее ->",
                callback_data="next_odn"
            ))
            builder.add(InlineKeyboardButton(
                text="Назад к выбору типа <-",
                callback_data="predzakaz"
            ))
        elif i == 10 and number > 10 and (
                len(os.listdir("parsers/odnorazki")) > number):
            builder.add(InlineKeyboardButton(
                text="Назад <-",
                callback_data="back_odn"
            ))
            builder.add(InlineKeyboardButton(
                text="Далее ->",
                callback_data="next_odn"
            ))
            builder.add(InlineKeyboardButton(
                text="Назад к выбору типа <-",
                callback_data="predzakaz"
            ))

    if (len(os.listdir("parsers/odnorazki")) < number) or (len(os.listdir("parsers/odnorazki")) == number):
        builder.add(InlineKeyboardButton(
            text="Назад <-",
            callback_data="back_odn"
        ))
        builder.add(InlineKeyboardButton(
            text="Назад к выбору типа <-",
            callback_data="predzakaz"
        ))


    builder.adjust(1)

    return builder.as_markup()