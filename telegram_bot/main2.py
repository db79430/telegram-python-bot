from unittest.mock import call

# import telebot
# from telebot import types
#
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Вас приветствует чат-бот Houser Bot!Мы поможем вам найти клиентов через '
#                                       'целевые каналы в Telegram и Facebook.')
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     item1 = types.KeyboardButton('Да, давай')
#     item2 = types.KeyboardButton('Спасибо, не надо')
#     markup.add(item1, item2)
#     bot.send_message(message.chat.id, 'Чтобы начать, нам необходимо настроить категории поиска. Не переживайте - их '
#                                       'можно перенастроить в любой момент. После выбора категории поиска бот начнет '
#                                       'отслеживать релевантные предложения и высылать их в этот чат. Это может занять '
#                                       'некоторое время - в зависимости от появления новых запросов, подходящих под '
#                                       'ваши критерии поиска. Ну что, приступим?.', reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: True)
# def func(message):
#     if (message.text == "Спасибо, не надо"):
#         bot.send_message(message.chat.id, text="Очень жаль, но мы ждем тебя снова")
#     elif message.text == "Да, давай":
#         markupButton = types.InlineKeyboardMarkup(row_width=2)
#         buttons = [
#             types.InlineKeyboardButton("Анталья", callback_data='button1'),
#             types.InlineKeyboardButton("Стамбул", callback_data='button2'),
#             types.InlineKeyboardButton("Аланья", callback_data='button1'),
#             types.InlineKeyboardButton("Мерсин", callback_data='button1'),
#             types.InlineKeyboardButton("Кемер", callback_data='button1'),
#             types.InlineKeyboardButton("Демирташ", callback_data='button1'),
#             types.InlineKeyboardButton("Газипаша", callback_data='button1'),
#             types.InlineKeyboardButton("Сиде", callback_data='button1')
#         ]
#         back = types.InlineKeyboardButton("Вернуться в главное меню")
#         markupButton.add(*buttons, back)
#         bot.send_message(message.chat.id, text="Выберите локации, по которым мы начнем наш поиск:",
#                          reply_markup=markupButton)
#
#         # регистрируем обработчик для следующего сообщения
#         bot.register_next_step_handler(message, process_buttons)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def process_buttons(call):
#     if call.data == 'button1':
#         buttons_rent = [
#             types.InlineKeyboardButton("Поиск арендаторов"),
#             types.InlineKeyboardButton("Поиск арендодателей"),
#             types.InlineKeyboardButton("Поиск продавцов"),
#             types.InlineKeyboardButton("Поиск покупателей"),
#
#         ]
#     markupRent = types.InlineKeyboardMarkup()
#     markupRent.add(*buttons_rent)
#     selected_buttons = call.text.split(', ')
#     bot.send_message(call.chat.id, 'Вы выбрали: ' + ', '.join(selected_buttons) + 'Отлично! Теперь выберите '
#                                                                                   'типы запросов, которые вас '
#                                                                                   'интересуют:',
#                      reply_markup=markupRent)
#     bot.register_next_step_handler(call, message_settings_end)
#
#
# def message_settings_end(message):
#     markupButton = types.InlineKeyboardMarkup(row_width=2)
#     back = types.KeyboardButton("Вернуться в главное меню")
#     markupButton.add(back)
#     bot.send_message(message.chat.id, 'Настройка завершена! Релевантные запросы будут появляться в '
#                                       'этом чате. Это может занять от нескольких минут до '
#                                       'нескольких часов.  Поменять настройки поиска можно в '
#                                       'Главном меню. /menu')
#
#
# bot.polling()
