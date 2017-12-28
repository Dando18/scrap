'''
a list of Expression objects
'''
import scrap_utilities as util
from scrap_expression import Expression
from scrap_error import *
from scrap_variable import *
import re

expression_list = []

'''
returns the expression with the given key.
Note: will return the first expression with the key,
however, duplicate keys are not expected.
'''
def get_expression(key):
	for expression in expression_list:
		if expression.key == key:
			return expression
	return None

''' LOAD
	
	loads a file into a variable or variable into primary. If not a string, then sets primary to variable name.	
	USES:
		load _1_ ?( into _2_)
			1: string (file) or file type
			2: variable
			~ loads contents of 1 into 2 or primary
	load "file.txt" into text
	load "file.txt"

'''
def load_func(args, compiler):
	print('load_func with args=' + str(args))
	
	# set file and load contents
	if util.is_string(args[0]):
		file_name = args[0][1:-1]
	elif compiler.var_stack.contains_name(args[0]):
		var = compiler.var_stack.get_variable(args[0])
		file_name = compiler.var_stack.get_variable(args[0]).data
	else:
		print_error('Syntax Error', 'The format of \'load\' is \'load _1_ ?( into _2_ )\'. Parameter 1 has to be a filename in quotes or a variable with type STRING or FILE', compiler.cur_line, kill=True)

	content = util.read_from_file(file_name)
	if content is None:
		print_error('I/O Error', 'Unable to read file. Check file permissions and/or existence.', compiler.cur_line, kill=True)

	# load into primary or given variable
	if len(args)>1 and args[1] is "into":
		compiler.var_stack.set( Variable(args[2], content, Type.STRING) )
	else:
		compiler.var_stack.set_primary( content, Type.STRING)	
	return			

expression_list.append( Expression("load", 'load _1_ ?(into _2_)', load_func) )



''' REPLACE

	replaces a string/regex with a string. Uses primary unless ended with in <var>.
	USES:
		replace _1_ with _2_ ?( in _3_ )
			1: regex or string
			2: string or variable with string type
			3: variable with string or file type
		replace _1_ ?( in _2_)
			1: regex or string
			2: variable with string or file type
			~ replaces 1 with empty string "" in primary or 2		
	EXAMPLES:
		replace "old" with "new"
		replace r"[^A-Za-z]" with "" in var
		replace " "
'''
def replace_func(args, compiler):
	print('replace_func with args=' + str(args))
	
	# determine variable
	if args[-2] is 'in':
		var = compiler.var_stack.get_variable(args[-1])
		if var is None:
			print_error('Unkown Variable', 'The variable '+args[-1]+' does not exist.', compiler.cur_line, kill=True)
	else:
		var = compiler.var_stack.get_primary()
	
	# main string to be manipulated
	string = util.read_string_from_variable(var)
	if string is None:
		print_error('Invalid Argument', 'variable expected to be of type file, string, or numeric', compiler.cur_line, kill=True)	
	
	# new string
	if args[1] is 'with':
		new = args[2]
	else:
		new = ''

	# old string to replace with new
	if util.is_string(args[0]):
		old = args[0][1:-1]
		string = string.replace(old, new) 
	elif util.is_regex(args[0]):
		old = args[0][2:-1]
		string = re.sub(old, new, string)			
	else:
		print_error('Invalid Argument', 'First argument should either be a string or regex.', compiler.cur_line, kill=True)
 
	# rewrite
	util.write_string_to_variable(var, string) 
	return

expression_list.append( Expression("replace", 'replace _1_ ?(with _2) ?(in _3_)', replace_func) )


''' WRITE
	
	writes a string to a file
	USES:
		write ?(_1_) to _2_
			1: string or variable with string type
			2: string (filename) or variable with file type
			~ writes 1 or primary to 2
	EXAMPLES:
		write "new file text" to "out_file.txt"
		write text_var to "out_file.txt"
		write to "out_file.txt"
'''
def write_func(args, compiler):
	print('write_func with args=' + str(args))
	return

expression_list.append( Expression("write", 'write ?(_1_) to _2_', write_func) )





