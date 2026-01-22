import random

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import json
import os

def show_prods_admin_odn(file, number):
    builder = InlineKeyboardBuilder()
    emojis = '🥰😍😘🥵😳🤯🤫😮🥱😎😛😋😌🙃😆😅😏🤩'
    if os.path.exists(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/odnorazki/{file.replace("_", " ")}0 MG ).json"):
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/odnorazki/{file.replace("_", " ")}0 MG ).json", "r", encoding="utf-8") as f:
            data = json.load(f)
            products = data.get("products")
            for i, item in enumerate(products[number-10:number+1]):
                name = item["name"]
                if name.count("(") == 1 and "MG" not in name.split("(")[1] and "%" not in name.split("(")[1] and "НИКОТИНА" not in name.split("(")[1]:
                    namel = name.split("(")
                    builder.add(InlineKeyboardButton(
                        text=namel[1].strip().rstrip(")") + random.choice(emojis),
                        callback_data=f"ado_{namel[1].strip().rstrip(")").strip().replace("  ", " ").replace(" - ", "_").replace(' ', '_')}")
                    )
                elif name.count("(") == 2:
                    namel = name.split("(")
                    builder.add(InlineKeyboardButton(
                        text=namel[2].strip().rstrip(")"),
                        callback_data=f"ado_{namel[2].strip().rstrip(")").strip().replace("  ", " ").replace(" - ", "_").replace(' ', '_')}")
                    )
                if i == 10 and number == 10:
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_o_t_add"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="add_odn"
                    ))
                elif i == 10 and number > 10 and (len(products) > number):
                    builder.add(InlineKeyboardButton(
                        text="Назад <-",
                        callback_data="back_o_t_add"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_o_t_add"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="add_odn"
                    ))
            if (len(products) < number) and number == 10:
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="add_odn"
                ))
            elif (len(products) < number) or (len(products) == number):
                builder.add(InlineKeyboardButton(
                    text="Назад <-",
                    callback_data="back_o_t_add"
                ))
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="add_odn"
                ))


    builder.adjust(1)

    return builder.as_markup()