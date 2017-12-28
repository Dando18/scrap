'''
Utility functions for scrap
'''
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
	


