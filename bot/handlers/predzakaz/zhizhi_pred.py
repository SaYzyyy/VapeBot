from aiogram import types, Router
from .keyboards.predzakaz_keyboard_names import predzakaz_keyboard_names
from .keyboards.predzakaz_keyboard_prods import show_prods
from datetime import datetime
from .keyboards.start_keyboard import start_keyboard
import os

zh_pred_router = Router()

@zh_pred_router.callback_query(lambda c: c.data == "zhizhi")
async def zhizhi(callback_query: types.CallbackQuery):
    global number_zh
    global string_for_admins
    global number_zh_t
    global zh_type
    await callback_query.message.answer(text = "Выберите производителя:", reply_markup=predzakaz_keyboard_names(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/zhizha"), number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_zh = 10
    string_for_admins = ""
    number_zh_t = 10
    zh_type = ""

@zh_pred_router.callback_query(lambda c: c.data.startswith("p_"))
async def prods_lists(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    global zh_type
    string_for_admins += callback_query.data.split("p_")[1].replace("_", " ") + "0 MG ) "
    zh_type = callback_query.data.split("p_")[1]
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods(callback_query.data.split("p_")[1], number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_zh = 10

@zh_pred_router.callback_query(lambda c: c.data == ("next_zhizha"))
async def next_zhizha(callback_query: types.CallbackQuery):
    global number_zh
    number_zh += 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=predzakaz_keyboard_names(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/zhizha"), number = number_zh))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_pred_router.callback_query(lambda c: c.data == ("back_zhizha"))
async def back_zhizha(callback_query: types.CallbackQuery):
    global number_zh
    number_zh -= 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=predzakaz_keyboard_names(os.listdir(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/zhizha"), number = number_zh))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_pred_router.callback_query(lambda c: c.data == ("next_zh_t"))
async def next_zh_t(callback_query: types.CallbackQuery):
    global number_zh_t
    global zh_type
    number_zh_t += 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods(zh_type, number = number_zh_t))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_pred_router.callback_query(lambda c: c.data == ("back_zh_t"))
async def back_zh_t(callback_query: types.CallbackQuery):
    global number_zh_t
    global zh_type
    number_zh_t -= 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_prods(zh_type, number = number_zh_t))
    await callback_query.answer()
    await callback_query.message.delete()

@zh_pred_router.callback_query(lambda c: c.data.startswith("r_"))
async def taste_list(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_zh
    string_for_admins += callback_query.data.split("r_")[1].replace("_", " ")
    await callback_query.bot.send_message(chat_id="@predzakazyy", text=f"{callback_query.from_user.full_name}\n@{callback_query.from_user.username}"
                                                                f"\n{callback_query.from_user.id}\n{string_for_admins.replace("  "," ")}\n{datetime.now(tz = None)}")
    await callback_query.message.answer(text = f"Заказ {string_for_admins} принят! В ближайшее время с вами свяжется админ! 🕖 \n\nЕсли хотите что-то ещё, можете воспользоваться кнопками снизу:", reply_markup = start_keyboard())
    await callback_query.answer()
    await callback_query.message.delete()
    string_for_admins = ""
    number_zh = 10