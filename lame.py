prg = input()
base = "hello"
#$ %^ -> "hello"
#abc $ % ^ -> abc
#$ % hello ->

if '$' in prg:
	split = prg.split('$')
	var = base if split[0] == '' else split[0].replace(' ', '')
	prg = split[1]
else:
	var = base

prg = prg.replace(' ', '').split('^')[0]
if prg == '': prg = var
if '%' in prg:
	prg = prg.replace('%', var)

if '@' in prg:
	split = prg.split('@')
	print(split[0]==split[1])
else:
	print(prg)
