# coding: utf-8

# Importar calendario
import calendar

# Def para que funcione el my_range
def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment


#Para seleccionar el mes y año que quiere ver el amo.
anyo=input('Introduce el año que desee: ')
mes=input('Introduce el mes que desee: ')


cont=1
#Numero total de dias en el mes que seleccionamos.
num_dias_mes=calendar.monthrange(anyo,mes)[1]
#Dia de la semana que empieza el mes.
dia_semana=(calendar.weekday(anyo,mes,1))+1


for fil in my_range(1,6,1):
	for col in my_range(1,7,1):
		if(fil==1):
			if col==1:
				print "L ",
			if col == 2 :
				print "M ",
			if col == 3 :
				print "X ",
			if col == 4 :
				print "J ",
			if col == 5 :
				print "V ",
			if col == 6 :
				print "S ",
			if col == 7 :
				print "D ",
		elif(fil==2):
			if(dia_semana <= col):
				print cont,
				cont=cont+1
			else:
				print " ",
						
		elif ( cont <=num_dias_mes ):
			print cont,
			cont=cont+1
		
		else:
			print " ",
			
	print ""
			
