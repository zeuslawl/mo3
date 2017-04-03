# !/usr/bin/python
# -*- coding: utf-8-*-

num= 31

salir= False

while (salir==False) :
	
	if (num %7 == 0) or (num %7 ==1) :
		j1= "tijera"
	if (num %7 ==2) or (num %7==3) or (num %7 == 6) :
		j1= "piedra"
	if (num %7 ==4) or (num %7 == 5):
		j1 = "papel"
	if (num %5 ==0) or (num %5 ==1) or (num % 5 ==2):
		j2 = "papel"
	if (num %5 ==3):
		j2= "tijera"
	if (num %5 ==4) :
		j2= "piedra"
	
	if (j1 =="piedra" and j2== "tijera") :
		print num,"¡Gana el jugador 1!"
		
	if (j1 == "papel" and j2 == "piedra"):
		print num,"¡Gana el jugador 1!"
  
	if (j1 == "tijera" and j2 == "papel"):
		print num,"¡Gana el jugador 1!"

	if (j2 == "piedra" and j1 == "tijera"):
		print num,"¡Gana el jugador 2!"
  
	if (j2 == "papel" and j1 == "piedra"):
		print num,"¡Gana el jugador 2!"
  
	if (j2 == "tijera" and j1 == "papel"):
		print num,"¡Gana el jugador 2!"

	if (j1 == j2):
		print num,"¡Empate!"
  
	if (num == 57):
		salir=True
  
	num = num + 1
