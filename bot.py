from aiogram import Bot, Dispatcher, types, executor
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5897660885:AAEr_ne_UKV110wB8BjlYB_QyL-TK27nW30")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', 'salom'])
async def bot_start(message: types.Message):
    if message.text == '/start':
        await message.answer('Hello Welcome\nThis is My Bot ^_~ ___ 😊')
    elif message.text == '/salom':
        await message.answer('Valeykum Assalom ...')
    else:
        await message.answer('Bu bot 3 ta commandasi bor\n'
                             '1 - /start\n2 - /help\n3 - /salom\n'
                             'Bu botga siz:\n'
                             'rasm -> desangiz rasm chiqaradi\n'
                             'video -> desangiz kichik video chiqaradi\n'
                             'audio -> desangiz audio chiqaradi\n'
                             'voice -> desangiz voice chiqaradi\n')


@dp.message_handler()
async def text_handler(message: types.Message):
    if message.text == 'rasm':
        file = open('img.png', 'rb')
        await bot.send_photo(message.chat.id, file, 'This is photo')
    elif message.text == 'video':
        file2 = open('video.mp4', 'rb')
        await bot.send_video(message.chat.id, file2)
    elif message.text == 'audio':
        file3 = open('audio.ogg', 'rb')
        await bot.send_audio(message.chat.id, file3, 'This is audio')
    elif message.text == 'voice':
        file4 = open('audio_2023-01-24_22-51-07.ogg', 'rb')
        await bot.send_audio(message.chat.id, file4, 'This is voice')
    else:
        place = ''
        for i in message.text:
            place += str(chr(ord(i) + 2))
        await message.answer(place)

executor.start_polling(dp, skip_updates=False)
