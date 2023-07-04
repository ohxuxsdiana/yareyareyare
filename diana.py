from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = AsyncTeleBot('6388793741:AAEeo692qmu59YBm5OjWEey3GE0GGqmsKyc')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    print(message)
    await bot.reply_to(message, 'Здравствуй, не понятный челик! ')


@bot.message_handler(commands=['home'])
async def send_welcome(message):
    await bot.reply_to(message, 'Привет! Я  JojoBot! И я буду тебе помогать в чем либо! ')


@bot.message_handler(commands=['game'])
async def send_welcome(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎲')


@bot.message_handler(commands=['film'])
async def send_m(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Лучшие фильмы века:/n1)Вызов/n2)Дюна/n3)Бэтмен')


@bot.message_handler(commands=['sticker'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_sicker(chat_id,'CAACAgIAAxkBAAIiVmSkDIhd9Z1DAiirZ7v4AzsAAdFWXgACMgEAApNA9g7Y4VKN6fnuNy8E')


@bot.message_handler(commands=['help'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_document(chat_id, open('text.txt', 'rb'))



@bot.message_handler(commands=['geographique'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id, 35.681732, 139.753925)


@bot.message_handler(commands=['photo'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_photo(chat_id,'https://i.ytimg.com/vi/ts9dBg4wBWE/maxresdefault.jpg?7857057827', caption='зе ээээнд')


@bot.message_handler(commands=['help'])
async def send_welcome(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    one_button = 'Первая кнопка'
    two_button = 'Вторая кнопка'
    three_button = 'Третья кнопка'
    markup.add(one_button, two_button, three_button, row_width=2)
    await bot.send_message(chat_id, 'Второй вариант кнопок ', reply_merkup=markup)


def generate_reply_keyboard(list_buttons, row):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_buttons, row_width=row)
    return markup


@bot.message_handler(commands=['help, start'])
async def send_welcome(message):
    chat_id = message.from_user.id
    list_buttons = 'Первая кнопка', 'Вторая кнопка', 'Третья кнопка'
    await bot.send_message(chat_id, 'торой вариянт кнопок', reply_markup=generate_reply_keyboard(list_buttons, 2))



@bot.message_handler(commands=['help,start'])
async def send_welcome(message):
    chat_id = message.from_user.id
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Перая кнопка ', callback_date = 'first')
    button2 = InlineKeyboardButton('Втораякнопка ', callback_date = 'second')
    button3 = InlineKeyboardButton('Третья кнопка ', callback_date = 'three')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    await bot.send_message(chat_id, 'Первый вариант кнопок', reply_markup=markup)



@bot.message_handler(func=lambda messange: True)
async def echo_messange(message):
    text_message = message.text
    text_message = text_message.lower()
    if 'дела' in text_message or 'настроение' in text_message:
        await bot.reply_to(message, 'всё запипись! У тебя?', )
    elif 'шутка' in text_message or 'анекдот' in text_message:
        await bot.reply_to(message, 'С увеличением градусов тупеют даже углы')
    else:
        await bot.reply_to(message, 'Эй, чел норм пиши, а то я тебя не понимаю')





import asyncio

asyncio.run(bot.polling())
