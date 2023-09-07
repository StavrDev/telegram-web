from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

class TgBot:
    def __init__(self, token):
        bot = Bot(token)
        self.dp = Dispatcher(bot)

        async def Start(message: types.Message):
            await message.answer('Привет!\nДля введи то что хочешь найти в Википедия')

        async def Search(message:types.Message):
            message_text = message.text
            btn1 = InlineKeyboardButton("Веб-приложение", web_app=WebAppInfo(url = f'https://ru.wikipedia.org/wiki/{message_text}'))
            keyboard = InlineKeyboardMarkup().add(btn1)
            await message.answer("Переходи по ссылке и читай!", reply_markup=keyboard)

        self.dp.register_message_handler(Start, commands=['start'])
        self.dp.register_message_handler(Search)
    
    def start(self):
        executor.start_polling(self.dp, skip_updates=True)