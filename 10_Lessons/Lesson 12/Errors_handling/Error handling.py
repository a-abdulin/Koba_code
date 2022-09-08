import json
from json import JSONDecodeError

try:
    file = open("data.jsons")
    items = json.load(file)
    for item in itemZZZ :
        print(item)
except BaseException as e:
    print(e)
except JSONDecodeError:
    print("Файл не удается преобразовать")
except NameError:
    print("Ошибка в переменных")

# Будет выведено NameError: name 'itemZZZ' is not defined
