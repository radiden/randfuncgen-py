#!/usr/bin/python

import argparse, string
from random import choice

parser = argparse.ArgumentParser(description = 'ep1c p4st1ng t00l')
parser.add_argument('num', help='amount of lines', type=int)
args = parser.parse_args()

chars = string.ascii_uppercase + string.ascii_lowercase
numbers = "123456789"

def makename():
	return "".join(choice(chars) for i in range(0,12))

def main():
	with open('out.cpp', '+w') as file:
		file.write('#include <string>\n#include <iostream>\n#include <stdio.h>\n\nusing namespace std;\n')
		file.write(f'void {makename()}()' + '{\n')
		i = 0
		while i < args.num:
			type = choice(['b', 's', 'i', 'if'])
			if type == "b":
				boolstat = choice(['true', 'false'])
				file.write(f'    bool {makename()} = {boolstat};' + '\n')
			if type == "s":
				cont = choice(['true', 'false'])
				if cont == 'true':
					file.write(f'    string {makename()} = "{makename()}";' + '\n')
				else:
					file.write(f'    string {makename()};' + '\n')
			if type == "i":
				digits = "".join(choice(numbers) for i in range(0,6))
				file.write(f'    int {makename()} = {digits};' + '\n')
			if type == "if":
				epicname = makename()
				boolstat = choice(['true', 'false'])
				file.write(f'    bool {epicname} = {boolstat};' + '\n')
				file.write(f'    if({epicname} == true)' + '{' + f'{epicname} = false;' + '}\n')
			i = i + 1
		file.write('}')
		print('done. file is in the directory you ran the program in.')

if __name__ == '__main__':
	main()