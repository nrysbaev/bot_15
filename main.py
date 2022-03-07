from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello, my master {message.from_user.full_name}')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    question = "By whom invented Python"
    answers = ["Harry Potter", "Voldemort", "Guido Van Rossum", "Linus Torvalds"]
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,
                        explanation='This is easy, not gonna tell you',
                        explanation_parse_mode=ParseMode.MARKDOWN_V2)


@dp.message_handler(commands=['problem'])
async def problem_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('След задача',
                                         callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'Output:'
    answers = [0.0, 4, 0, 8, 8.0, "Error"]
    # Add photo!
    photo = open('media/', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answers,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


@dp.callback_query_handlers(lambda func: func.data == 'button_call_1')
async def problem_2(call: types.CallbackQuery):
    question = 'Output:'
    answers = ['1', '2', '3', '4', '5', '6', '7']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=2,
        is_anonymous=False,
        type='quiz'
    )


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)


if __name__ == "main":
    executor.start_polling(dp, skip_updates=False)
