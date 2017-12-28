'''
variable manager class;
contains get, set methods taking variable name
'''
from scrap_variable import *

class VariableManager:
	
	'''
	VariableManager class. Maintains a list of Variable objects and is responsible
	for adding, deleting, and returning variables given their name. Initializes
	with the primary variable named '__primary__'
	'''
	def __init__(self):
		self.vars = [Variable("__primary__", "", Type.STRING)]

	
	'''
	returns True if a variable exists with the given name. False otherwise.
	'''
	def contains_name(self, name):
		return any(var.name == name for var in self.vars)

	
	'''
	adds a new variable to the variable list. If the variable already exists, then it overwrites
	the data and type_t, else it adds a completely new variable.
	'''
	def set(self, variable):
		for i, var in enumerate(self.vars):
			if var.name is variable.name:
				var.set_all(variable.name, variable.data, variable.type_t)
				break
		else:
			self.vars.append(variable)	

	
	'''
	sets the primary variable to the data and type_t provided
	'''
	def set_primary(self, data, type_t):
		for var in self.vars:
			if var.name is '__primary__':
				var.data = data
				var.type_t = type_t
				return

	
	'''
	removes the variable with the given name from the variable list. 
	If variable does not exist, then it does nothing.
	'''
	def remove(self, name):
		for i, var in enumerate(self.vars):
			if var.name is name:
				del self.vars[i]
				break

	'''
	returns the variable with the given name. If no variable exists with the name, then returns None
	'''
	def get_variable(self, name):
		for var in self.vars:
			if var.name is name:
				return var
		return None

	def get_primary(self):
		return self.get_variable('__primary__')			







