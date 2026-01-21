from aiogram import types, Router
from .keyboards.start_keyboard import start_keyboard
from .keyboards.predzakaz_keyboard_names_pod import show_prods_pods
from .keyboards.predzakaz_keyboard_prods_pod import show_prods_pod_c
from datetime import datetime

pod_pred_router = Router()

@pod_pred_router.callback_query(lambda c: c.data == "pods")
async def pods(callback_query: types.CallbackQuery):
    global number_pod
    global string_for_admins
    global number_pod_t
    global pod_type
    await callback_query.message.answer(text="Выберите название под-системы:", reply_markup=show_prods_pods("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/new_category2.json", number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_pod = 10
    string_for_admins = ""
    number_pod_t = 10
    pod_type = ""

@pod_pred_router.callback_query(lambda c: c.data.startswith("pod_"))
async def pods_lists(callback_query: types.CallbackQuery):
    global string_for_admins
    global number_pod
    global pod_type
    string_for_admins += callback_query.data.split("pod_")[1].replace("_", " ")
    pod_type = callback_query.data.split("pod_")[1]
    await callback_query.message.answer(text = "Выберите цвет:", reply_markup=show_prods_pod_c(callback_query.data.split("pod_")[1], number = 10))
    await callback_query.answer()
    await callback_query.message.delete()
    number_pod = 10

@pod_pred_router.callback_query(lambda c: c.data == ("next_pod"))
async def next_pod(callback_query: types.CallbackQuery):
    global number_pod
    number_pod += 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=show_prods_pods(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/new_category2.json", number = number_pod))
    await callback_query.answer()
    await callback_query.message.delete()

@pod_pred_router.callback_query(lambda c: c.data == ("back_pod"))
async def back_pod(callback_query: types.CallbackQuery):
    global number_pod
    number_pod -= 10
    await callback_query.message.answer(text="Выбеите производителя:", reply_markup=show_prods_pods(
        "/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/predzakaz/keyboards/parsers/new_category2.json", number = number_pod))
    await callback_query.answer()
    await callback_query.message.delete()

@pod_pred_router.callback_query(lambda c: c.data == ("next_pod_t"))
async def next_pod_t(callback_query: types.CallbackQuery):
    global number_pod_t
    global pod_type
    number_pod_t += 10
    await callback_query.message.answer(text = "Выбеите цвет:", reply_markup=show_prods_pod_c(pod_type, number = number_pod_t))
    await callback_query.answer()
    await callback_query.message.delete()

@pod_pred_router.callback_query(lambda c: c.data == ("back_pod_t"))
async def back_pod_t(callback_query: types.CallbackQuery):
    global number_pod_t
    global pod_type
    number_pod_t -= 10
    await callback_query.message.answer(text = "Выбеите цвет:", reply_markup=show_prods_pod_c(pod_type, number = number_pod_t))
    await callback_query.answer()
    await callback_query.message.delete()

@pod_pred_router.callback_query(lambda c: c.data.startswith("podc_"))
async def pod_col(callback_query: types.CallbackQuery):
    global string_for_admins
    string_for_admins += " " + callback_query.data.split("podc_")[1].replace("_", " ")
    await callback_query.bot.send_message(chat_id="@predzakazyy",
                                          text=f"{callback_query.from_user.full_name}\n@{callback_query.from_user.username}"
                                               f"\n{callback_query.from_user.id}\n{string_for_admins.replace("  ", " ")}\n{datetime.now(tz=None)}")
    await callback_query.message.answer(text=f"Заказ {string_for_admins} принят! В ближайшее время с вами свяжется админ! 🕖 \n\nЕсли хотите что-то ещё, можете воспользоваться кнопками снизу:", reply_markup = start_keyboard())
    await callback_query.answer()
    await callback_query.message.delete()
    string_for_admins = ""