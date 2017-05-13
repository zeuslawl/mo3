#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio de contar del 1 al 3

contador=1
salir= False
#Bucle donde printeamos contador y empieza en el 1 al llegar al 3 sale del bucle.
while(salir==False):
	print contador
	if(contador==3):
		salir=True
	contador= contador +1
