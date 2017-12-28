'''
preprocessor class is intended to format and replace any preprocessor directives.
does not alter the functionality of the input code.
'''
import re

class Preprocessor:

	def __init__(self, source):
		self.source = source
	

	def process(self, optimized=False):
		out = self._swap_block(self.source)
		out = self._remove_empty_lines(out)
		return out	

	'''
	replaces block argument with block argument. i.e.:
		foreach file in files:
			load file
			replace "mispeled wrd" with "misspelled word"
			write to file
		~~~~~~~~~~~ CHANGES TO ~~~~~~~~~~~~~~~
		foreach file in files : {load file; replace "mispeled wrd" with misspelled word"; write to file}
	'''
	def _swap_block(self, source):
		for match in re.finditer(r':\n((\t[^\n]*\n)*)', source):
			block = ' : {' +  match.group(0).replace(':', '').replace('\n', ';').replace('\t', '') + '}'
			# remove first and last ';', because before it is shaped '{;command;...;command;}'
			block = block[:4] + block[5:-2] + block[-1]
			source = source[:match.start()] + block + source[match.end():]
		return source

	
	'''
	removes empty lines from the source
	'''
	def _remove_empty_lines(self, source):
		return '\n'.join( [line for line in source.split('\n') if line.strip()] )







