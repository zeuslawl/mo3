# !/usr/bin/python
# coding:utf-8
import os
import time
import stat
 
ruta_a_explorar="/home/zeus/Documentos/python"

#Tamaño 1gb en bytes
tamanyo_minimo=1073741824


hoy=int(time.strftime("%y"))
 
for ruta, directorios, archivos in os.walk(ruta_a_explorar):
    for nombre in archivos:
		
		#La ruta del archivo		
        ruta_entera=os.path.join(ruta, nombre)
        
		#Peso de los archivos
        total_size=os.stat(ruta).st_size
					
        #el ultimo dia de acceso al archivo
        tiempo=time.ctime(os.path.getatime(ruta))
        
        tiempo_anyo = tiempo[23:25]
        
        ultimo_tiempo= int(hoy) - int(tiempo_anyo)
        
        
        if(total_size>=tamanyo_minimo) and(ultimo_tiempo >=1 or ultimo_tiempo < 0):
			print ruta,
			print total_size
			
			print "El ultimo acceso al archivo: "
			print tiempo	
			



 
