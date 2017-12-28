'''
Utility functions for scrap
'''
import re

def is_string(string):
	return re.match(r'"(.*?)"', string) is not None	


def is_regex(string):
	return re.match(r'r"(.*?)"', string) is not None




