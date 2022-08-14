
staff_list = {
    "Мария А": "Фронтендер",
    "Алексей А": "Фронтендер",
    "Иван Б": "Бэкендер",
    "Тоня И": "Бэкендер",
    "Дарья У": "Тестировщик",
    "Валерия К": "Бэкендер",
    "Дарья У": "Тестировщег",
}

fio_list = []
speciality = input("Введите специальность: ")

for it_key, it_value in staff_list.items():
    if it_value.lower() == speciality.lower():
        fio_list.append (it_key)

fio_str = ", ".join(fio_list)
print (fio_str)
