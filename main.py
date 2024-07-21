import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData
from decouple import config
from groups import directions, channels_groups

TOKEN = config('TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode="HTML")

dp = Dispatcher(bot)


cb_nest = CallbackData('nest', 'action')
cb_channels = CallbackData('channels', 'action')
cb_group = CallbackData('group', 'action')


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
    for group_channel in directions[direction]['group']:
        buttons.append(InlineKeyboardButton(text=group_channel, callback_data=cb_channels.new(action=group_channel)))
    buttons.append(InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
    inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(*buttons)
    return inline_kb


def channels_keyboard(group):
    inline_btn_1 = InlineKeyboardButton(text='Готово, проверяй!', callback_data=cb_group.new(action=group))
    back_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back')
    inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_1).add(back_btn)
    return inline_kb


def success_keyboard():
    inline_btn_1 = InlineKeyboardButton('Получить доступ 🔑', url='https://easyoffer.ru/4jfVYlHMjaNg1yESRMGLb08Mu3QmKMgZhBby1IFYy')
    back_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back')
    inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_1).add(back_btn)
    return inline_kb


# Шаг 1. Старт
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я бот, который выдаст доступ к сайту 👾 easyoffer'
                         '\nКакое направление тебе интересно?', reply_markup=welcome_keyboard())


# Шаг 2. Обработка вложенность группы
@dp.callback_query_handler(cb_nest.filter())
async def show_nest(callback: types.CallbackQuery, callback_data: dict):
    direction = callback_data['action']
    await callback.message.edit_text('А точнее?', reply_markup=specify_keyboard(direction))


# Шаг 3. Вывод списка групп для подписки
@dp.callback_query_handler(cb_channels.filter())
async def show_channels(callback: types.CallbackQuery, callback_data: dict):
    group = callback_data['action']
    channels_number = len(channels_groups[group])
    if channels_number == 1:
        await callback.message.edit_text(
            f'Получи доступ к easyoffer, подписавшись на наши каналы:\n\n'
            f'<a href="https://t.me/easyoffer_ru">easyoffer</a>\n'
            f'<a href="https://t.me/{channels_groups[group][0][1]}">{channels_groups[group][0][0]}</a>\n'
            , reply_markup=channels_keyboard(group), parse_mode="HTML", disable_web_page_preview=True)
    if channels_number == 2:
        await callback.message.edit_text(
            f'Получи доступ к easyoffer, подписавшись на наши каналы:\n\n'
            f'<a href="https://t.me/easyoffer_ru">easyoffer</a>\n'
            f'<a href="https://t.me/{channels_groups[group][0][1]}">{channels_groups[group][0][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][1][1]}">{channels_groups[group][1][0]}</a>\n'
            , reply_markup=channels_keyboard(group), parse_mode="HTML", disable_web_page_preview=True)
    if channels_number == 3:
        await callback.message.edit_text(
            f'Получи доступ к easyoffer, подписавшись на наши каналы:\n\n'
            f'<a href="https://t.me/easyoffer_ru">easyoffer</a>\n'
            f'<a href="https://t.me/{channels_groups[group][0][1]}">{channels_groups[group][0][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][1][1]}">{channels_groups[group][1][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][2][1]}">{channels_groups[group][2][0]}</a>\n'
            , reply_markup=channels_keyboard(group), parse_mode="HTML", disable_web_page_preview=True)
    if channels_number == 4:
        await callback.message.edit_text(
            f'Получи доступ к easyoffer, подписавшись на наши каналы:\n\n'
            f'<a href="https://t.me/easyoffer_ru">easyoffer</a>\n'
            f'<a href="https://t.me/{channels_groups[group][0][1]}">{channels_groups[group][0][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][1][1]}">{channels_groups[group][1][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][2][1]}">{channels_groups[group][2][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][3][1]}">{channels_groups[group][3][0]}</a>\n'
            , reply_markup=channels_keyboard(group), parse_mode="HTML", disable_web_page_preview=True)
    if channels_number == 5:
        await callback.message.edit_text(
            f'Получи доступ к easyoffer, подписавшись на наши каналы:\n\n'
            f'<a href="https://t.me/easyoffer_ru">easyoffer</a>\n'
            f'<a href="https://t.me/{channels_groups[group][0][1]}">{channels_groups[group][0][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][1][1]}">{channels_groups[group][1][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][2][1]}">{channels_groups[group][2][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][3][1]}">{channels_groups[group][3][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][4][1]}">{channels_groups[group][4][0]}</a>\n'
            , reply_markup=channels_keyboard(group), parse_mode="HTML", disable_web_page_preview=True)
    if channels_number == 6:
        await callback.message.edit_text(
            f'Получи доступ к easyoffer, подписавшись на наши каналы:\n\n'
            f'<a href="https://t.me/easyoffer_ru">easyoffer</a>\n'
            f'<a href="https://t.me/{channels_groups[group][0][1]}">{channels_groups[group][0][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][1][1]}">{channels_groups[group][1][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][2][1]}">{channels_groups[group][2][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][3][1]}">{channels_groups[group][3][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][4][1]}">{channels_groups[group][4][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][5][1]}">{channels_groups[group][5][0]}</a>\n'
            , reply_markup=channels_keyboard(group), parse_mode="HTML", disable_web_page_preview=True)
    if channels_number == 7:
        await callback.message.edit_text(
            f'Получи доступ к easyoffer, подписавшись на наши каналы:\n\n'
            f'<a href="https://t.me/easyoffer_ru">easyoffer</a>\n'
            f'<a href="https://t.me/{channels_groups[group][0][1]}">{channels_groups[group][0][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][1][1]}">{channels_groups[group][1][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][2][1]}">{channels_groups[group][2][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][3][1]}">{channels_groups[group][3][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][4][1]}">{channels_groups[group][4][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][5][1]}">{channels_groups[group][5][0]}</a>\n'
            f'<a href="https://t.me/{channels_groups[group][6][1]}">{channels_groups[group][6][0]}</a>\n'
            , reply_markup=channels_keyboard(group), parse_mode="HTML", disable_web_page_preview=True)


# Шаг 4. Выдача ссылки
@dp.callback_query_handler(cb_group.filter())
async def check_channels(callback: types.CallbackQuery, callback_data: dict):
    group = callback_data['action']
    user_id = callback.from_user.id
    if await check_sub(group, user_id):
        await callback.message.edit_text(f'✅ Готово! Нажми "Получить доступ"', reply_markup=success_keyboard())
    else:
        await callback.answer('Подпишиcь на все каналы 🤷‍♂️Если бот тупит, то его нужно обновить командой /start', show_alert=True)
    await callback.answer()


# Проверка подписки
async def check_sub(group, user_id):
    chat_member = await bot.get_chat_member(chat_id='@easyoffer_ru', user_id=user_id)
    if chat_member['status'] == 'left':
        return False
    for channel in channels_groups[group]:
        chat_member = await bot.get_chat_member(chat_id=f'@{channel[1]}', user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    else:
        return True



# Вернуться назад
@dp.callback_query_handler(text='back')
async def back(callback: types.CallbackQuery):
    await callback.message.edit_text('Какое направление тебе интересно?', reply_markup=welcome_keyboard())




#
#
#

#
#
#
#






# # Шаг 2. Уточнение направления, если есть вложенность
# @dp.message_handler(lambda message: directions[message.text]['attachment'] == True)
# async def without_puree(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = []
#     for direction_name in directions[message.text]['group']:
#         buttons.append(direction_name)
#     keyboard.add(*buttons)
#     await message.answer('А точнее?', reply_markup=keyboard)


# # Шаг 3. Список каналов на подписку
# @dp.message_handler(lambda message: message.text == 'python')
# async def without_puree(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button_1 = types.KeyboardButton(text="Получить доступ")
#     keyboard.add(button_1)
#     await message.answer('Подпишись на эти телегам каналы:\n'
#                          '1. easy Python\n'
#                          '2. Python Job\n'
#                          '3. Python Chat', reply_markup=keyboard)



if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
