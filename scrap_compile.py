'''
compiler class;
splits the script into individual statements and executes each one by 
looking up its expression
'''
from scrap_expressions import get_expression
import scrap_utilities as util
from scrap_error import *
import re



class Compile():
	
	'''
	sets source to source and splits the source into lines. Expecting expressions are split by '\n'.
	'''
	def __init__(self, source):
		self.source = source
		self.lines = source.split('\n')

	
	'''
	iterates thru each line and executes it
	'''
	def compile(self):
		for line in self.lines:
			self.execute(line)
	

	'''
	find the expression, parse args, and exec
	'''
	def execute(self, source):
		# split into key and args
		elements = re.findall(r'(?:"[^"]*"|[^\s"])+', source.strip())
		key = elements[0].strip()
		args = elements[1:]		

		# lookup expression and run
		expression = get_expression(key)
		if expression is None:
			print_error('Expression Not Found', 'The used expression \'' + key + '\' does not exist. Try checking the spelling.', 0)
			return
		expression.execute(source)		
		return	




