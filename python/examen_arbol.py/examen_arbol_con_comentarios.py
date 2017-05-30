# !/usr/bin/python
# -*-coding: utf-8-*-

#Bucle en el que simulamos un arbol, para ello necesitamos hacer un for y si la casilla es 4 le ponemos una A.
#Lo mismo si la casilla es fila 3 y col 2,3 y 4 le ponemos una A (son las ramas)
#Si es fil 2 y col 3 una A (con esto ya tenemos las ramas hechas)
#Si es fila 1 y col 3 le ponemos un * (es la estrella)
#Si es fila 5 y col 3 o fila 6 y col 3 le ponemos una N que es el tronco
#Con esto ya tenemos el arbol hecho!

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

for fil in my_range(1,6,1):
	for col in my_range(1,5,1):
		if(fil==4):
			print "A",
		elif (fil==3 and col==2) or (fil==3 and col==3) or (fil==3 and col==4):
			print "A",
		elif (fil==1 and col==3):
			print "*",
		elif (fil==2 and col==3):
			print "A",
		elif (fil==5 and col==3) or (fil==6 and col==3):
			print "N",
		else:
			print " ",
print ""
