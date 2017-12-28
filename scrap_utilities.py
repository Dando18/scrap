'''
Utility functions for scrap
'''
from scrap_variable import *
from scrap_error import *
import re
import sys


def is_string(string):
	return re.match(r'"(.*?)"', string) is not None	


def is_regex(string):
	return re.match(r'r"(.*?)"', string) is not None


def kill(message):
	sys.exit(str(message))


def write_to_file(filename, content, append=False, line_number=-1):
	try:
		f = open(filename, ('a' if append else 'w'))
	except IOError:
		print_error('I/O Error', 'File \'' + filename + '\' could not be opened.', line_number, kill=True)

	with f:
		f.write(content)


def read_from_file(filename, line_number=-1):
	try:
		f = open(filename, 'r')
	except IOError:
		print_error('I/O Error', 'File \'' + filename + '\' could not be read.', line_number, kill=True)
	
	with f:
		return f.read()
	


'''
Attempts to get a string from a variable. If type is STRING or NUMERIC, then data is returned
in string form. If type is FILE, then the file is read into the string. Else 'None' is returned.
'''
def read_string_from_variable(var):
	if var.type_t is Type.STRING:
		return var.data
	elif var.type_t is Type.FILE:
		return read_from_file(var.data)
	elif var.type_t is Type.NUMERIC:
		return str(var.data)
	else:
		return None
		

'''
writes a string into a var. methods pends on its type.
'''
def write_string_to_variable(var, string):
	if var.type_t is Type.STRING:
		var.data = string
	elif var.type_t is Type.FILE:
		write_to_file(var.data, string)
	elif var.type_t is Type.NUMERIC:
		var.data = string
		var.type_t = Type.STRING





