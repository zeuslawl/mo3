# !/usr/bin/python
# -*- coding: utf-8-*-

import os

os.system('clear')

salir = False

#Bucle sencillo en el que printeamos que desea hacer el amo y si le da a las opciones sale del bucle sinó, te dice que esa opcion no existe.

while salir == False :
	
		print 'Qué desea hacer el amo?'
		print 'S.- Salir'
		print '1.- Sumar'
		print '2.- Restar'
		print '3.- Multiplicar'
		print '4.- Dividir'

		opcion = raw_input('Elija una opcion ---> ')
		

		if ( opcion >= "1" and opcion <= "4") or (opcion == "S") or (opcion == "s") :
				
				print "Correcto"
				salir = True
				
		else: 
				print "Error, esa opcion no existe"
