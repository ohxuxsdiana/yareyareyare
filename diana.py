from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('6388793741:AAEeo692qmu59YBm5OjWEey3GE0GGqmsKyc')
@bot.message_handler(commands = ['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Приветствую тебя, новый пользователь!')

@bot.message_handler(commands = ['home'])
async def send_welcome(message):
    await bot.reply_to(message, 'Привет! Нажми старт, чтобы начать активность бота ')
@bot.message_handler(func=lambda messange: True)
async def echo_messange(message):
    text_message = message.text
    text_message = text_message.lower()
    if 'дела' in text_message or 'настроение' in text_message:
        await bot.reply_to(message, 'хорошо,  у тебя',)
    elif 'шутка' in text_message or 'анекдот' in text_message:
        await bot.reply_to(message, 'Колобок повесился')
    else:
        await bot.reply_to(message, 'Извините, я вас не поняла')


import asyncio
asyncio.run(bot.polling())
