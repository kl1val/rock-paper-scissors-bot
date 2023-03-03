from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from bot.keyboards.keyboards import yes_no_kb, game_kb
from bot.services.services import get_bot_choice, get_winner
from bot.lexicon.lexicon_ru import LEXICON_RU


router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"],
                         reply_markup=yes_no_kb)
    

@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"],
                         reply_markup=yes_no_kb)
    

@router.message(Text(text=LEXICON_RU["yes_button"]))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU["yes"],
                         reply_markup=game_kb)
    

@router.message(Text(text=LEXICON_RU["no_button"]))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU["no"])


@router.message(Text(text=[LEXICON_RU["rock"],
                           LEXICON_RU["paper"],
                           LEXICON_RU["scissors"]]))
async def procces_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)

