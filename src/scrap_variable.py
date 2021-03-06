'''
Variable base class;
holds variable name, type, and data
'''
from enum import Enum


"""
Different types of variable data.
STRING - generic string type. contains only string data. data is the the string
NUMERIC - stored as either floating or integer. pending on how it was set. data is an integer
FILE - simply a reference to a file type. data is the name of the file
"""
class Type(Enum):
	STRING = 1
	NUMERIC = 2
	FILE = 3
	REGEX = 4
	LIST = 5

class Variable:
	
	"""
	variable base type. Holds name of variable, data, and type_t.
	"""
	def __init__(self, name, data, type_t):
		self.name = name
		self.data = data
		self.type_t = type_t


	def set_name(self, new):
		self.name = new

	def set_data(self, new):
		self.data = new

	def set_type_t(self, new):
		self.type_t = new

	def set_all(self, new_name, new_data, new_type_t):
		self.name = new_name
		self.data = new_data
		self.type_t = new_type_t

	def __str__(self):
		return '<var name="'+str(self.name)+'" data="'+str(self.data)+'" type_t="'+str(self.type_t)+'">'



