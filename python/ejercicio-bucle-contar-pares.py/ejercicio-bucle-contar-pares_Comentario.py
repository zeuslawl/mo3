# !/usr/bin/python
# -*- coding: utf-8-*-

num = 1
final = input("Introduce un numero: ")
salir = False

#Bucle que el usuario pone el numero final y te va contando los pares que hay.

while salir == False:

#Para ello ponemos el módulo %2 y cuando llega hasta el numero final sale del bucle

	if (num % 2 == 0):
		print  num
	if (num == final):
		salir = True
	num=num+1
