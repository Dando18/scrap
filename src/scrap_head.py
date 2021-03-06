'''
Head File: designate .scrap head source file and process input options.
Calls preproccesor and then compile.
'''

from scrap_preprocessor import Preprocessor
from scrap_compile import Compile
from scrap_error import *
import scrap_utilities as util
import argparse


# create argument parser and parse arguments
parser = argparse.ArgumentParser(description='scrap toolbox')
parser.add_argument('script_file')
parser.add_argument('--verbose-compile', '--vc', action='store_true', default=False, dest='verbose_compile', help='displays preprocessor and compile time output')
args = parser.parse_args()


# get file name for script and change working directory
script_name = args.script_file
if script_name[-6:] != '.scrap':
	script_name = 'script.scrap'
util.change_working_directory(script_name)


# read in script_file
if args.verbose_compile:
	print('attempting to read ' + script_name + '...')
script_text = util.read_from_file(script_name)
if args.verbose_compile and script_text is not None:
	print_OK('read ' + script_name + ' successfully!\n', checked=True)


# process
if args.verbose_compile:
	print('attempting to preprocess source...')
preprocessor = Preprocessor(script_text)
processed_text = preprocessor.process()

if args.verbose_compile:
	print_heading('PREPROCESSED TEXT')
	print(script_text.strip() + '\n')
	if processed_text is not None:
		print_heading('PROCESSED TEXT')
		print(processed_text + '\n')
		print_OK('preprocessed source successfully!\n', checked=True)


# compile
if args.verbose_compile:
	print('attempting to execute source...')
compiler = Compile(processed_text)
compiler.compile()
if args.verbose_compile:
	print_OK('executed successfully!', checked=True)






