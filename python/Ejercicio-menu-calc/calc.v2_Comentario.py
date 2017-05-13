# !/usr/bin/python
# -*- coding: utf-8 -*-


"""
Calculadora Básica
""" 

import os

os.system('clear')

#Preguntamos al amo que desea hacer si sumar, restar,multiplicar,dividir o salir

print 'Qué desea hacer el amo?'
print '1.- Sumar'
print '2.- Restar'
print '3.- Multiplicar'
print '4.- Dividir'
print '0.- Salir'

opcion = raw_input('Elija una opcion ---> ')

os.system('clear')

#La operacion de sumar

if opcion == '1':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	
	suma = numero1 + numero2
	print 'El resultado es ', suma
 
#La operacion de restar

if opcion == '2':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	resta = numero1 - numero2
	print 'El resultado es ', resta


#La operacion de multiplicar
 
if opcion == '3':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	multi = numero1 * numero2
	print 'El resultado es ', multi
 
#La operacion de dividir
 
if opcion == '4':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	divi = numero1 / numero2
	print 'El resultado es ', divi
    
 # Si queremos salir pulsamos el 0   
if opcion == '0':
	exit
	print 'Has salido'
