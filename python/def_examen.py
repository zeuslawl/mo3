# !/usr/bin/python
# -*-coding: utf-8-*-

import os

def obtener_tamanyo(ruta):

	peso=0
	peso = os.stat(ruta).st_size
	return peso
	
	
def imprimir_total(total):
	
	print "Se han borrado" ,total, "archivos"


ruta_origen = raw_input("Pon la ruta que quieres: ")
tamanyo = input("Pon el tamaño máximo: ")

total=0

for root,dirs,files in os.walk(ruta_origen):

	for name in files:
		
		ruta=os.path.join(root,name)
		comando= 'rm -rf ' + ruta
		
		if tamanyo >= obtener_tamanyo(ruta):
			
			os.system(comando)
			total=total+1
			
imprimir_total(total)
