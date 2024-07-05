from aiogram.types import Message, FSInputFile
from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

from datetime import datetime

router = Router()

@router.message(CommandStart())
async def hello(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}, здесь ты можешь узнать какое настроение у меня сегодня!\nПросто используй команду /mood')
    
@router.message(Command('mood'))
async def get_mood(message: Message):

    date_now = datetime.now().weekday()
    path = './gifs/' + str(date_now) + '.gif'
    gif_from_pc = FSInputFile(path=path)
   
    await message.answer_animation(
        animation=gif_from_pc,
        caption=f'мой муд сегодня:',
        show_caption_above_media=True,
    )


