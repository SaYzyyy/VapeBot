from aiogram import types, Router
from bot.handlers.nalichie.user.keyboards.nalichie_keyboard_user_names_odn import nalichie_keyboard_names_user_odn
from bot.handlers.nalichie.user.keyboards.nalichie_keyboard_user_prods_odn import show_prods_user_odn
from datetime import datetime
from bot.handlers.nalichie.user.keyboards.nalichie_keyboard_user import first_choose_user
from bot.handlers.start import string_for_admins
import os
import json

odn_user_router = Router()
prod = {}

@odn_user_router.callback_query(lambda c: c.data == "nal_odn")
async def odnorazki(callback_query: types.CallbackQuery):
    global number_odn
    global string_for_admins
    global number_odn_t
    global odn_type
    global prod
    await callback_query.message.answer(text = "Выберите производителя:", reply_markup=nalichie_keyboard_names_user_odn(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal"), number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_odn = 10
    string_for_admins = ""
    number_odn_t = 10
    odn_type = ""

@odn_user_router.callback_query(lambda c: c.data.startswith("no_"))
async def prods_lists(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_odn
    global odn_type
    string_for_admins += callback_query.data.split("no_")[1].replace("_", " ") + "0 MG ) "
    odn_type = callback_query.data.split("no_")[1]
    prod['name'] = f'{string_for_admins}'
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_user_odn(callback_query.data.split("no_")[1], number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_odn = 10
#
@odn_user_router.callback_query(lambda c: c.data == ("next_odn_nal"))
async def next_odn(callback_query: types.CallbackQuery):
    global number_odn
    number_odn += 10
    await callback_query.message.answer(text="Выберите производителя:", reply_markup=nalichie_keyboard_names_user_odn(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal"), number = number_odn))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_user_router.callback_query(lambda c: c.data == ("back_odn_nal"))
async def back_odn(callback_query: types.CallbackQuery):
    global number_odn
    number_odn -= 10
    await callback_query.message.answer(text="Выберите производителя:", reply_markup=nalichie_keyboard_names_user_odn(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal"), number = number_odn))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_user_router.callback_query(lambda c: c.data == ("next_zh_t_nal"))
async def next_odn_t(callback_query: types.CallbackQuery):
    global number_odn_t
    global odn_type
    number_odn_t += 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_user_odn(odn_type, number = number_odn_t))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_user_router.callback_query(lambda c: c.data == ("back_zh_t_nal"))
async def back_odn_t(callback_query: types.CallbackQuery):
    global number_odn_t
    global odn_type
    number_odn_t -= 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_user_odn(odn_type, number = number_odn_t))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_user_router.callback_query(lambda c: c.data.startswith("nod_"))
async def taste_list(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    global prod
    prod['name'] += f'({callback_query.data.split("nod_")[1].replace("_", " ")})'
    string_for_admins += callback_query.data.split("nod_")[1].replace("_", " ")
    with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json", "r") as file:
        print(f"{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}")
        print(prod['name'])
        f = json.load(file)
        products = f["products"]
        for item in products:
            if item['name'] == prod['name']:
                products.remove(item)
                with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json","w") as fil:
                    json.dump({"products":products}, fil, indent=4, ensure_ascii=False)
                    if len(products) == 0:
                        os.remove(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json")
                break
    await callback_query.bot.send_message(chat_id="@predzakazyy", text=f"{callback_query.from_user.full_name}\n@{callback_query.from_user.username}"
                                                                f"\n{callback_query.from_user.id}\n{string_for_admins.replace("  "," ")}\n{datetime.now(tz = None)}")
    await callback_query.message.answer(text = f"Заказ {string_for_admins} принят. Чтобы сделать новый заказ, выберите кнопку ниже:", reply_markup = first_choose_user())
    await callback_query.answer()
    await callback_query.message.delete()
    string_for_admins = ""
    number_odn = 10