# !/usr/bin/python
# -*-coding: utf-8-*-


import os
os.system('clear')

#Ponemos el número que queremos que empiece a contar.
numero = 1
sortir = False

while sortir == False :
#imprimirá el numero que esta contando
	print "El número es", numero
  
	#Hasta el número 50 y cuando llegue saldrá del bucle.
  
	if(numero == 50) :
		sortir = True
		 
numero = numero + 1
