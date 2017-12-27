'''
a list of Expression objects
'''
import scrap_utilities as util
from scrap_expression import Expression

expression_list = []

def get_expression(key):
	for expression in expression_list:
		if expression.key == key:
			return expression
	return None

''' LOAD FUNCTION
	
	loads a file into a variable or variable into primary. If not a string, then sets primary to variable name.	

	load "file.txt" into text
	load "file.txt"
	load text

'''
def load_func(args):
	print('load_func')
	if not util.is_string(args[0]):
		return			

expression_list.append( Expression("load", load_func) )





