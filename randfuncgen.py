#!/usr/bin/python

import argparse, string
from random import choice

parser = argparse.ArgumentParser(description = 'ep1c p4st1ng t00l')
parser.add_argument('num', help='amount of lines', type=int)
parser.add_argument('--digitnum', default='6', help='the amount of digits for the ints\' values', dest='digitnum', type=int)
parser.add_argument('--namelen', default='12', help='length of the random generated variable names and strings', dest='namelen', type=int)
parser.add_argument('--strlen', default='16', help ='length of the random generated variable content (strings)', dest='strlen', type=int)
parser.add_argument('--funccount', default='1', help='amount of functions to generate', dest='funccount', type=int)
parser.add_argument('--path', default='out.cpp', help='path where the output will be saved, either a direct path or <filename> for current directory', dest='path')
args = parser.parse_args()

chars = string.ascii_uppercase + string.ascii_lowercase
numbers = "123456789"

def makename():
	return "".join(choice(chars) for i in range(0,args.namelen))

def strcont():
	return "".join(choice(chars) for i in range(0,args.strlen))

def main():
	x = 1
	with open(args.path, '+w') as file:
		file.write('#include <string>\n#include <iostream>\n#include <stdio.h>\n\n')
		while x <= args.funccount:
			file.write(f'void {makename()}()' + '{\n')
			i = 0
			while i <= args.num:
				type = choice(['b', 's', 'i', 'if'])
				if type == "b":
					boolstat = choice(['true', 'false'])
					file.write(f'    bool {makename()} = {boolstat};' + '\n')
				if type == "s":
					cont = choice(['true', 'false'])
					if cont == 'true':
						file.write(f'    std::string {makename()} = "{strcont()}";' + '\n')
					else:
						file.write(f'    std::string {makename()};' + '\n')
				if type == "i":
					digits = "".join(choice(numbers) for i in range(0,args.digitnum))
					file.write(f'    int {makename()} = {digits};' + '\n')
				if type == "if":
					epicname = makename()
					boolstat = choice(['true', 'false'])
					file.write(f'    bool {epicname} = {boolstat};' + '\n')
					file.write(f'    if({epicname} == true)' + '{' + f'{epicname} = false;' + '}\n')
				i += 1
			x += 1
			file.write('}\n\n')
		print('done. file is in the directory you ran the program in.')

if __name__ == '__main__':
	main()
