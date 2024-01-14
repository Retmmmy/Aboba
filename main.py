# Импорты используемых библиотек
import asyncio  # Позволяет работать с асинхронными функциями
from aiogram import Bot, Dispatcher, types  # Базовые объекты для работы с ботами
from aiogram.filters import Command  # Фильтры для принятия входных сообщения
import logging  # Получение информации о процессе работы бота
from custom_json import getData, addData, delData  # Моя библиотека для лёгкой работы с JSON-файлами

logging.basicConfig(level=logging.INFO)  # Установка уровня логирования
dp = Dispatcher()  # Создание диспетчера
last_messages = {}
last_statuses = {}

configData = getData("data/config.json")  # Получение словаря со всеми параметрами бота
bot = Bot(token = configData["token"])  # Выдача телеграм-логина боту

@dp.message(Command("start"))  # Обработчик команды /start
async def startCMD(message: types.Message):
  # Отвечаем пользователю на /start
  bot_message = await message.reply("Добро пожаловать в AbobaEconomicBot!")
  last_messages[message.chat.id] = bot_message  # Запись сообщения бота в словарь чатов
  last_statuses[message.chat.id] = "start"  # Выдаём статус общения бота с пользователем

@dp.message()  # В случае сообщений не попадающих под фильтры
async def textMessage(message: types.Message):
  print(message.chat.id)

async def main():
  await dp.start_polling(bot)  # Запуск сервера бота

if __name__ == "__main__":
  asyncio.run(main())  # Запуск асинхронной функции main()
  