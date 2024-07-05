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
    if date_now == '4':
        gif_from_pc = FSInputFile('meme-polish-cow.gif')
        await message.answer_animation(
            gif_from_pc,
            caption=f'мой муд сегодня:',
            show_caption_above_media=True,
        )
    if date_now == '5':
        gif_from_pc = FSInputFile('meme-polish-cow.gif')
        await message.answer_animation(
            gif_from_pc,
            caption=f'мой муд сегодня:',
            show_caption_above_media=True,
        )
    if date_now == '6':
        gif_from_pc = FSInputFile('meme-polish-cow.gif')
        await message.answer_animation(
            gif_from_pc,
            caption=f'мой муд сегодня:',
            show_caption_above_media=True,
        )
    if date_now == '0':
        gif_from_pc = FSInputFile('meme-polish-cow.gif')
        await message.answer_animation(
            gif_from_pc,
            caption=f'мой муд сегодня:',
            show_caption_above_media=True,
        )
    if date_now == '1':
        gif_from_pc = FSInputFile('meme-polish-cow.gif')
        await message.answer_animation(
            gif_from_pc,
            caption=f'мой муд сегодня:',
            show_caption_above_media=True,
        )
    if date_now == '2':
        gif_from_pc = FSInputFile('meme-polish-cow.gif')
        await message.answer_animation(
            gif_from_pc,
            caption=f'мой муд сегодня:',
            show_caption_above_media=True,
        )
    if date_now == '3':
        gif_from_pc = FSInputFile('meme-polish-cow.gif')
        await message.answer_animation(
            gif_from_pc,
            caption=f'мой муд сегодня:',
            show_caption_above_media=True,
        )


