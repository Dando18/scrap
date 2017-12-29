'''
Expression class; 
initialize each expression with:
	load = Expression('load', 'load _1_ ?( into _2_)', func)
'''

class Expression:
	
	def __init__(self, key, use, func):
		self.key = key
		self.use = use
		self.func = func

	
	'''
	args is expected to be a list of strings
	'''
	def execute(self, args, compiler):
		self.func(args, compiler)



