# coding: utf-8

# Importar calendario
import calendar

# Def para que funcione el my_range
def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

print "L,M,X,J,V,S,D"

anyo = input('INsifweijfowif año: ')
mes = input('Inserte fueiwhf3uiwehfquiwf mes: ')

cont=1
num_dias_mes=calendar.monthrange(anyo, mes)[1]) 
dia_semana=(calendar.weekday(anyo,mes,1))+1

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
