import requests
from dotenv import dotenv_values
from telegram import Bot


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
    dotenv_dict = dotenv_values()

    token = dotenv_dict['token']
    chat_id = dotenv_dict['chat_id']
    authorization = dotenv_dict['Authorization']

    bot = Bot(token=token)

    path = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': authorization}

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
            print("Error Connecting:", error)
            continue

        res.raise_for_status()
        res_dict = res.json()

        if res_dict['status'] == 'found':
            for attempt in res_dict['new_attempts']:
                text = make_message(attempt)
                bot.send_message(chat_id=chat_id, text=text)

            timestamp = res_dict['last_attempt_timestamp']
            continue

        timestamp = res_dict['timestamp_to_request']
