import logging

new_logger = logging.getLogger()

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log.txt")

new_logger.addHandler(console_handler)
new_logger.addHandler(file_handler)

new_logger.warning("Все работает")
