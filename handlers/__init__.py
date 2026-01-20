from aiogram import Dispatcher
from handlers.start import start_router
from handlers.predzakaz.predzakaz import want_router
from handlers.predzakaz.zhizhi_pred import zh_pred_router
from handlers.predzakaz.odn_pred import odn_pred_router
from handlers.predzakaz.pod_pred import pod_pred_router
def Register_Routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(want_router)
    dp.include_router(zh_pred_router)
    dp.include_router(odn_pred_router)
    dp.include_router(pod_pred_router)