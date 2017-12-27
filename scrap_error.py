'''
Error and Warning print protocol
'''

def print_error(name, message, line_number):
	print('ERROR (' + str(name) + '): ' + str(message) + ' --- at line #' + str(line_number))


def print_warning(name, message, line_number):
	print('WARNING (' + str(name) + '): ' + str(message) + ' --- at line #' + str(line_number))	




