# !/usr/bin/python
# -*- coding: utf-8-*-

#Versión 1 de pi_pa_ti
#Bucle en el que eliges la "tirada" de jugador 1 y la "tirada" de jugador 2 y de ahí sale el ganador o empate

j1 = raw_input("Opción para el Jugador 1: piedra, papel o tijera. ")

j2 = raw_input("Opción para el Jugador 2: piedra, papel o tijera. ")

if (j1 == "piedra") and (j2 == "piedra"):
	print "¡Empate!"
		
if (j1 == "piedra") and (j2 == "papel"):
	print "¡Gana el Jugador 2!"
	
if (j1 == "piedra") and (j2 == "tijera"):
	print "¡Gana el Jugador 1!"
	
		
if (j1 == "papel") and (j2 == "papel"):
	print "¡Empate!"
	
if (j1 == "papel") and (j2 == "piedra"):
	print "¡Gana el Jugador 1!"
	
if (j1 == "papel") and (j2 == "tijera"):
	print "¡Gana el Jugador 2!"
	
	
if (j1 == "tijera") and (j2 == "tijera"):
	print "¡Empate!"
	
if (j1 == "tijera") and (j2 == "piedra"):
	print "¡Gana el Jugador 2!"
	
if (j1 == "tijera") and (j2 == "papel"):
print "¡Gana el Jugador 1!"
