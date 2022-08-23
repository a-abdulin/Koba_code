import json
import requests
import random
from Classes import BasicWord

def word_list():
    content = requests.get ('https://jsonkeeper.com/b/DRBB').json()
    # На всякий случай работает и из файла (не нужно подключаться к интернету)
    # with open('words.json', mode='r', encoding='utf-8') as file:
    #     content = json.load(file)

    word_rand =  random.choice(content)
    word_line = BasicWord(word_rand['word'], word_rand['subwords'])

    return word_line
