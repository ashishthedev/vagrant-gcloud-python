
__author__ = """ashishthedev@gmail.com (Ashish Anand)"""

import newapp
import config

DEBUG = True
app = newapp.create_app(config, debug=DEBUG)

