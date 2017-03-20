# !/usr/bin/python
# -*- coding: utf-8-*-

import os

os.system('clear')

salir = False

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
