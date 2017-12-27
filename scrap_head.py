'''
Head File: designate .scrap head source file and process input options.
Calls preproccesor and then compile.
'''

from scrap_preprocessor import Preprocessor
from scrap_compile import Compile
from scrap_error import *
import argparse


# create argument parser and parse arguments
parser = argparse.ArgumentParser(description='scrap toolbox')
parser.add_argument('--verbose-compile', '--vc', action='store_true', default=False, dest='verbose_compile', help='displays preprocessor and compile time output')
args = parser.parse_args()


# get file name for script
script_name = 'script.scrap'


# read in script_file
with open(script_name) as script_file:
	script_text = script_file.read()


# process
preprocessor = Preprocessor(script_text)
processed_text = preprocessor.process()

if args.verbose_compile:
	print('~~~~~~~~~~~~~~~\nPREPROCESSED TEXT\n~~~~~~~~~~~~~~~\n' + str(script_text))
	print('~~~~~~~~~~~~~~~\nPROCESSED TEXT\n~~~~~~~~~~~~~~~\n' + str(processed_text) + '\n')


# compile
compiler = Compile(processed_text)
compiler.compile()






