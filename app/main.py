import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from orm import create_tables

create_tables()

logging.info('Приложение готово к работе')
