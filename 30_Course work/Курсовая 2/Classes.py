class BasicWord():

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def word_check(self, word_input):
        return word_input.lower() in self.subwords

    def count_words(self):
        return len(self.subwords)

    def __repr__(self):
        return  f'{self.word} ' \
                f'{self.subwords}'

class Player():
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def count_words(self):
        return len(self.used_words)

    def add_word(self, word):
        self.used_words.append(word)

    def already_used_word(self, word):
        return word in self.used_words
