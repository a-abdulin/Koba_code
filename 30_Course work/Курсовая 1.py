# Курсовая 1

# Активируем библиотеку random для активации случайных чисел (на всякий случай :)
import random

# Задаем словарь Морзе и список слов
morse_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}
words = ['code', 'bit', 'list', 'soul', 'next', 'mail', 'voice', 'monk', 'coffee', 'tea']


def morse_encode(word):
    """
    Описываем функцию шифрования слова по Морзе
    """
    morse_code = ''
    for letter in word:
        if letter not in morse_dict.keys():
            return 'Не корректное слово'
            break
        else:
            morse_code += morse_dict.get(letter)
    return morse_code


def get_word():
    """
    Описываем функцию - случайное слово из списка
    """
    # print (words_)
    return random.choice(words)


# Начало основного кода
input('''Сегодня мы потренируемся расшифровывать азбуку Морзе. Нажмите Enter и начнем''')

answers = []
number_of_questions = 5
q = 1

# Основной цикл программы. Берет случайное слово из списка, кодирует, сравнивает с ответом пользователя, комментирует и считает ответы
while q <= number_of_questions:
    rand_word = get_word()
    morse_code = morse_encode(rand_word)
    answer = input(f'Слово {q} {morse_code} ')
    if answer == rand_word:
        print(f'Верно, {rand_word}!')
        answers.append(True)
    else:
        print(f'Неверно, {rand_word}!')
        answers.append(False)
    q += 1

# Вывод результатов
print(f'\nВсего задачек: {number_of_questions}')
print(f'Отвечено верно: {answers.count(True)}')
print(f'Отвечено неверно: {answers.count(False)}')
