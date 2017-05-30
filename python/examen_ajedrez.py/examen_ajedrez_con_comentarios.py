# coding: utf-8

#Bucle en el que la idea es simular un tablero de ajedrez donde hay una ficha blanca y otra negra.
#La forma de hacerlo es utilizando el modulo y cada casilla par le ponemos un * que simula la negra. Sino lo dejamos en blanco.


def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici=inici+increment
		
for fil in my_range(1,8,1):
	for col in my_range(1,8,1):
		if (fil%2==0 and col%2==0):
			print "*",
		else:
			print " ",
print ""
