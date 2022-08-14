import json
import requests
from Classes import BasicWord, Player
from utils import word_list

user_name = input ('Введите ваше имя: ')
player = Player(user_name)

print (f'Добрый день, {player.name}!')
game_words = word_list()
print (f'Составьте {game_words.count_words()} слов из слова {game_words.word.upper()}')
# print (f"Список подслов: {', '.join(game_words.subwords)}")
user_word = input ('Поехали! Ваше первое слово? ')
if game_words.word_check(user_word):
    print('Есть такое слово!')
    player.add_word(user_word)
else:
    print('Такого слова нет!')

while player.count_words() < game_words.count_words():
    user_word = input(f'Следующее слово (осталось {game_words.count_words()-player.count_words()})? ')
    if user_word in ['stop', 'стоп']:
        break
    elif player.already_used_word(user_word):
        print('Слово уже использовалось!')
    elif game_words.word_check(user_word) and not player.already_used_word(user_word):
        print('Есть такое слово!')
        player.add_word(user_word)
    else:
        print('Такого слова нет!')

print ('\nСлова закончились!')
print (f'Вы угадали {player.count_words()}!')
print (f"И эти слова: {', '.join(player.used_words)}!")
