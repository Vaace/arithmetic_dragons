# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
class Hero(Attacker):
	def __init__(self, name):
		Hero._health = 100
		Hero._attack = 50
		Hero._experience = 0
		Hero._name = ''
		Hero._level = 1
	def level_up(self):
		if 	self._experience >= 150:
			self._level += 1
			self._health += 10
			self._attack += 5
			self._experience -= 150
	def gameOver(self):
		pass #<FIXME> непонятно, зачем метод нужен
		
