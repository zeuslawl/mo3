# !/usr/bin/python
# -*-coding: utf-8-*-

#Ejercicio del examen que hicimos de python.
#Igual que el con cara pero sin asignar los valores de la cara. (Más sencillo)

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
		else:
			if(fil==2 and col==1) or (fil==2 and col==8) or (fil==3 and col==1) or (fil==3 and col==8):
				print "*",
			else:
				print " ",
print ""
