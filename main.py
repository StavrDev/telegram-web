import config as c
from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo


bot = Bot(c.TOKEN_BOT)
dp = Dispatcher(bot)

async def Start(message: types.Message):
    await message.answer('Привет!\nДля введи то что хочешь найти в Википедия')

async def Search(message:types.Message):
    message_text = message.text
    btn1 = InlineKeyboardButton("Веб-приложение", web_app=WebAppInfo(url = f'https://ru.wikipedia.org/wiki/{message_text}'))
    keyboard = InlineKeyboardMarkup().add(btn1)
    await message.answer("Переходи по ссылке и читай!", reply_markup=keyboard)

dp.register_message_handler(Start, commands=['start'])
dp.register_message_handler(Search)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)