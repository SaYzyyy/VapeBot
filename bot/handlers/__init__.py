from aiogram import Dispatcher
from bot.handlers.start import start_router
from bot.handlers.predzakaz.predzakaz import want_router
from bot.handlers.predzakaz.zhizhi_pred import zh_pred_router
from bot.handlers.predzakaz.odn_pred import odn_pred_router
from bot.handlers.predzakaz.pod_pred import pod_pred_router
from bot.handlers.nalichie.admin.zhizhi_admin import zh_admin_router
from bot.handlers.nalichie.user.zhizhi_user import zh_user_router
from bot.handlers.nalichie.admin.odn_admin import odn_admin_router
from bot.handlers.nalichie.user.odn_user import odn_user_router
def Register_Routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(want_router)
    dp.include_router(zh_pred_router)
    dp.include_router(odn_pred_router)
    dp.include_router(pod_pred_router)
    dp.include_router(zh_admin_router)
    dp.include_router(zh_user_router)
    dp.include_router(odn_admin_router)
    dp.include_router(odn_user_router)