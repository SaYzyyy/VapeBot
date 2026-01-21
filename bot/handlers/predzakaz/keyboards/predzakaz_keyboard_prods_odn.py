from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
import json
import os

def show_prods(file, number_o):
    builder = InlineKeyboardBuilder()
    if os.path.exists(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/odnorazki/{file.replace("(", "(_").replace(")", "_)").replace("_", " ")}0 MG ).json"):
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/odnorazki/{file.replace("(", "(_").replace(")", "_)").replace("_", " ")}0 MG ).json", "r", encoding="utf-8") as f:
            data = json.load(f)
            products = data.get("products")
            for i, item in enumerate(products[number_o-10:number_o+1]):
                emojis = '🥰😍😘🥵😳🤯🤫😮🥱😎😛😋😌🙃😆😅😏🤩'
                name = item["name"]
                if name.count("(") == 1 and "MG" not in name.split("(")[1] and "%" not in name.split("(")[1] and "НИКОТИНА" not in name.split("(")[1]:
                    namel = name.split("(")
                    builder.add(InlineKeyboardButton(
                        text=namel[1].strip().rstrip(")") + random.choice(emojis),
                        callback_data=f"or_{namel[1].strip().rstrip(")").strip().replace("  ", " ").replace(" - ", "_").replace(' ', '_')}")
                    )
                elif name.count("(") == 2:
                    namel = name.split("(")
                    builder.add(InlineKeyboardButton(
                        text=namel[2].strip().rstrip(")"),
                        callback_data=f"or_{namel[2].strip().rstrip(")").strip().replace("  ", " ").replace(" - ", "_").replace(' ', '_')}")
                    )
                if i == 10 and number_o == 10:
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_odn_t"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="odnorazki"
                    ))
                elif i == 10 and number_o > 10 and (len(products) > number_o):
                    builder.add(InlineKeyboardButton(
                        text="Назад <-",
                        callback_data="back_odn_t"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_odn_t"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору производителя <-",
                        callback_data="odnorazki"
                    ))
            if (len(products) < number_o) and number_o == 10:
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="odnorazki"
                ))
            elif (len(products) < number_o) or (len(products) == number_o):
                builder.add(InlineKeyboardButton(
                    text="Назад <-",
                    callback_data="back_odn_t"
                ))
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору производителя <-",
                    callback_data="odnorazki"
                ))

    builder.adjust(1)

    return builder.as_markup()