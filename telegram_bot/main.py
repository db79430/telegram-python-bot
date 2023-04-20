# import telebot
# import time
# from telebot import types
#
#
# bot = telebot.TeleBot('6085981384:AAE2PiPHjBds1oE4lPwZsxj1QXf1qeuKqG0')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, '👋 Вас приветствует чат-бот Houser Bot!'
#                                       '🏡 Мы поможем вам найти клиентов через целевые каналы в Telegram и Facebook.')
#     buttons_start = [
#         types.InlineKeyboardButton('Да, давай', callback_data='yes'),
#         types.InlineKeyboardButton('Спасибо, не надо', callback_data='no'),
#     ]
#     markup_start = types.InlineKeyboardMarkup(row_width=2)
#     markup_start.add(*buttons_start)
#     bot.send_message(message.chat.id, 'ℹ️ Чтобы начать, нам необходимо настроить категории поиска. Не переживайте - их '
#                                       'можно перенастроить в любой момент. После выбора категории поиска бот начнет '
#                                       'отслеживать релевантные предложения и высылать их в этот чат. Это может занять '
#                                       'некоторое время - в зависимости от появления новых запросов, подходящих под '
#                                       'ваши критерии поиска. Ну что, приступим?  или введите команду /settings', reply_markup=markup_start)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler_start(call):
#     if call.data == 'no':
#         bot.send_message(call.message.chat.id, 'Очень жаль, но мы всегда ждем Вас снова')
#         bot.stop_polling()
#     elif call.data == 'yes':
#         buttons_city = [
#             types.InlineKeyboardButton('Анталия', callback_data='antalya'),
#             types.InlineKeyboardButton('Кемер', callback_data='kemer'),
#             types.InlineKeyboardButton("Аланья", callback_data='alanya'),
#             types.InlineKeyboardButton("Мерсин", callback_data='mersin'),
#             types.InlineKeyboardButton("Стамбул", callback_data='istambul'),
#             types.InlineKeyboardButton("Демирташ", callback_data='dzemitrash'),
#             types.InlineKeyboardButton("Газипаша", callback_data='gezipasha'),
#             types.InlineKeyboardButton("Сиде", callback_data='side')
#         ]
#         buttons_category = [
#             types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords'),
#             types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants'),
#             types.InlineKeyboardButton('Поиск продавцов', callback_data='rents'),
#             types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers')
#         ]
#         markup_city = telebot.types.InlineKeyboardMarkup(row_width=2)
#         markup_city.add(*buttons_city)
#         bot.send_message(call.message.chat.id, 'Выберите локации, по которым мы начнем наш поиск:',
#                                      reply_markup=markup_city)
#         markup_category = types.InlineKeyboardMarkup(row_width=1)
#         markup_category.add(*buttons_category)
#
#     bot.register_next_step_handler(call, callback_handler_city)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler_city(call):
#     if call.data == 'antalya':
#         bot.send_message(call.message.chat.id, 'Вы выбрали город Анталия')
#         buttons_category = [
#             types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords_antalya'),
#             types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants_antalya'),
#             types.InlineKeyboardButton('Поиск продавцов', callback_data='rents_antalya'),
#             types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers_antalya')
#         ]
#         markup_category = types.InlineKeyboardMarkup(row_width=1)
#         markup_category.add(*buttons_category)
#         bot.send_message(call.message.chat.id, 'Отлично! Теперь выберите типы запросов, которые вас интересуют:',
#                          reply_markup=markup_category)
#     elif call.data == 'kemer':
#         bot.answer_callback_query(call.id)
#         bot.send_message(call.message.chat.id, 'Вы выбрали город Кемер')
#         buttons_category = [
#             types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords_kemer'),
#             types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants_kemer'),
#             types.InlineKeyboardButton('Поиск продавцов', callback_data='rents_kemer'),
#             types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers_kemer')
#         ]
#         markup_category = types.InlineKeyboardMarkup(row_width=1)
#         markup_category.add(*buttons_category)
#         bot.send_message(call.message.chat.id, 'Отлично! Теперь выберите типы запросов, которые вас интересуют:',
#                          reply_markup=markup_category)
#     elif call.data == 'alanya':
#         bot.answer_callback_query(call.id)
#         bot.send_message(call.message.chat.id, 'Вы выбрали город Кемер')
#         buttons_category = [
#             types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords_alanya'),
#             types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants_alanya'),
#             types.InlineKeyboardButton('Поиск продавцов', callback_data='rents_alanya'),
#             types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers_alanya')
#         ]
#         markup_category = types.InlineKeyboardMarkup(row_width=1)
#         markup_category.add(*buttons_category)
#         bot.send_message(call.message.chat.id, 'Отлично! Теперь выберите типы запросов, которые вас интересуют:',
#                          reply_markup=markup_category)
#     elif call.data == 'mersin':
#         bot.answer_callback_query(call.id)
#         bot.send_message(call.message.chat.id, 'Вы выбрали город Кемер')
#         buttons_category = [
#             types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords_mersin'),
#             types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants_mersin'),
#             types.InlineKeyboardButton('Поиск продавцов', callback_data='rents_mersin'),
#             types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers_mersin')
#         ]
#         markup_category = types.InlineKeyboardMarkup(row_width=1)
#         markup_category.add(*buttons_category)
#         bot.send_message(call.message.chat.id, 'Отлично! Теперь выберите типы запросов, которые вас интересуют:',
#                          reply_markup=markup_category)
#
#     elif call.data.startswith('landlords'):
#         bot.answer_callback_query(call.id)
#         city = call.data.split('-')[1]
#         bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск арендодателей" в городе {city}')
#     elif call.data.startswith('tenants'):
#         bot.answer_callback_query(call.id)
#         city = call.data.split('-')[1]
#         bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск арендаторов" в городе {city}')
#     elif call.data.startswith('rents'):
#         bot.answer_callback_query(call.id)
#         city = call.data.split('-')[1]
#         bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск продавцов" в городе {city}')
#     elif call.data.startswith('buyers'):
#         bot.answer_callback_query(call.id)
#         city = call.data.split('-')[1]
#         bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск покупателей" в городе {city}')
#     else:
#         buttons_back = types.InlineKeyboardButton('Вернуться назад', callback_data='back_to')
#         markup_back = types.InlineKeyboardMarkup(row_width=1)
#         markup_back.add(buttons_back)
#
#
# @bot.message_handler()
# def great_settings(message):
#     bot.send_message(message.chat.id, 'Настройка завершена! Релевантные запросы будут появляться в '
#                                       'этом чате. Это может занять от нескольких минут до '
#                                       'нескольких часов.  Поменять настройки поиска можно в '
#                                       'Главном меню. /menu')
#
#
# @bot.message_handler(commands=['stop'])
# def stop(message):
#     bot.send_message(message.chat.id, 'Спасибо за использование нашего бота!')
#     bot.stop_polling()
#
#
# bot.polling()
