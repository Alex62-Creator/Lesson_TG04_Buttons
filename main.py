# Задание 1: Создание простого меню с кнопками
# При отправке команды /start бот будет показывать меню с кнопками "Привет" и "Пока". При нажатии на кнопку "Привет" бот должен отвечать "Привет, {имя пользователя}!", а при нажатии на кнопку "Пока" бот должен отвечать "До свидания, {имя пользователя}!".
# Задание 2: Кнопки с URL-ссылками
# При отправке команды /links бот будет показывать инлайн-кнопки с URL-ссылками. Создайте три кнопки с ссылками на новости/музыку/видео
# Задание 3: Динамическое изменение клавиатуры
# При отправке команды /dynamic бот будет показывать инлайн-кнопку "Показать больше". При нажатии на эту кнопку бот должен заменять её на две новые кнопки "Опция 1" и "Опция 2". При нажатии на любую из этих кнопок бот должен отправлять сообщение с текстом выбранной опции.

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
# Файл config с ключами необходимо создавать дополнительно
from config import TOKEN
import buttons as bt

# Создаем объекты классов Bot (отвечает за взаимодействие с Telegram bot API) и Dispatcher (управляет обработкой входящих сообщений и команд)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(CommandStart())
async def start(message: Message):
    # Подключение простого меню с Reply-кнопками
    await message.answer('Вас приветствует бот Кнопки', reply_markup=bt.simple_keyboard)

# Обработка кнопки Привет
@dp.message(F.text == "Привет")
async def hello_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}')

# Обработка кнопки Пока
@dp.message(F.text == "Пока")
async def bye_button(message: Message):
   await message.answer(f'Пока, {message.from_user.first_name}')

# Обработка команды /links
@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Сделай выбор', reply_markup=await bt.inline_keyboard())

# Обработка команды /dynamic
@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Динамически меняем клавиатуру', reply_markup=bt.inline_keyboard_first)

# Замена сообщения и inline-кнопок
@dp.callback_query(F.data == 'dynamic')
async def new_button(callback: CallbackQuery):
    await callback.message.edit_text('Новая клавиатура', reply_markup=bt.inline_keyboard_dynamic)

# Обработка кнопки Опция 1
@dp.callback_query(F.data == 'opt1')
async def opt1(callback: CallbackQuery):
   await callback.answer("Работает Опция 1", show_alert=True)

# Обработка кнопки Опция 2
@dp.callback_query(F.data == 'opt2')
async def opt2(callback: CallbackQuery):
   await callback.answer("Работает Опция 2", show_alert=True)

# Создаем асинхронную функцию main, которая будет запускать наш бот
async def main():
    await dp.start_polling(bot)

# Запускаем асинхронную функцию main
if __name__ == "__main__":
    asyncio.run(main())