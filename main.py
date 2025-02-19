import asyncio
import logging
import sys
import config
import random
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import Message
from aiogram import F


TOKEN = config.BOT_TOKEN

dp = Dispatcher()

chars = [

    charSmalLetters := [],
    charBigLetters := [],
    charNumbers := ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    charSpecs := ["!", "@", "$", "%", "#", "&", "*"],

]

for i in "qwertyuiopasdfghjklzxcvbnm":

    charSmalLetters.append(i)

for i in "QWERTYUIOPASDFGHJKLZXCVBNM":

    charBigLetters.append(i)


def PasswordGenerate(difficulty):

    endPassword = ""
    password = ""

    if difficulty == "easy":

        for i in range(random.randrange(3, 4)):
            password += random.choice(chars[0])
        for i in range(random.randrange(3, 4)):
            password += random.choice(chars[1])
        for i in range(random.randrange(3, 4)):
            password += random.choice(chars[2])

    else:

        for i in range(random.randrange(3, 4)):
            password += random.choice(chars[0])
        for i in range(random.randrange(3, 4)):
            password += random.choice(chars[1])
        for i in range(random.randrange(3, 4)):
            password += random.choice(chars[2])
        for i in range(random.randrange(3, 4)):
            password += random.choice(chars[3])

    password = list(password)
    random.shuffle(password)

    for i in password:
        endPassword += i

    return(endPassword)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Легкий")],
        [types.KeyboardButton(text="Сложный")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Каокй пароль сгенерировать?")


    await message.answer("Какой пароль создать?", reply_markup=keyboard)


@dp.message(F.text.lower() == "легкий")
async def easy(message: types.Message):
    password = PasswordGenerate("easy")
    await message.answer("Пароль: <tg-spoiler>" + password + "</tg-spoiler>", parse_mode="HTML")

@dp.message(F.text.lower() == "сложный")
async def hard(message: types.Message):
    password = PasswordGenerate("hard")
    await message.answer("Пароль: <tg-spoiler>" + password + "</tg-spoiler>", parse_mode="HTML")

@dp.message()
async def echo_handler(message: Message) -> None:
    kb = [
        [types.KeyboardButton(text="Легкий")],
        [types.KeyboardButton(text="Сложный")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Каокй пароль сгенерировать?")


    await message.answer("Какой пароль создать?", reply_markup=keyboard)


async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
