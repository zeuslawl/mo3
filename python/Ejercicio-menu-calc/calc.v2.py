# !/usr/bin/python
# -*- coding: utf-8 -*-


"""
Calculadora Básica
""" 

import os

os.system('clear')

print 'Qué desea hacer el amo?'
print '1.- Sumar'
print '2.- Restar'
print '3.- Multiplicar'
print '4.- Dividir'
print '5.- Salir'

opcion = raw_input('Elija una opcion ---> ')

os.system('clear')

if opcion == '1':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	
	suma = numero1 + numero2
	print 'El resultado es ', suma
 
if opcion == '2':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	resta = numero1 - numero2
	print 'El resultado es ', resta
 
if opcion == '3':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	multi = numero1 * numero2
	print 'El resultado es ', multi
 
if opcion == '4':
	numero1 = float(raw_input('Introduce un numero -> '))
	numero2 = float(raw_input('Introduce otro numero -> '))
	divi = numero1 / numero2
	print 'El resultado es ', divi
    
if opcion == '5':
	exit
	print 'Has salido'
