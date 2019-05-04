import logging


class MyLogsHandler(logging.Handler):

    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)

        self.bot.send_message(chat_id=self.chat_id, text=log_entry)


logger = logging.getLogger("Название логера")
logger.setLevel(logging.INFO)
