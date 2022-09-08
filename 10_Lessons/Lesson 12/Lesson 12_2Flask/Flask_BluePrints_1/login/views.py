# Сначала импортируем класс блюпринта
from flask import Blueprint

# Затем создаем новый блюпринт, выбираем для него имя
login_blueprint = Blueprint('login_blueprint', __name__)

# Создаем вьюшку, используя в декораторе блюпринт вместо app
@login_blueprint.route('/login/')
def profile_page():
    return f"Я страничка логина для пользователя!"
