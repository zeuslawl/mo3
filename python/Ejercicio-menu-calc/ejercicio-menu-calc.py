# !/usr/bin/python
# -*- coding: utf-8 -*-


""" 
Calculadora Básica
""" 
numero1 = int(raw_input('Introduce un numero -> '))
numero2 = int(raw_input('Introduce otro numero -> '))

print 'Qué desea hacer el amo?'
print '1.- Sumar'
print '2.- Restar'
print '3.- Multiplicar'
print '4.- Dividir'
print '5.- Salir'

 
opcion = raw_input('Elija una opcion ---> ')
if opcion == '1':
    suma = numero1 + numero2
    print 'El resultado es ', suma
 
if opcion == '2':
    resta = numero1 - numero2
    print 'El resultado es ', resta
 
if opcion == '3':
    multi = numero1 * numero2
    print 'El resultado es ', multi
 
if opcion == '4':
    divi = numero1 / numero2
    print 'El resultado es ', divi
    
if opcion == '5':
	exit
	print 'Has salido'


