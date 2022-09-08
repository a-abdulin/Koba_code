import pytest

class Player:

	def __init__(self, name):
		if type(name) != str:
			raise TypeError ("Неправильный тип имени")

		self.name = name
		self.points = 0

	def change_name(self, new_name):
		self.name = new_name

	def add_points(self, number):
		self.points += number

	def get_points(self):
		return self.points

class Test_Player:

	def test_get_name(self):
		player = Player("Никита")
		player.change_name("Слава")
		assert player.name == "Слава", "Ошибка в функции присвоения нового имени"

	def test_str_type_error(self):
		with pytest.raises(TypeError):
			player = Player(123)

