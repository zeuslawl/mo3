# coding: utf-8

# Importar calendario
import calendar

# Def para que funcione el my_range
def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

print "L,M,X,J,V,S,D"

cont=1
num_dias_mes=num_dias
dia_semana=dia_sem

for fil in my_range(1,6,1):
	for col in my_range(1,7,1):
		if(col==num_dias_mes):
			print cont,
			cont=cont+1
		else:
			print " ",
	print ""
	
for col in my_range(1,7,1):
	if(col==dia_semana):
		print " ",

for col in my_range(1,7,1):
	print cont
	cont=cont+1

for fil in my_range(1,6,1):
	for col in my_range(1,7,1):
		if(col==num_dias_mes):
			print cont,
			cont=cont+1
		else:
			print " ",
	print ""
