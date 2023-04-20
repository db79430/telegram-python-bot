from this import d

import telebot
from telethon import TelegramClient, sync, events

bot = telebot.TeleBot('TOKEN')
api_id = 'ID'
api_hash = 'HASH'
client = TelegramClient('session_name', api_id, api_hash)


# функция для отправки сообщений в чат с пользователем
def send_message(chat_id, message):
    bot.send_message(chat_id, message)


# функция-обработчик новых сообщений во всех каналах
@client.on(events.NewMessage(chats=('')))
async def handle_new_message(event):
    # проверяем, содержит ли сообщение ключевые слова
    if 'Анталия' in event.message.message or 'сдам' in event.message.message or 'Аренда' in event.message.message:
        # отправляем найденное сообщение в чат с пользователем
        send_message(chat_id, event.message.message)


# запускаем клиента Telethon
client = TelegramClient('session_name', api_id, api_hash)
client.start()

# запускаем бота
bot.polling()
