# !/usr/bin/python
# -*-coding: utf-8-*-

#Examen de recuperación M03 Python avanzado.

#Los import de las librerias os, stat y time.
import os
import stat 
import time


#La ruta a explorar
path_to_explore=('/home/users/inf/hism1/ism43567395/Documentos/Carpeta_Para_Examen')

# Contadores de los directorios y archivos.
total_dirs=0

total_files=0

for root,dirs,files in os.walk(path_to_explore):
	
	for name in files:
		
		ruta= os.path.join(root,name)
		peso= os.stat(ruta).st_size
		
		print "La ruta es: ", ruta
		
		print " "
		
		print "El tamaño del archivo es: ", peso, "Bytes"
		
		print " " 
		
		print "La fecha de ultima modificación es: ", time.ctime(os.path.getmtime(path_to_explore))
		
		print " "
		
		total_files=total_files+1
		
	for name in dirs:
		
		ruta=os.path.join(root,name)
		
		print "La ruta es: ", ruta
		
		total_dirs=total_dirs+1
	
	
print "Número total de archivos:", total_files

print "Número total de directorios:",total_dirs
