from aiogram import F, types, Router
from aiogram.filters import Command
from .keyboards.start_keyboard import start_keyboard
from bot.handlers.nalichie.admin.keyboards.keyboard_nalichie_admin_start import first_choose_admin
from bot.handlers.nalichie.user.keyboards.nalichie_keyboard_user import first_choose_user
from aiogram.types import FSInputFile
# import os

string_for_admins = ""
number_zh = 10
number_zh_t = 10
zh_type = ""
number_odn = 10
number_odn_t = 10
odn_type = ""
number_pod = 10
number_pod_t = 10
pod_type = ""


start_router = Router()

@start_router.message(Command(commands = ["start"]))
async def Hello(message: types.Message):
    global number_odn
    global string_for_admins
    global number_zh
    global zh_type
    global number_zh_t
    global odn_type
    global number_odn_t
    global pod_type
    global number_pod
    global number_pod_t
    await message.answer_photo(photo = FSInputFile("/Users/sayzyyy/PycharmProjects/VapeBot/bot/handlers/logo.png"), caption ="ЗДРАВСТВУЙТЕ! 👋\nВы зашли в телеграм-бота вейп-шопа STREET CLOUDS! \n\nЗдесь вы можете ознакомиться с товаром в наличии, "
                         "а также оформить предзаказ того, что вы хотите! 🥵\n\nЧтобы оформить предзаказ нажмите кнопку ПРЕДЗАКАЗ 🕓.\n"
                         "Чтобы посмотреть товары в наличии, нажмите кнопку В НАЛИЧИИ 👇.", reply_markup=start_keyboard())
    number_zh = 10
    string_for_admins = ""
    number_zh_t = 10
    zh_type = ""
    number_odn = 10
    number_odn_t = 10
    odn_type = ""
    number_pod = 10
    number_pod_t = 10
    pod_type = ""

@start_router.callback_query(lambda c: c.data == "admin")
async def admin(callback_query: types.CallbackQuery):
    if callback_query.from_user.username in ["ggyf0", "NotSaYzyyy"]:
        await callback_query.message.answer(text = "Вы вошли в админ-панель. Чтобы добавить товар, выберите категорию, затем товар и вкус/цвет:", reply_markup=first_choose_admin())
        await callback_query.answer()
        await callback_query.message.delete()






@start_router.callback_query(lambda c: c.data == "v_nalichii")
async def buy(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = "Выберите тип:", reply_markup=first_choose_user())
    await callback_query.answer()
    await callback_query.message.delete()