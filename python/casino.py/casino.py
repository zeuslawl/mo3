#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

saldo = 100
intentos = 0

salir1= False
salir2= False


while(salir1==False):
		print " Tienes este", saldo, "€"
		print " Para abandonar pon -1"
	
		apuesta = input("De cuanto es su apuesta? "	
	
		if ( saldo <10)
			print " Tienes este", saldo, "€"
			print " No tienes suficiente dinero para apostar"
		
		if ( apuesta == -1 or saldo < 10 or intentos == 2):
		
			salir1= True
	
		if (apuesta > saldo):
			print "No tienes ese dinero para apostar!"
	
		else: 
			if ( apuesta < 10):
			print " Lo mínimo que puedes apostar son 10 €"
			intentos = intentos + 1
		else: 
			
			if (apuesta <= saldo and apuesta >10):
				
				while (salir2 == False):
			
					palo = randint(1,4)
				
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
				
					jugador1 = randint(2,14)
					jugador2 = randint(2,14)	
				
					if(jugador1==11):
						jugador1="J"
						
					if(jugador1==12):
							jugador1="Q"
						
					if(jugador1==13):
							jugador1="K"
								
					if(jugador1==14):
							jugador1="AS"
								
					if(jugador2==11):
							jugador2="J"
							
					if(jugador2==12):
							jugador2="Q"
							
					if(jugador2==13):
							jugador2="K"
								
					if(jugador2==14):
							jugador2="AS"
								
					if(jugador1==jugador2):
					
						print "¡Empate!"
						print "El jugador 1 tiene un", jugador1, "de", palo1
						print "EL jugador 2 tiene un", jugador2, "de", palo2
						print "HAS EMPATADO"
						saldo = saldo - apuesta
				else:
					if(jugador1 > jugador2):
					
						print "El jugador 1 tiene un", jugador1, "de", palo1
						print "EL jugador 2 tiene un", jugador2, "de", palo2
						print "¡Ha ganado el jugador 1!"
						saldo = saldo + (apuesta*2)
					else:	
						print "El jugador 1 tiene un", jugador1, "de", palo1
						print "EL jugador 2 tiene un", jugador2, "de", palo2
						print "¡Ha ganado el jugador 2!"
						saldo = saldo - apuesta
						
						salir2=True
