from aiogram.types import Message
from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def hello(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}, здесь ты можешь узнать какое настроение у меня сегодня!\n Просто используй команду /gif')
    
@router.message(Command('mood'))
async def get_mood(message: Message):
    await message.answer_animation(
        animation='meme-polish-cow.gif',
        caption='мой муд сегодня:',
        show_caption_above_media=True,
    )
    
