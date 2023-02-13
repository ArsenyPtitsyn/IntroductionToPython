from bot import dp
import handlers
from aiogram.utils import executor

handlers.register_handlers(dp)
executor.start_polling(dp, skip_updates=True)
