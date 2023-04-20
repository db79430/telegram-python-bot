import telebot
from telebot import types
import time

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '👋 Вас приветствует чат-бот Houser Bot!'
                                      '🏡 Мы поможем вам найти клиентов через целевые каналы в Telegram и Facebook.')

    bot.send_message(message.chat.id, 'ℹ️ Чтобы начать, нам необходимо настроить категории поиска. Не переживайте - их '
                                      'можно перенастроить в любой момент. После выбора категории поиска бот начнет '
                                      'отслеживать релевантные предложения и высылать их в этот чат. Это может занять '
                                      'некоторое время - в зависимости от появления новых запросов, подходящих под '
                                      'ваши критерии поиска. Ну что, приступим?  или введите команду /settings')
    buttons_city = [
        types.InlineKeyboardButton('Анталия', callback_data='antalya'),
        types.InlineKeyboardButton('Кемер', callback_data='kemer'),
        types.InlineKeyboardButton("Аланья", callback_data='alanya'),
        types.InlineKeyboardButton("Мерсин", callback_data='mersin'),
        types.InlineKeyboardButton("Стамбул", callback_data='istambul'),
        types.InlineKeyboardButton("Демирташ", callback_data='dzemitrash'),
        types.InlineKeyboardButton("Газипаша", callback_data='gezipasha'),
        types.InlineKeyboardButton("Сиде", callback_data='side')
    ]

    buttons_category = [
        types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords'),
        types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants'),
        types.InlineKeyboardButton('Поиск продавцов', callback_data='rents'),
        types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers')
    ]
    markup_city = types.InlineKeyboardMarkup(row_width=2)

    markup_city.add(*buttons_city)
    markup_category = types.InlineKeyboardMarkup(row_width=1)
    markup_category.add(*buttons_category)
    bot.send_message(message.chat.id, ' 🌅 Выберите локации, по которым мы начнем наш поиск:', reply_markup=markup_city)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'antalya':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Вы выбрали город Анталия')
        buttons_category = [
            types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords-antalya'),
            types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants-antalya'),
            types.InlineKeyboardButton('Поиск продавцов', callback_data='rents-antalya'),
            types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers-antalya')
        ]
        markup_category = types.InlineKeyboardMarkup(row_width=1)
        markup_category.add(*buttons_category)
        bot.send_message(call.message.chat.id, 'Отлично! Теперь выберите типы запросов, которые вас интересуют:',
                         reply_markup=markup_category)
    elif call.data == 'kemer':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Вы выбрали город Кемер')
        buttons_category = [
            types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords-kemer'),
            types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants-kemer'),
            types.InlineKeyboardButton('Поиск продавцов', callback_data='rents-kemer'),
            types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers-kemer')
        ]
        markup_category = types.InlineKeyboardMarkup(row_width=1)
        markup_category.add(*buttons_category)
        bot.send_message(call.message.chat.id, 'Отлично! 🙂 Теперь выберите типы запросов, которые вас интересуют:',
                         reply_markup=markup_category)
    elif call.data == 'alanya':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Вы выбрали город Кемер')
        buttons_category = [
            types.InlineKeyboardButton('Поиск арендодателей', callback_data='landlords-alanya'),
            types.InlineKeyboardButton('Поиск арендаторов', callback_data='tenants-alanya'),
            types.InlineKeyboardButton('Поиск продавцов', callback_data='rents-alanya'),
            types.InlineKeyboardButton('Поиск покупателей', callback_data='buyers-alanya')
        ]
        markup_category = types.InlineKeyboardMarkup(row_width=1)
        markup_category.add(*buttons_category)
        bot.send_message(call.message.chat.id, 'Отлично! Теперь выберите типы запросов, которые вас интересуют:',
                         reply_markup=markup_category)
    elif call.data.startswith('landlords'):
        bot.answer_callback_query(call.id)
        city = call.data.split('-')[1]
        bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск арендодателей" в городе {city}')
    elif call.data.startswith('tenants'):
        bot.answer_callback_query(call.id)
        city = call.data.split('-')[1]
        bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск арендаторов" в городе {city}')
    elif call.data.startswith('rents'):
        bot.answer_callback_query(call.id)
        city = call.data.split('-')[1]
        bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск продавцов" в городе {city}')
    elif call.data.startswith('buyers'):
        bot.answer_callback_query(call.id)
        city = call.data.split('-')[1]
        bot.send_message(call.message.chat.id, f'Вы выбрали категорию "Поиск покупателей" в городе {city}')


@bot.message_handler()
def great_settings(message):
    bot.send_message(message, 'Настройки завершены. Отправка сообщений начнется через 10 секунд.')
    time.sleep(10)
    while True:
        bot.send_message(message, 'Hello, world!')
        time.sleep(10)




@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, 'Спасибо за использование нашего бота!')
    bot.stop_polling()


bot.polling()
