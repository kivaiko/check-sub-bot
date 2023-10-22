from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from groups import directions
from main import cb_nest, cb_channels


def welcome_keyboard():
    buttons = []
    for direction in directions:
        if directions[direction]['attachment']:
            buttons.append(InlineKeyboardButton(text=direction, callback_data=cb_nest.new(action=direction)))
        else:
            buttons.append(InlineKeyboardButton(text=direction, callback_data=cb_channels.new(action=direction)))
    inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(*buttons)
    return inline_kb


def specify_keyboard(direction):
    buttons = []
    for group_channel in directions[direction]:
        buttons.append(InlineKeyboardButton(text=group_channel, callback_data=cb_channels.new(action=direction)))
    inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(*buttons)
    return inline_kb


def channels_keyboard():
    inline_btn_1 = InlineKeyboardButton('Подписался', callback_data='check')
    inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_1)
    return inline_kb


def success_keyboard():
    inline_btn_1 = InlineKeyboardButton('Получить доступ', url='https://goo.su/8vBNUy')
    inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_1)
    return inline_kb
