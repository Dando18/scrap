'''
Error and Warning print protocol
'''
import scrap_utilities as util

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def print_error(name, message, line_number, kill=False):
	print(bcolors.FAIL + 'ERROR (' + str(name) + '): ' + str(message) + ' --- at line #' + str(line_number) + bcolors.ENDC)
	if kill:
		util.kill('Fatal Error')

def print_warning(name, message, line_number):
	print(bcolors.WARNING + 'WARNING (' + str(name) + '): ' + str(message) + ' --- at line #' + str(line_number) + bcolors.ENDC)	


def print_heading(title):
	print(bcolors.OKBLUE + bcolors.UNDERLINE + bcolors.BOLD + str(title) + bcolors.ENDC)


def print_OK(text, checked=False):
	print(bcolors.OKGREEN + ('✓' if checked else '') + ' ' + text + bcolors.ENDC) 

