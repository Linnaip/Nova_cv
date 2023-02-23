from aiogram import executor

from src.bot_app.app import dispatcher


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
