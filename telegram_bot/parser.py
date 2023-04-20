import telebot
# from telethon import TelegramClient, client, events
# from telethon.tl.functions.channels import GetDialogsRequest
# from telethon.tl.types import InputChannel, InputMessagesFilterEmpty
#
#
#
# # функция для отправки сообщений в чат с пользователем
# def send_message(chat_id, message):
#     bot.send_message(chat_id, message)
#
#
# # функция-обработчик новых сообщений во всех каналах
# @client.on(events.NewMessage(chats=('')))
# async def handle_new_message(event):
#     # проверяем, содержит ли сообщение ключевые слова
#     if 'Анталия' in event.message.message or 'сниму' in event.message.message:
#         # отправляем найденное сообщение в чат с пользователем
#         send_message(USER_CHAT_ID, event.message.message)
#
#
# # запускаем клиента Telethon
# client = TelegramClient('session_name', api_id, api_hash)
# client.start()
#
# # запускаем бота
# bot.polling()
