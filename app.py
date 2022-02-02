from aiogram import executor

import filters
import handlers
import middlewares
from data.config import ADMINS
from loader import dp
from utils.misc.logger import setup_logger
from utils.notify_admins import notify_admins
from utils.set_bot_commands import set_default_commands
from utils.timetable_photo import check_updates


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await notify_admins(ADMINS)


if __name__ == '__main__':
    setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
    executor.start_polling(dp, on_startup=on_startup)
