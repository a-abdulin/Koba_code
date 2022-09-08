a = input()
b = input()

try:
    a_int = int(a)
    b_int = int(b)
    result = a_int / b_int

except (TypeError, ValueError, ZeroDivisionError):
    print("Какая-то ошибка, запусти еще раз")

else:
    print(result)

