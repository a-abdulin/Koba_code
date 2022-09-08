# app.py

from flask import Flask, request, render_template

# Импортируем блюпринты из их пакетов
from catalog.views import catalog_blueprint
from profile.views import profile_blueprint
from login.views import login_blueprint

app = Flask(__name__)

# Регистрируем первый блюпринт
app.register_blueprint(catalog_blueprint, url_prefix='/catalog')
# Регистрируем второй блюпринт
app.register_blueprint(profile_blueprint)
# Регистрируем третий блюпринт
app.register_blueprint(login_blueprint)


app.run()
