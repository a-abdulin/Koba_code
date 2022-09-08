try:
	user_input = int(input('Введите  число: '))
	result = 1 / user_input
except ValueError:
	print("Неверный ввод")
except ZeroDivisionError:
	print("Деление на ноль")
else:
	print(f"Результат: {result}")
finally:
	print("В любом случае спасибо")
