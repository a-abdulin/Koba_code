import json


class Candidates:
    def __init__(self, id='', name='', picture='', position='', gender='', age=0, skills=''):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

    def __repr__(self):
        return f'{self.id}; {self.name}; {self.position}; {self.gender}; {self.age}; {self.skills}\n'