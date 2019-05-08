import os
import requests
from telegram import Bot

from bot_logger import logger, MyLogsHandler


def make_message(attempt: dict) -> str:
    message = 'У Вас проверили работу {}\n'.format(attempt['lesson_title'])

    negative_messsage = 'Нужно доработать задачу'
    positive_message = 'Все OK'

    if attempt['is_negative']:
        message += negative_messsage
    else:
        message += positive_message

    message += '\nhttps://dvmn.org{}'.format(attempt['lesson_url'])

    return message


if __name__ == '__main__':
    token_telegram_bot = os.environ['token_telegram_bot']
    chat_id_telegram = os.environ['chat_id_telegram']
    token_devman = os.environ['token_devman']

    bot = Bot(token=token_telegram_bot)

    logger.addHandler(MyLogsHandler(bot, chat_id_telegram))

    path = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': token_devman}

    first = True
    timestamp = None

    while True:
        if first:
            params = dict()
            first = False
        else:
            params = {'timestamp': timestamp}

        try:
            res = requests.get(path, headers=headers, params=params)
        except requests.ConnectionError as error:
            logger.exception(error)
            continue

        res.raise_for_status()
        res_dict = res.json()

        if res_dict['status'] == 'found':
            for attempt in res_dict['new_attempts']:
                text = make_message(attempt)
                bot.send_message(chat_id=chat_id_telegram, text=text)

            timestamp = res_dict['last_attempt_timestamp']
            continue

        timestamp = res_dict['timestamp_to_request']
