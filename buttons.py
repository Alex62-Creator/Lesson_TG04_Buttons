from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Создание простого меню с Reply-кнопками
simple_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ], resize_keyboard=True)

# Создание Inline-кнопок с URL-ссылками
async def inline_keyboard():
    inline_key = [['Новости', "https://sputnik.by"], ['Музыка', "https://zvuk.com"], ['Видео', "https://youtube.com"]]
    keyboard = InlineKeyboardBuilder()
    for key in inline_key:
        keyboard.add(InlineKeyboardButton(text=key[0], url=key[1]))
    return keyboard.adjust(2).as_markup()

# Динамическое изменение клавиатуры

# Первоначальная клавиатура
inline_keyboard_first = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='dynamic')],
    ])

# Новая клавиатура
inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data='opt1'),
    InlineKeyboardButton(text="Опция 2", callback_data='opt2')],
    ])