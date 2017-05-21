#!/usr/bin/env python
# coding:utf-8

#Bucle para que cuente hasta 5.(1,2,3,4,5) y luego sume esos números.

import os
os.system('clear')

sortir = False
numero = 1
total = 0

while (sortir==False):
	print numero
#Que cuente hasta 5.
	if(numero==5):
		
		sortir = True 
		print "--"
#Suma los numeros.	
	total= total + numero
	numero= numero +1
print total
