#!usr/bin/env python
#encoding: latin1

byte = raw_input("Coloque el binario en forma de octeta (byte): ")
valor = 128
numero = 0
for x in range(len(byte)):
	if "1" == byte[x]:
		numero += valor
	else:
		numero += 0
	valor = valor / 2
print "El valor decimal es", numero
