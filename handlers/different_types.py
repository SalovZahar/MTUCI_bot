from aiogram import Router, F
from aiogram.types import Message

router = Router()

# ответить пользователю той же гифкой, что была прислана
@router.message(F.animation)
async def echo_gif(message: Message):
    await message.answer("Я не умею обрабатывать гифки:(")
    await message.reply_animation(message.animation.file_id)

@router.message(F.sticker)  # ответка на стикер который отправил пользователь
async def echo_to_text(message: Message):
    await message.reply("Я не умею обрабатывать стикеры:(")

@router.message(F.photo)  # ответка на фото которое отправил пользователь
async def echo_to_text(message: Message):
    await message.reply("Ну и зачем мне твое фото")

@router.message(F.video)  # ответка на видео которое отправил пользователь
async def echo_to_text(message: Message):
    await message.reply("Я не понимаю ваши видео у меня лапки")
