from data.models import BotUsers, Callback
import telebot
from telebot import types
import pickle
import time
import json
import os
import django
import datetime
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()

urls = {
    'users': 'https://internetbor/api/users/',
    'callback': 'https://internetbor/api/callbacks',
    'news': 'https://internetbor/api/news/',
    'providers': 'https://internetbor/api/providers/',
    'top_providers': 'https://internetbor/api/top-providers/',
    'offers': 'https://internetbor/api/offers/',
}

# users = requests.get(urls['users'])

with open('token.txt', 'rb') as file:
    TOKEN = pickle.loads(file.read())

bot = telebot.TeleBot(TOKEN)

domen = 'http://127.0.0.1:8000/home'

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
all_requests = types.KeyboardButton(('Все заявки 🗂'))
opened = types.KeyboardButton(('Только открытые 📥'))
closed = types.KeyboardButton(('Только закрытые 📪'))
markup_arr = [all_requests, opened, closed]
markup.add(all_requests, opened, closed)
bot_users = BotUsers.objects.all()
admin_list = []
for i in bot_users:
    if i.is_admin:
        admin_list.append(i.user_id)
    else:
        pass


@bot.message_handler(commands=['start'])
def start(message):
    global markup, markup_arr, domen
    user = message.chat.id
    username = message.from_user.first_name
    response = ''
    status = 'User'
    bot_user = None
    try:
        bot_user = BotUsers.objects.get(user_id=message.chat.id)
    except:
        pass
    if bot_user is not None:
        if bot_user.is_admin:
            status = 'Admin'
            response = f'Здравствуйте, кажется вы уже присутствуете в нашей системе, ваш статус <b>{status}</b>. Я буду оповещать вас о новых заявках оставленных пользователями на сайте <b>{domen}</b>. Также у вас будет возможность видеть все заявки и их статусы.'
            bot.send_message(
                user, response, reply_markup=markup, parse_mode='html')

        else:
            response = f'Здравствуйте уважаемый пользователь, кажется вы не являетесь админом ваш статус <b>{status}</b>. Подождите пока вам дадут статус админа, чтобы воспользоваться моими фичами, а на данный момент к сожалению ничего не могу сделать для вас :)'
            bot.send_message(user, response, parse_mode='html')

    else:
        status = 'User'
        new_user = BotUsers(user_id=user, username=username, is_admin=False)
        response = f'Здравствуйте, кажется вас не было в нашей системе. Мы вас успешно зарегестрировали. Ваш статус <b>{status}</b>. Пока у вас не появится статус <b>Админа</b>, вы не можете воспользоваться моими услугами. '
        new_user.save()
        bot.send_message(user, response, parse_mode='html')


@bot.message_handler(commands=['validation'])
def validation(message):
    is_admin = BotUsers.objects.get(user_id=message.chat.id).is_admin
    response = ''
    if is_admin:
        response = f'Ваш статуc Admin. Я буду оповещать вас о новых заявках оставленных пользователями на сайте <b>{domen}</b>. Также у вас будет возможность видеть все заявки и их статусы.'
        bot.send_message(message.chat.id, response,
                         reply_markup=markup, parse_mode='html')
    else:
        response = f'Извините, кажется вы все еще не Admin. Попытайтесь позже :)'
        bot.send_message(message.chat.id, response, parse_mode='html')


process = None


@bot.message_handler(commands=['statistics'])
def stat(message):
    global process
    is_admin = BotUsers.objects.get(user_id=message.chat.id).is_admin
    response = ''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    today = types.KeyboardButton(('За сегодня'))
    week = types.KeyboardButton(('За неделю'))
    markup.add(today, week)

    if is_admin:
        response = f'Введите дату, за которую хотите получить статистику: '
        process = 'statistics'
        bot.send_message(message.chat.id, response, reply_markup=markup)

    else:
        response = f'Извините, кажется вы все еще не Admin.'
        bot.send_message(message.chat.id, response)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    global markup_arr, status
    user = BotUsers.objects.get(user_id=message.chat.id)
    is_admin = user.is_admin
    response = ''
    query = ''
    datetime.datetime.today().strftime('%b %d, %Y, %-I%p')
    if is_admin:
        if process == 'statistics':
            if message.text == 'За сегодня':
                try:
                    query = Callback.objects.get(
                        created=datetime.datetime.today())
                    response = f'Cтатистика заявок за сегодня:\n\n'
                except:
                    response = 'Нет заявок за сегодня!'
        elif process != 'statistics':
            if message.text == markup_arr[0].text:
                query = Callback.objects.all()
                response = f'Все заявки на данный момент, кол-во <b>({len(query)})</b>:\n\n'
            elif message.text == markup_arr[1].text:
                query = Callback.objects.filter(status='opened')
                response = f'Открытые заявки на данный момент, кол-во <b>({len(query)})</b>:\n\n'
            elif message.text == markup_arr[2].text:
                query = Callback.objects.filter(status='closed')
                response = f'Закрытые заявки на данный момент, кол-во <b>({len(query)})</b>:\n\n'

        if len(query) != 0:
            for i in query:

                response += f'\
Заявка <b>#{i.id}</b>\n\
Имя: <b>{i.name}</b>\n\
Телефон номер: <b>{i.phone}</b>\n\
Город: <b>{i.city}</b>\n\
Район: <b>{i.district}</b>\n\
Улица: <b>{i.city}</b>\n\
Дом: <b>{i.house}</b>\n\
Статус: <b>{i.status}</b>\n\
Посмотреть в админке: \nhttp://127.0.0.1:8000/admin/data/callback/{i.id}/change/\n\
--------------------------------\n\n'
    else:
        response = f'Извините, но я не могу выполнить ваш запрос, так как вы не являетесь Админом.' + \
            'Воспользуйтесь командой - /validation, чтобы проверить ваш статус. '
    bot.send_message(message.chat.id, response, parse_mode='html')


if __name__ == '__main__':
    print('Starting a bot...')
    bot.infinity_polling()
    print('Wrapping out...')
