from dotenv import dotenv_values
import logging

from devman_bot import bot_start

if __name__ == '__main__':
    dotenv_dict = dotenv_values()

    token_telegram_bot = dotenv_dict['token_telegram_bot']
    chat_id_telegram = dotenv_dict['chat_id_telegram']
    token_devman = dotenv_dict['token_devman']

    logger = logging.getLogger('Bot-logger')
    logger.setLevel(logging.INFO)

    bot_start(token_telegram_bot, chat_id_telegram, token_devman, logger)
