from aiogram import types, Router
from bot.handlers.nalichie.admin.keyboards.keyboard_nalichie_names_odn_admin import nalichie_keyboard_names_odn
from bot.handlers.nalichie.admin.keyboards.keyboard_nalichie_prods_odn_admin import show_prods_admin_odn
# from datetime import datetime
from bot.handlers.nalichie.admin.keyboards.keyboard_nalichie_admin_start import first_choose_admin
import os
import json

odn_admin_router = Router()
prod = {'category': 'ЖИДКОСТИ'}

@odn_admin_router.callback_query(lambda c: c.data == "add_odn")
async def odnorazki(callback_query: types.CallbackQuery):
    global number_odn
    global string_for_admins
    global number_odn_t
    global odn_type
    global prod
    await callback_query.message.answer(text = "Выберите производителя:", reply_markup=nalichie_keyboard_names_odn(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki"), number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    prod = {'category': 'ЭЛЕКТРОНКИ'}
    number_odn = 10
    string_for_admins = ""
    number_odn_t = 10
    odn_type = ""

@odn_admin_router.callback_query(lambda c: c.data.startswith("ao_"))
async def prods_lists(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_odn
    global odn_type
    string_for_admins += callback_query.data.split("ao_")[1].replace("_", " ") + "0 MG ) "
    print(callback_query.data.split("ao_")[1].replace("_", " ") + "0 MG ) ")
    prod['name'] = f'{string_for_admins}'
    odn_type = callback_query.data.split("ao_")[1]
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_admin_odn(callback_query.data.split("ao_")[1], number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_odn = 10

@odn_admin_router.callback_query(lambda c: c.data == ("next_odn_add"))
async def next_odn(callback_query: types.CallbackQuery):
    global number_odn
    number_odn += 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=nalichie_keyboard_names_odn(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki"), number = number_odn))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_admin_router.callback_query(lambda c: c.data == ("back_odn_add"))
async def back_odn(callback_query: types.CallbackQuery):
    global number_odn
    number_odn -= 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=nalichie_keyboard_names_odn(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki"), number = number_odn))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_admin_router.callback_query(lambda c: c.data == ("next_o_t_add"))
async def next_zh_t(callback_query: types.CallbackQuery):
    global number_odn_t
    global odn_type
    number_odn_t += 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_admin_odn(odn_type, number = number_odn_t))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_admin_router.callback_query(lambda c: c.data == ("back_o_t_add"))
async def back_zh_t(callback_query: types.CallbackQuery):
    global number_odn_t
    global odn_type
    number_odn_t -= 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_admin_odn(odn_type, number = number_odn_t))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_admin_router.callback_query(lambda c: c.data.startswith("ado_"))
async def taste_list(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    global prod
    prod['name'] += f'({callback_query.data.split("ado_")[1].replace("_", " ")})'
    prod['name'] = prod['name'].replace("  ", " ")
    string_for_admins += callback_query.data.split("ado_")[1].replace("_", " ")
    # await callback_query.bot.send_message(chat_id="@predzakazyy", text=f"{callback_query.from_user.full_name}\n@{callback_query.from_user.username}"
    #                                                             f"\n{callback_query.from_user.id}\n{string_for_admins.replace("  "," ")}\n{datetime.now(tz = None)}")
    if not(os.path.exists(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json")):
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json", "w") as file:
            json.dump({"products":[prod]}, file, indent=4, ensure_ascii=False)
    else:
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/odnorazki_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json", "r+") as file:
            data = json.load(file)
            products = data.get("products", [])
            products.append(prod)
            file.seek(0)
            json.dump({"products":products}, file, indent=4, ensure_ascii=False)
            file.truncate()
    await callback_query.message.answer(text = f"Товар {string_for_admins} добавлен. Чтобы добавить новый товар, выберите кнопку ниже:", reply_markup = first_choose_admin())
    await callback_query.answer()
    await callback_query.message.delete()
    string_for_admins = ""
    number_zh = 10