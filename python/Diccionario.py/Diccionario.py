# !/usr/bin/python
# -*-coding: utf-8-*-

salir = False
num = 1
top_mejores_jugadores = {1: "Leo Messi", 2: "Cristiano Ronaldo", 3: "Antoine Griezmann"}

print "Mejores Futbolistas"

print "------------------"


while salir == False :
	
	
	print top_mejores_jugadores[num]
	if num == len(top_mejores_jugadores) :
		
		salir = True
	num = num + 1
