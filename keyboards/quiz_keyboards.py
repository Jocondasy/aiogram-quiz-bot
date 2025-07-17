from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

def make_reply_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    kb = [[KeyboardButton(text=item)] for item in items]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def make_inline_keyboard(options: list, correct_option_index: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for index, option in enumerate(options):
        callback_data = "right_answer" if index == correct_option_index else "wrong_answer"
        builder.add(InlineKeyboardButton(text=option, callback_data=callback_data))
    builder.adjust(1)
    return builder.as_markup()