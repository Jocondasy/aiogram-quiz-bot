from aiogram import Router, types, F
from aiogram.filters import Command

from keyboards.quiz_keyboards import make_inline_keyboard, make_reply_keyboard
from data.quiz_data import quiz_data
from utils.database import get_quiz_index, update_quiz_index, get_user_stats

router = Router()

# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    text = "Привет! Я бот для проведения квиза. Готов начать?"
    keyboard = make_reply_keyboard(["Начать игру"])
    await message.answer(text, reply_markup=keyboard)


async def get_question(message: types.Message, user_id: int):
    current_question_index = await get_quiz_index(user_id)
    if current_question_index < len(quiz_data):
        question_info = quiz_data[current_question_index]
        keyboard = make_inline_keyboard(question_info['options'], question_info['correct_option'])
        await message.answer(question_info['question'], reply_markup=keyboard)
    else:
        await message.answer("Это был последний вопрос. Квиз завершен!")
        stats = await get_user_stats(user_id)
        await message.answer(f"Ваша статистика:\nПравильных ответов: {stats['correct']}\nНеправильных ответов: {stats['wrong']}")

async def new_quiz(message: types.Message):
    user_id = message.from_user.id
    # Сбрасываем только индекс вопроса, НЕ статистику
    await update_quiz_index(user_id, 0)
    await get_question(message, user_id)

@router.message(F.text == "Начать игру")
@router.message(Command("quiz"))
async def cmd_quiz(message: types.Message):
    await message.answer("Давайте начнем квиз!", reply_markup=types.ReplyKeyboardRemove())
    await new_quiz(message)


@router.callback_query(F.data == "right_answer")
async def right_answer(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    current_question_index = await get_quiz_index(callback.from_user.id)
    await callback.message.answer("Верно!")
    
    # Обновляем индекс и увеличиваем счетчик правильных ответов
    await update_quiz_index(callback.from_user.id, current_question_index + 1, correct_increment=1)
    
    await get_question(callback.message, callback.from_user.id)

@router.callback_query(F.data == "wrong_answer")
async def wrong_answer(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    current_question_index = await get_quiz_index(callback.from_user.id)
    correct_option_index = quiz_data[current_question_index]['correct_option']
    correct_option_text = quiz_data[current_question_index]['options'][correct_option_index]
    
    await callback.message.answer(f"Неправильно. Правильный ответ: {correct_option_text}")
    
    # Обновляем индекс и увеличиваем счетчик неправильных ответов
    await update_quiz_index(callback.from_user.id, current_question_index + 1, wrong_increment=1)
    
    await get_question(callback.message, callback.from_user.id)


@router.message(Command("stats"))
async def cmd_stats(message: types.Message):
    user_id = message.from_user.id
    stats = await get_user_stats(user_id)
    await message.answer(f"Ваша статистика:\nПравильных ответов: {stats['correct']}\nНеправильных ответов: {stats['wrong']}")