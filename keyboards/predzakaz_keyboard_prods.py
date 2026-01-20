import random

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import json
import os

def show_prods(file, number):
    builder = InlineKeyboardBuilder()
    print(file)
    emojis = '🥰😍😘🥵😳🤯🤫😮🥱😎😛😋😌🙃😆😅😏🤩'
    if os.path.exists(f"../parsers/zhizha/{file.replace("_", " ")}0 MG ).json"):
        with open(f"../parsers/zhizha/{file.replace("_", " ")}0 MG ).json", "r", encoding="utf-8") as f:
            data = json.load(f)
            products = data.get("products")
            for i, item in enumerate(products[number-10:number+1]):
                name = item["name"]
                if name.count("(") >= 1:
                    namel = name.split("(")
                    builder.add(InlineKeyboardButton(
                        text=namel[1].strip().rstrip(")") + random.choice(emojis),
                        callback_data=f"r_{namel[1].strip().rstrip(")").strip().replace("  ", " ").replace(" - ", "_").replace(' ', '_')}"))
                if i == 10 and number == 10:
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_zh_t"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="zhizhi"
                    ))
                elif i == 10 and number > 10 and (len(products) > number):
                    builder.add(InlineKeyboardButton(
                        text="Назад <-",
                        callback_data="back_zh_t"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_zh_t"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="zhizhi"
                    ))
            if (len(products) < number) and number == 10:
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="zhizhi"
                ))
            elif (len(products) < number) or (len(products) == number):
                builder.add(InlineKeyboardButton(
                    text="Назад <-",
                    callback_data="back_zh_t"
                ))
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="zhizhi"
                ))


    builder.adjust(1)

    return builder.as_markup()