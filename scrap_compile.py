'''
compiler class;
splits the script into individual statements and executes each one by 
looking up its expression
'''
from scrap_expressions import get_expression
import scrap_utilities as util
from scrap_error import *
from scrap_variable_manager import VariableManager
import re


class Compile():
	
	'''
	sets source to source and splits the source into lines. Expecting expressions are split by '\n'.
	'''
	def __init__(self, source):
		self.source = source
		self.lines = source.split('\n')
		self.var_stack = VariableManager()
		self.cur_line = 0

	
	'''
	iterates thru each line and executes it
	'''
	def compile(self):
		for i, line in enumerate(self.lines):
			self.cur_line = i
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
			util.kill('Execution Failed')		
			return
		expression.execute(args, self)		
		return	




