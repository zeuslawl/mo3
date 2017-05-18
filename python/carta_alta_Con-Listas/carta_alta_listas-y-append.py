#!/usr/bin/env python
# -*- coding: utf-8 -*-
#############################################################################
#				nivel Explicación                           #
#############################################################################  
#Juego de cartas en el que hay dos jugadores que se generan dos cartas aleatoriamente y el que tenga el número mas grande gana.


#############################################################################
#				nivel Import                                #
#############################################################################  
#importamos random para que lo haga aleatoriamente.
import random

#############################################################################
#				nivel Variables globales                    #
#############################################################################  
salir= False

#Creamos las listas.
numeros=[1,2,3,4,5,6,7,8,9,10]

palos=[]

numeros.append("J")
numeros.append("Q")
numeros.append("K")

palos.append("Diamante")
palos.append("Corazones")
palos.append("Trebol")
palos.append("Picas")

#############################################################################
#				nivel tirada                                #
#############################################################################  

#Random choice es para que te genere un numero al azar de la lista numeros y palos.

jugador1=random.choice(numeros)
jugador2=random.choice(numeros)

palo1=random.choice(palos)
palo2=random.choice(palos)

#############################################################################
#				nivel 3                                     #
#############################################################################  

def empate():
	
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "HAS EMPATADO"
			
def ganador():
	
	if(jugador1 > jugador2):
		
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "¡Ha ganado el jugador 1!"
	else:	
		print "El jugador 1 tiene un", jugador1, "de", palo1
		print "EL jugador 2 tiene un", jugador2, "de", palo2
		print "¡Ha ganado el jugador 2!"


#############################################################################
#				nivel 2                                     #
#############################################################################  

def jugada():
	
	if(jugador1==jugador2):
		
			empate()
			
	else:
		
		ganador()

#############################################################################
#				nivel 1                                     #
#############################################################################  	
		
while(salir==False):
			
	jugada()
	
	salir=True
