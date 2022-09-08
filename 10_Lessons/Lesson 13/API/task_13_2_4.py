import os

import dotenv
from flask import Flask

app = Flask(__name__)

dotenv.load_dotenv(override=True)
if os.environ.get("LOCATION") == 'work':
    location_message = 'Приложение запущено на рабочем сервере'
elif os.environ.get("LOCATION") == 'home':
    location_message = 'Приложение запущено на домашнем сервере'


@app.route('/')
def start_page():
    return f"{location_message}"


app.run()
