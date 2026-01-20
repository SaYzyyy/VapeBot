from aiogram import types, Router
from keyboards.choose_pr_vn import first_choose
from handlers.start import number_zh, number_zh_t, number_odn, number_odn_t, string_for_admins, zh_type, odn_type, pod_type, number_pod, number_pod_t
from keyboards.start_keyboard import start_keyboard

want_router = Router()

@want_router.callback_query(lambda c: c.data == "predzakaz")
async def pred(callback_query: types.CallbackQuery):
    global number_zh
    global string_for_admins
    global number_zh_t
    global zh_type
    global number_odn
    global number_odn_t
    global odn_type
    global number_pod
    global number_pod_t
    global pod_type
    await callback_query.message.answer(text="Выберите что вам нужно:", reply_markup=first_choose())
    await callback_query.answer()
    await callback_query.message.delete()
    number_zh = 10
    string_for_admins = ""
    number_zh_t = 10
    zh_type = ""
    number_odn = 10
    number_odn_t = 10
    odn_type = ""
    pod_type = ""
    number_pod = 10
    number_pod_t = 10

@want_router.callback_query(lambda c: c.data == "back_to_choose")
async def back_to_choose(callback_query: types.CallbackQuery):
    global number_zh
    global string_for_admins
    global number_zh_t
    global zh_type
    global number_odn
    global number_odn_t
    global odn_type
    global number_pod
    global number_pod_t
    global pod_type
    await callback_query.message.answer(text="Хорошо! Выберите наличие: ", reply_markup=start_keyboard())
    await callback_query.answer()
    await callback_query.message.delete()
    number_zh = 10
    string_for_admins = ""
    number_zh_t = 10
    zh_type = ""
    number_odn = 10
    number_odn_t = 10
    odn_type = ""
    pod_type = ""
    number_pod = 10
    number_pod_t = 10