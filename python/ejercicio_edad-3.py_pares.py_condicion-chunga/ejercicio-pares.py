# coding: utf8
"""
Ejercicio-pares    Alejandro López

 Lee un número del teclado
 Si es par: Escribe "Qué bonito número par"
 Si es impar: Escribe "Qué número más vulgar"
 Pista usar módulo %
 """
 
num=int(raw_input("introduce un número:"))
if (num%2 == 0) : 
	print 'Qué bonito número par' 
if (num%2 != 0) :
	print 'Qué número más vulgar' 
 
