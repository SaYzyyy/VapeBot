import random

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import json
import os

def show_prods_user(file, number):
    builder = InlineKeyboardBuilder()
    emojis = '🥰😍😘🥵😳🤯🤫😮🥱😎😛😋😌🙃😆😅😏🤩'
    if os.path.exists(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{file.replace("_", " ").replace("  ", " ")}0 MG ).json"):
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{file.replace("_", " ")}0 MG ).json", "r", encoding="utf-8") as f:
            data = json.load(f)
            products = data['products']
            for i, item in enumerate(products[number-10:number+1]):
                name = item["name"]
                if name.count("(") >= 2:
                    namel = name.split("(")
                    builder.add(InlineKeyboardButton(
                        text=namel[2].strip().rstrip(")") + random.choice(emojis),
                        callback_data=f"nzh_{namel[2].strip().rstrip(")").strip().replace("  ", " ").replace(" - ", "_").replace(' ', '_')}"))
                if i == 10 and number == 10:
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_zh_t_nal"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="nal_zh"
                    ))
                elif i == 10 and number > 10 and (len(products) > number):
                    builder.add(InlineKeyboardButton(
                        text="Назад <-",
                        callback_data="back_zh_t_nal"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_zh_t_nal"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="nal_zh"
                    ))
            if (len(products) < number) and number == 10:
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="nal_zh"
                ))
            elif (len(products) < number) or (len(products) == number):
                builder.add(InlineKeyboardButton(
                    text="Назад <-",
                    callback_data="back_zh_t_nal"
                ))
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="nal_zh"
                ))


    builder.adjust(1)

    return builder.as_markup()