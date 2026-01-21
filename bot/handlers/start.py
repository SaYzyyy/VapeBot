from aiogram import types, Router
from aiogram.filters import Command
from .keyboards.start_keyboard import start_keyboard
from .keyboards.buy_keyboard import buy_keyboard
from aiogram.types import FSInputFile
import os

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
    # await message.answer(text ="ЗДРАВСТВУЙТЕ! 👋\nВы зашли в телеграм-бота вейп-шопа STREET CLOUDS! \n\nЗдесь вы можете ознакомиться с товаром в наличии, "
    #                      "а также оформить предзаказ того, что вы хотите! 🥵\n\nЧтобы оформить предзаказ нажмите кнопку ПРЕДЗАКАЗ 🕓.\n"
    #                      "Чтобы посмотреть товары в наличии, нажмите кнопку В НАЛИЧИИ 👇.", reply_markup=start_keyboard())
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





















@start_router.callback_query(lambda c: c.data == "v_nalichii")
async def buy(callback_query: types.CallbackQuery):
    if os.path.exists("/db/names.txt"):
        with open("/db/names.txt", "r") as f:
            await callback_query.message.answer(text = "Нажмите на кнопку с названием товара, который вы хотите.", reply_markup=buy_keyboard(f.readlines()))
            await callback_query.answer()
            await callback_query.message.delete()