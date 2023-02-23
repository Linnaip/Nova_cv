import requests
from aiogram import types

from .app import dispatcher


@dispatcher.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет, а дай номер')


@dispatcher.message_handler(commands=['send'])
async def send_phone_number(message: types.Message):
    button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True)
    keybord = types.ReplyKeyboardMarkup()
    keybord.add(button_phone)
    await message.reply('Номер телефона', reply_markup=keybord)


@dispatcher.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        user_id = message.from_user.id
        phone = message.contact.phone_number
        print(message.contact)
        data = {'phone': phone, 'login': user_id}
        url = 'https://s1-nova.ru/app/private_test_python/'
        response = requests.post(url, data=data)
        print(response.status_code)
