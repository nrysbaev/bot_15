from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
