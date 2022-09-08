# catalog / views.py

# Сначала импортируем класс блюпринта
from flask import Blueprint

# Затем создаем новый блюпринт, выбираем для него имя
catalog_blueprint = Blueprint('catalog_blueprint', __name__)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@catalog_blueprint.route('/')
def profile_page():
    return "Я главная каталога"


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@catalog_blueprint.route('/<cat>')
def category_page(cat):
    return f"Я страничка каталога категории {cat}"
