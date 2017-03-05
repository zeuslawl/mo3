# coding: utf8
""" 
Ejercicio-condicion-chunga     Alejandro López

 Lee un número del teclado 
 Si es:
 -par
 -entre -10 y 40
 -negativo
"""

num=int(raw_input("introduce un número:"))
if (num%2 == 0) : 
	print 'Es par' 
if (num >= -10 and num <= 40) :
	print 'Entre -10 y 40'
if (num<0) :
	print 'Negativo'
