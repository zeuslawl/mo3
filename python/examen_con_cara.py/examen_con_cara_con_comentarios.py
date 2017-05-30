# !/usr/bin/python
# -*-coding: utf-8-*-

#Bucle en el que printeamos una cara
#Para ello necesitamos utilizar el for y saber las vueltas que necesitamos
#Para la fila 1 y la fila 4 que son los extremos, ponemos un *


def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

for fil in my_range(1,4,1):
	for col in my_range(1,8,1):
		if(fil==1):
			print "*",
		elif (fil==4):
			print "*",
      #Aqui asignamos los valores para conseguir la cara.
		else:
			if(fil==2 and col==1) or (fil==2 and col==8) or (fil==3 and col==1) or (fil==3 and col==8):
				print "*",
			elif (fil==2 and col==4) or (fil==2 and col==5):
				print ".",
			elif (fil==3 and col==4):
				print "\\",
			elif (fil==3 and col==5):
				print "/",
			else:
				print " ",
print ""
