from aiogram.types import Message
from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def hello(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}, здесь ты можешь узнать какое настроение у меня сегодня!')
    
