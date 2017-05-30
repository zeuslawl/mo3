# !/usr/bin/python
# -*-coding: utf-8-*-

#Para utilizar el my_range utilizamos el def

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

#Este bucle es del examen que al final se suspendio.
#Va por coordenadas como los anterios de examen_con_cara y sin cara.
#Asignar donde queremos la A,B,C y en el resto -

for fil in my_range(1,5,1):
	for col in my_range(1,4,1):
		if (fil ==1):
			if (col ==2):
				print "A",
			elif col ==3:
				print "B",
			elif col==4:
				print "C",
			else:
				print "-",
		else:
			if(col==1):
				print fil-1,
			else:
				if(fil==3 and col ==3) or (fil==4 and col==2):
					print "*",
				else:
					print "-",
	print ""

