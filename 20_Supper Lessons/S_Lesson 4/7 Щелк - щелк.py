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
}

string_in = input ('Последовательность кода Морзе с пробелом или слово на латинице: ')
string_out = string_in

if string_in.isalpha():
    string_list = list(string_in)
    for i in range (0, len (string_list)):
        if string_list [i].lower () in morse_dict.keys ():
            string_list [i] = morse_dict.get (string_list [i].lower())
    string_out = ' '.join(string_list)
else:
    string_list = string_out.split(' ')
    for letter, code in morse_dict.items():
        while code in string_list:
            string_list [string_list.index (code)] = letter
    string_out = ''.join(string_list)

print (string_out)