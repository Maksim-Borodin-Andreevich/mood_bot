import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import router
from config_reader import config

async def main():
    bot = Bot(
        token= config.bot_token,
        default=DefaultBotProperties(
            ParseMode=ParseMode.HTML
        )
    )

    dp = Dispatcher()
    dp.include_router(router)