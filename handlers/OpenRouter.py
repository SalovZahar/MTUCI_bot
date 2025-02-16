from aiogram import Router
from aiogram.client.session.middlewares.request_logging import logger
from aiogram.types import Message
import requests
from dotenv import load_dotenv
import os

router = Router()

# Загрузка переменных окружения из файла .env
load_dotenv()

#  API-ключ модели
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# URL-адрес API OpenRouter для отправки запросов.
OPENROUTER_ENDPOINT = 'https://openrouter.ai/api/v1/chat/completions'

# История диалога (для поддержки контекста)
user_context = {}

# Обработчик текстовых сообщений
@router.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    user_input = message.text

    # Сохраняем контекст
    # Если у пользователя еще нет истории диалога, создается пустой список.
    # Затем сообщение пользователя добавляется в историю.
    if user_id not in user_context:
        user_context[user_id] = []
    user_context[user_id].append({"role": "user", "content": user_input})

    # Вызываем LLM через OpenRouter API
    response_text = await query_llm(user_context[user_id])

    # Добавляем ответ LLM в контекст
    user_context[user_id].append({"role": "assistant", "content": response_text})

    # Убедаемся что ответ от модели (google/gemini-2.0-flash-001) не пустой.
    if not response_text or response_text.strip() == "":
        response_text = "Произошла ошибка: ответ от модели пуст."

    # Отправляем ответ пользователю
    await message.reply(response_text)

# Функция для запроса к LLM
async def query_llm(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    # Тело запроса, содержащее модель и историю сообщений.
    data = {
        "model": "google/gemini-2.0-flash-001",
        "messages": messages
        # "max_tokens": 500 - возможность поставить ограничение на символы в ответе
    }
    try:
        response = requests.post(OPENROUTER_ENDPOINT, headers=headers, json=data)

        # Проверка, что запрос завершился успешно (код ответа 200).
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"Ответ сервера: {e.response.  text}")
        return "Произошла ошибка при обработке вашего запроса."
