# !/usr/bin/python
# -*- coding: utf-8 -*-

import os

os.system('clear')

valor1 = input("Introduce un valor: ")
valor2 = input("Introduce un valor: ")

if valor1 > valor2 :
	print "Valor 1 es mayor que valor 2"
else :
	if valor1 == valor2 :
		print "Valor 1 es igual a valor 2"
		
	else :
		print "Valor 2 es mayor a valor 1"
