#!/usr/bin/env python
# coding:utf-8

import os
os.system('clear')

sortir = False
numero = 1
total = 0

while (sortir==False):
	print numero

	if(numero==5):
		
		sortir = True 
		print "--"
	
	total= total + numero
	numero= numero +1
print total
