'''
Expression class; 
initialize each expression with:
	load = Expression('load', func)
'''

class Expression:
	
	def __init__(self, key, func):
		self.key = key
		self.func = func

	
	'''
	args is expected to be a list of strings
	'''
	def execute(self, args, compiler):
		self.func(args, compiler)



