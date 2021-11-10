from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.utils import executor
from create_bot import dp,bot
from handlers import menu_handlers
from handlers import process_handlers
from aiogram.dispatcher import FSMContext


async def on_startup(_):
    print("All systems online")
    
   


menu_handlers.register_handlers_menu(dp)
process_handlers.register_handlers_process(dp)

executor.start_polling(dp,skip_updates=True,on_startup=on_startup)









