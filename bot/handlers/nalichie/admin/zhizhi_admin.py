from aiogram import types, Router
from bot.handlers.nalichie.admin.keyboards.nalichie_keyboard_admin_names import nalichie_keyboard_names
from bot.handlers.nalichie.admin.keyboards.nalichie_keyboard_admin_prods import show_prods_admin
# from datetime import datetime
from bot.handlers.nalichie.admin.keyboards.keyboard_nalichie_admin_start import first_choose_admin
import os
import json

zh_admin_router = Router()
prod = {'category': 'ЖИДКОСТИ'}

@zh_admin_router.callback_query(lambda c: c.data == "add_zh")
async def zhizhi(callback_query: types.CallbackQuery):
    global number_zh
    global string_for_admins
    global number_zh_t
    global zh_type
    global prod
    await callback_query.message.answer(text = "Выберите производителя:", reply_markup=nalichie_keyboard_names(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha"), number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    prod = {'category': 'ЖИДКОСТИ'}
    number_zh = 10
    string_for_admins = ""
    number_zh_t = 10
    zh_type = ""

@zh_admin_router.callback_query(lambda c: c.data.startswith("z_"))
async def prods_lists(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    global zh_type
    string_for_admins += callback_query.data.split("z_")[1].replace("_", " ") + "0 MG ) "
    prod['name'] = f'{string_for_admins}'
    zh_type = callback_query.data.split("z_")[1]
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_admin(callback_query.data.split("z_")[1], number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_zh = 10

@zh_admin_router.callback_query(lambda c: c.data == ("next_zhizha_add"))
async def next_zhizha(callback_query: types.CallbackQuery):
    global number_zh
    number_zh += 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=nalichie_keyboard_names(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha"), number = number_zh))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_admin_router.callback_query(lambda c: c.data == ("back_zhizha_add"))
async def back_zhizha(callback_query: types.CallbackQuery):
    global number_zh
    number_zh -= 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=nalichie_keyboard_names(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha"), number = number_zh))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_admin_router.callback_query(lambda c: c.data == ("next_zh_t_add"))
async def next_zh_t(callback_query: types.CallbackQuery):
    global number_zh_t
    global zh_type
    number_zh_t += 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_admin(zh_type, number = number_zh_t))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_admin_router.callback_query(lambda c: c.data == ("back_zh_t_add"))
async def back_zh_t(callback_query: types.CallbackQuery):
    global number_zh_t
    global zh_type
    number_zh_t -= 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods_admin(zh_type, number = number_zh_t))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_admin_router.callback_query(lambda c: c.data.startswith("add_zh_"))
async def taste_list(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    global prod
    prod['name'] += f'({callback_query.data.split("add_zh_")[1].replace("_", " ")})'
    prod['name'] = prod['name'].replace("  ", " ")
    string_for_admins += callback_query.data.split("add_zh_")[1].replace("_", " ")
    # await callback_query.bot.send_message(chat_id="@predzakazyy", text=f"{callback_query.from_user.full_name}\n@{callback_query.from_user.username}"
    #                                                             f"\n{callback_query.from_user.id}\n{string_for_admins.replace("  "," ")}\n{datetime.now(tz = None)}")
    if not(os.path.exists(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json")):
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json", "w") as file:
            json.dump({"products":[prod]}, file, indent=4, ensure_ascii=False)
    else:
        with open(f"/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/nalichie/admin/keyboards/parsers/zhizha_v_nal/{prod['name'].split("(")[0].replace("  ", " ")}({prod['name'].split("(")[1][0:-1].replace("  ", " ")}.json", "r+") as file:
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