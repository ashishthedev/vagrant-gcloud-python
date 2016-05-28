
__author__ = """ashishthedev@gmail.com (Ashish Anand)"""

import newapp
import config


import logging
from logging.handlers import RotatingFileHandler


DEBUG = True
app = newapp.create_app(config, debug=DEBUG)

handler = RotatingFileHandler('newapp.log', maxBytes=100000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


