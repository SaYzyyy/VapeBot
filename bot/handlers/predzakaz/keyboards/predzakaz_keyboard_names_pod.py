from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import json
import os

def show_prods_pods(file, number):
    builder = InlineKeyboardBuilder()
    if os.path.exists(f"{file}"):
        with open(f"{file}", "r", encoding="utf-8") as f:
            data = json.load(f)
            for i, item in enumerate(data[number-10:number+1]):
                name = item["name"]
                with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/pods/{name}.json", "r", encoding="utf-8") as file:
                    data1 = json.load(file)
                    price = 0
                    products = data1["products"]
                    for product in products[0:2]:
                        price = product["price"]
                builder.add(InlineKeyboardButton(
                    text=name + " " + str(int(price*1.3)) + "р 💸",
                    callback_data=f"pod_{name.strip().replace(" - ", "_").replace(' ', '_')}")
                )
                if i == 10 and number == 10:
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_pod"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору типа <-",
                        callback_data="predzakaz"
                    ))
                elif i == 10 and number > 10 and (len(data) > number):
                    builder.add(InlineKeyboardButton(
                        text="Назад <-",
                        callback_data="back_pod"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Далее ->",
                        callback_data="next_pod"
                    ))
                    builder.add(InlineKeyboardButton(
                        text="Назад к выбору типа <-",
                        callback_data="predzakaz"
                    ))
            if (len(data) < number) or (len(data) == number):
                builder.add(InlineKeyboardButton(
                    text="Назад <-",
                    callback_data="back_pod"
                ))
                builder.add(InlineKeyboardButton(
                    text="Назад к выбору типа <-",
                    callback_data="predzakaz"
                ))

    builder.adjust(1)

    return builder.as_markup()