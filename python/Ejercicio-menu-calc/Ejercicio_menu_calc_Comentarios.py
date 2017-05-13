# !/usr/bin/python
# -*- coding: utf-8 -*-

#Ejercicio muy sencillo en el uqe preguntamos al amo que desea hacer y si pulsamos una tecla que no existe te sale que esa opción no existe.
import os

os.system('clear')

print 'Qué desea hacer el amo?'
print 'S.- Salir'
print '1.- Sumar'
print '2.- Restar'
print '3.- Multiplicar'
print '4.- Dividir'

opcion = raw_input('Elija una opcion ---> ')



if (opcion >= "1" and opcion  <= "4") or (opcion == "S") or (opcion == "s") :
	print "Correcto"
else:
	print " Error, esa opcion no existe"
