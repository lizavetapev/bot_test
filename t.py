import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token='8542565226:AAHF2O4baKJz_LVCJCRe8DqqjpCpWK3Wopo')
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Open web page', web_app = WebAppInfo(url = 'https://itproger.com/telegram.html'))]
        ], resize_keyboard=True, 
        one_time_keyboard=True
        )
    #markup.add(types.KeyboardButton('Открыть веб страницу', web_app = WebAppInfo(url = 'https://itproger.com')))
    await message.answer('Hello, my friend', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

# async def main():
#     await dp.start_polling(bot)