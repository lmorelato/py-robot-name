import random
from string import ascii_uppercase

class Robot(object):
	def __init__(self):
		self.name = self.name_generator()		
		
	def reset(self):
		random.seed(random.random())
		self.name = self.name_generator()	
		
	def name_generator(self):	
		prefix = ''.join(random.choices(ascii_uppercase, k=2))
		serial = ''.join(random.choices('0123456789', k=3))
		return prefix + serial