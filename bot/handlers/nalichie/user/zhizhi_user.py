from aiogram import types, Router
from bot.handlers.nalichie.user.keyboards.nalichie_keyboard_user_names import nalichie_keyboard_names_user
from bot.handlers.nalichie.user.keyboards.nalichie_keyboard_user_prods import show_prods_user
from datetime import datetime
from bot.handlers.nalichie.user.keyboards.nalichie_keyboard_user import first_choose_user
from bot.handlers.start import string_for_admins
import os
import json

zh_user_router = Router()
prod = {}

@zh_user_router.callback_query(lambda c: c.data == "nal_zh")
async def zhizhi(callback_query: types.CallbackQuery):
    global number_zh
    global string_for_admins
    global number_zh_t
    global zh_type
    global prod
    await callback_query.message.answer(text = "Выберите производителя:", reply_markup=nalichie_keyboard_names_user(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal"), number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_zh = 10
    string_for_admins = ""
    number_zh_t = 10
    zh_type = ""

@zh_user_router.callback_query(lambda c: c.data.startswith("n_"))
async def prods_lists(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    global zh_type
    string_for_admins += callback_query.data.split("n_")[1].replace("_", " ") + "0 MG ) "
    zh_type = callback_query.data.split("n_")[1]
    prod['name'] = f'{string_for_admins}'
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_user(callback_query.data.split("n_")[1], number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_zh = 10
#
@zh_user_router.callback_query(lambda c: c.data == ("next_zhizha_nal"))
async def next_zhizha(callback_query: types.CallbackQuery):
    global number_zh
    number_zh += 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=nalichie_keyboard_names_user(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal"), number = number_zh))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_user_router.callback_query(lambda c: c.data == ("back_zhizha_nal"))
async def back_zhizha(callback_query: types.CallbackQuery):
    global number_zh
    number_zh -= 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=nalichie_keyboard_names_user(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal"), number = number_zh))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_user_router.callback_query(lambda c: c.data == ("next_zh_t_nal"))
async def next_zh_t(callback_query: types.CallbackQuery):
    global number_zh_t
    global zh_type
    number_zh_t += 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_user(zh_type, number = number_zh_t))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_user_router.callback_query(lambda c: c.data == ("back_zh_t_nal"))
async def back_zh_t(callback_query: types.CallbackQuery):
    global number_zh_t
    global zh_type
    number_zh_t -= 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_user(zh_type, number = number_zh_t))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_user_router.callback_query(lambda c: c.data.startswith("nzh_"))
async def taste_list(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    global prod
    prod['name'] += f'({callback_query.data.split("nzh_")[1].replace("_", " ")})'
    string_for_admins += callback_query.data.split("nzh_")[1].replace("_", " ")
    with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json", "r") as file:
        print(f"{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}")
        print(prod['name'])
        f = json.load(file)
        products = f["products"]
        for item in products:
            if item['name'] == prod['name']:
                products.remove(item)
                with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json","w") as fil:
                    json.dump({"products":products}, fil, indent=4, ensure_ascii=False)
                    if len(products) == 0:
                        os.remove(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json")
                break
    await callback_query.bot.send_message(chat_id="@predzakazyy", text=f"{callback_query.from_user.full_name}\n@{callback_query.from_user.username}"
                                                                f"\n{callback_query.from_user.id}\n{string_for_admins.replace("  "," ")}\n{datetime.now(tz = None)}")
    await callback_query.message.answer(text = f"Заказ {string_for_admins} принят. Чтобы сделать новый заказ, выберите кнопку ниже:", reply_markup = first_choose_user())
    await callback_query.answer()
    await callback_query.message.delete()
    string_for_admins = ""
    number_zh = 10