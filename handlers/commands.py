from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from handlers.OpenRouter import user_context

router = Router()

HELP_MESSAGE = """
Вот все мои команды:
/start - начало работы с ботом
/help - список доступных команд
/info - информация о боте и команде
/clear - Очищает контекст диалога
Просто отправьте текстовое сообщение, и бот ответит вам.
"""

START_MESSAGE = """
👋 Привет! Я бот 🤖 с интеграцией LLM. Введите ваш запрос.
(Вызови /help чтобы увидеть доступные команды)
"""

INFO_MESSAGE = """
Я бот который создан командой из МТУСИ(Салов Захар).
Если есть какие то вопросы по поводу сотрудничества обращайтесь на sosikoni@gmail.com
"""

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(START_MESSAGE)

@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer(INFO_MESSAGE)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(HELP_MESSAGE)

# Обработчик команды /clear
@router.message(Command("clear"))
async def cmd_clear_context(message: Message):
    user_id = message.from_user.id

    # Очищаем контекст для пользователя
    if user_id in user_context:
        user_context[user_id] = []
        await message.reply("Контекст диалога очищен.")
    else:
        await message.reply("Контекст уже пуст.")