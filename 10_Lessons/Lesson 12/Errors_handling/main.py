# С ОБРАБОТКОЙ ОШИБОК
value = input("Введите число: ")

try:
  number = int(value)
  print(number)
except:
  print("Неверный ввод")