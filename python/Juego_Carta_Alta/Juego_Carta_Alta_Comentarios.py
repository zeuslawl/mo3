#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Juego de cartas en el que hay dos jugadores que se generan dos cartas aleatoriamente y el que tenga el número mas grande gana.
from random import randint

salir= False

while(salir==False):

#Randint es para generar aleatoriamente las jugadas.

	jugador1=randint(1,13)
	jugador2=randint(1,13)
	
	palo=randint(1,4)

#Asignamos cada numero con su simbolo 

	if(palo==1):
		palo1= "Picas"
	
	if(palo==2):
		palo1= "Diamantes"

	if(palo==3):
		palo1= "Trebol"
	
	if(palo==4):
		palo1= "Corazones"
		
	palo=randint(1,4)
	
	if(palo==1):
		palo2= "Picas"
	
	if(palo==2):
		palo2= "Diamantes"

	if(palo==3):
		palo2= "Trebol"
	
	if(palo==4):
		palo2= "Corazones"
		
#Aqui calculamos quien gana y quien empata.

	if(jugador1==jugador2):
		print "¡Empate!"
		
	else:
		if(jugador1 > jugador2):
			if(jugador1==11):
				jugador1="J"
			
			if(jugador1==12):
				jugador1="Q"
			
			if(jugador1==13):
				jugador1="K"
			
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "¡Ha ganado el jugador 1!"
		else:
			if(jugador2==11):
				jugador2="J"
			
			if(jugador2==12):
				jugador2="Q"
			
			if(jugador2==13):
				jugador2="K"
				
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "¡Ha ganado el jugador 2!"
			
		salir=True
