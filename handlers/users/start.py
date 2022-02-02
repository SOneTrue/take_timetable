import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.table_btn import time_table_btn
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.username}, нажми кнопку чтобы "
                         f"получить актуальное расписание.", reply_markup=time_table_btn)
