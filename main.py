import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


button_happyburthday = KeyboardButton('С днем рождения')
button_happy_anniversary = KeyboardButton('С юбилеем')
button_for_the_wedding = KeyboardButton('На свадьбу')
button_wedding_anniversaries = KeyboardButton('Годовщины свадеб')
button_important_events = KeyboardButton('Важные события')
button_ioved = KeyboardButton('Любимым')
button_holidays = KeyboardButton('Праздники')
button_universal = KeyboardButton('Универсальные')
button_by_name = KeyboardButton('По именам')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_happyburthday)
greet_kb.add(button_happy_anniversary)
greet_kb.add(button_for_the_wedding)
greet_kb.add(button_wedding_anniversaries)
greet_kb.add(button_important_events)
greet_kb.add(button_ioved)
greet_kb.add(button_holidays)
greet_kb.add(button_universal)
greet_kb.add(button_by_name)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Здравствуйте! Вас приветствует бот-поздравлений.")
    await message.answer("Выберете категорию", reply_markup=greet_kb)

if __name__ == '__main__':
    executor.start_polling(dp)