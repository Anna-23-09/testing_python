import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

logging.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logging.info('Немного информации о работе кода')
logging.warning('Внимание! Надвигается буря')
logging.error('Поймали ошибку. Дальше только неизвестность')
logging.critical('На этом все')
