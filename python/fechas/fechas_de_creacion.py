# !/usr/bin/python
# coding:utf-8
import os, time
 
ruta_a_explorar="/home/zeus/Documentos/python"
 
 
for ruta, directorios, archivos in os.walk(ruta_a_explorar):
	for nombre in archivos:
		ruta_completa=os.path.join(ruta, nombre)
		print(ruta_completa)
 
    	#Fecha ultimo acceso
    	print time.ctime(os.path.getatime(ruta_completa))
 
    	#Fecha ultima modificación
    	print time.ctime(os.path.getmtime(ruta_completa))
 
 
 
	for nombre in directorios:   		 
		ruta_completa=os.path.join(ruta, nombre)
		print(ruta_completa)
