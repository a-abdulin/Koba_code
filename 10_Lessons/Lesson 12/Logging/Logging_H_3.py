import logging

# Создаем или получаем новый логгер
logger_one = logging.getLogger("one")

# Cоздаем ему обработчик
console_handler = logging.FileHandler("log_file.log")

# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(pathname)s : %(asctime)s : %(message)s")
# Применяем форматирование к обработчику
console_handler.setFormatter(formatter_one)

# Добавлякем обработчик к журналу
logger_one.addHandler(console_handler)

logger_one.warning("Logger is working!!!")
