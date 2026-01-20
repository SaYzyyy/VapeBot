from aiogram import types, Router
from keyboards.predzakaz_keyboard_names_odn import predzakaz_keyboard_names as pred_odn
from keyboards.predzakaz_keyboard_prods_odn import show_prods as show_odn
from datetime import datetime
from keyboards.start_keyboard import start_keyboard
from handlers.start import number_odn, number_odn_t, string_for_admins, odn_type
import os

odn_pred_router = Router()

@odn_pred_router.callback_query(lambda c: c.data == "odnorazki")
async def odnorazki(callback_query: types.CallbackQuery):
    global number_odn
    global string_for_admins
    global number_odn_t
    global odn_type
    await callback_query.message.answer(text="Выберите производителя:", reply_markup=pred_odn(
        os.listdir("../parsers/odnorazki"), number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_odn = 10
    string_for_admins = ""
    number_odn_t = 10
    odn_type = ""


@odn_pred_router.callback_query(lambda c: c.data.startswith("o_"))
async def prods_lists_odn(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_odn
    global odn_type
    odn_type = callback_query.data.split("o_")[1]
    string_for_admins += callback_query.data.split("o_")[1].replace("_", " ")+ "0 MG ) " + " "
    await callback_query.message.answer(text="Выберите вкус:",
                                        reply_markup=show_odn(callback_query.data.split("o_")[1], number_o = 10))
    await callback_query.answer()
    await callback_query.message.delete()


@odn_pred_router.callback_query(lambda c: c.data == ("next_odn"))
async def next_odn(callback_query: types.CallbackQuery):
    global number_odn
    number_odn += 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=pred_odn(os.listdir(
        "../parsers/odnorazki"), number=number_odn))
    await callback_query.answer()
    await callback_query.message.delete()


@odn_pred_router.callback_query(lambda c: c.data == ("back_odn"))
async def back_odn(callback_query: types.CallbackQuery):
    global number_odn
    number_odn -= 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=pred_odn(os.listdir(
        "../parsers/odnorazki"), number=number_odn))
    await callback_query.answer()
    await callback_query.message.delete()


@odn_pred_router.callback_query(lambda c: c.data == ("next_odn_t"))
async def next_odn_t(callback_query: types.CallbackQuery):
    global number_odn_t
    global odn_type
    number_odn_t += 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_odn(odn_type, number_o = number_odn_t))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_pred_router.callback_query(lambda c: c.data == ("back_odn_t"))
async def back_odn_t(callback_query: types.CallbackQuery):
    global number_odn_t
    global odn_type
    number_odn_t -= 10
    await callback_query.message.answer(text = "Выбеите вкус:", reply_markup=show_odn(odn_type, number_o = number_odn_t))
    await callback_query.answer()
    await callback_query.message.delete()

@odn_pred_router.callback_query(lambda c: c.data.startswith("or_"))
async def taste_list_odn(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_odn
    string_for_admins += callback_query.data.split("or_")[1].replace("_", " ")
    await callback_query.bot.send_message(chat_id="@predzakazyy",
                                          text=f"{callback_query.from_user.full_name}\n@{callback_query.from_user.username}"
                                               f"\n{callback_query.from_user.id}\n{string_for_admins.replace("  ", " ")}\n{datetime.now(tz=None)}")
    await callback_query.message.answer(text=f"Заказ {string_for_admins} принят! В ближайшее время с вами свяжется админ! 🕖 \n\nЕсли хотите что-то ещё, можете воспользоваться кнопками снизу:", reply_markup = start_keyboard())
    await callback_query.answer()
    await callback_query.message.delete()
    string_for_admins = ""
    number_odn = 10