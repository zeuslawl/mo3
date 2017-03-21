# !/usr/bin/python
# -*-coding: utf-8-*-

import os
os.system('clear')

salir = False

while(salir==False) :

		print("hola")
		tecla = raw_input("Para salir teclee s o S ---> ")
		if(tecla=="S") or (tecla =="s") :
			print ("Adiós")
			salir=True
