# !/usr/bin/python
# -*-coding: utf-8-*-
#En este bucle ponemos el número final y hasta ese número contará

import os
os.system('clear')

sortir = False
numero = 1
final = input("Hasta que número desea el amo ")

while (sortir == False) :
#Imprime el numero	
	print numero
	#Saldrá del bucle cuando llegue al numero que hemos puesto anteriormente.
	if ( numero == final ) :
		
		sortir = True
		
numero = numero +1
