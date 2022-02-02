import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.timetable_photo import check_updates

@dp.message_handler(text='Расписание')
async def bot_give_table(message: types.Message):
    link = f'https://btgp.ru{await check_updates()}'
    await message.answer(f"{link}")