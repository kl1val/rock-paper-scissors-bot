import asyncio
import logging

from aiogram import Bot, Dispatcher
from bot.config_data.config import Config, load_config
from bot.handlers import user_handlers, other_handlers

# инициализируем логгер
logger = logging.getLogger(__name__)

# Функция конфигурирования и запуска бота
async def main():
    # Конфигуриеруем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')
    
    # Выводим в консоль информацию о начале запуска бота
    logging.info('Starting bot')

    # Загружаем конфиг в переменную
    config: Config = load_config('./.env')

    # Инициализируем бота и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, 
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

    

