import logging
import json
from json import JSONDecodeError

logging.basicConfig(filename="log_3.log")

try:
    path = "data1.json"
    file = open(path)
    items = json.load(file)
    for item in items:
        print(item)
except FileNotFoundError:
    logging.exception("File not found!!!")

except JSONDecodeError:
    # Будет выполнено если файл найден, но не превращается из JSON
    logging.exception("Файл не удается преобразовать")
