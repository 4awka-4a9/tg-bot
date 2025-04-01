#BTC - bc1qml9r2f7qud0zsatjf3kh4c6v9yetd8zer52t97
#ETH - 0xc3006CD922641337053BfB34a919299754002Fa6
#TETHER USD TRON NETWORK - TJ1Zc5Y2SsNLMaQKzdy9XFT5iLAZHx7zGZ
#TETHER USD ETHEREUM NETWORK - 0xc3006CD922641337053BfB34a919299754002Fa6

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
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


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

        for i in range(random.randrange(3, 5)):
            password += random.choice(chars[0])
        for i in range(random.randrange(3, 5)):
            password += random.choice(chars[1])
        for i in range(random.randrange(3, 5)):
            password += random.choice(chars[2])

    else:

        for i in range(random.randrange(3, 5)):
            password += random.choice(chars[0])
        for i in range(random.randrange(3, 5)):
            password += random.choice(chars[1])
        for i in range(random.randrange(3, 5)):
            password += random.choice(chars[2])
        for i in range(random.randrange(3, 5)):
            password += random.choice(chars[3])

    password = list(password)
    random.shuffle(password)

    for i in password:
        endPassword += i

    return(endPassword)

def PasswordReturn():
    types.easyButton = InlineKeyboardButton(text="Легкий")
    types.hardButton = InlineKeyboardButton(text="Сложный")

    keyboard = InlineKeyboardMarkup(input_field_placeholder="Какой пароль сгенерировать?", resize_keyboard=True)
    #keyboard.row(easyButton, hardButton)
    keyboard.add(easyButton)
    keyboard.add(hardButton)
    return(keyboard)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = PasswordReturn()

    await message.answer("Какой пароль создать?", reply_markup=keyboard)

@dp.message(Command('about'))
async def cmd_start(message: Message):

    await message.answer('Этот телеграм-бот был создан мною в 15 лет! Он достаточно простой, тут всего 2 режима: Легкий пароль который в длинну 9-12 символов, он содержит большие и маленькие буквы а также цифры. Длинный пароль в длинну 12-20 символов и к нему добавляются спец-символы.')

@dp.message(Command('generate_password'))
async def cmd_start(message: Message):
    keyboard = PasswordReturn()

    await message.answer("Какой пароль создать?", reply_markup=keyboard)

@dp.message(Command('donate'))
async def cmd_start(message: Message):

    await message.answer('Привет! Этот проект я разработал в свои 15 лет!!! Я начинающий программист и нуждаюсь в поддержке. Если тебе не жалко то можеш задонатить мне. Вот мои адреса криптокошельков:\nBTC - bc1qml9r2f7qud0zsatjf3kh4c6v9yetd8zer52t97\nETH - 0xc3006CD922641337053BfB34a919299754002Fa6\nUSDT TRC 20 - TJ1Zc5Y2SsNLMaQKzdy9XFT5iLAZHx7zGZ\nUSDT ERC 20 - 0xc3006CD922641337053BfB34a919299754002Fa6\n https://github.com/4awka-4a9 ')

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
    keyboard = PasswordReturn()

    await message.answer("Какой пароль создать?", reply_markup=keyboard)



async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
