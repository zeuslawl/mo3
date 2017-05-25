# !/usr/bin/python
# coding:utf-8

#este bucle te dice lo que pesa cada archivo y directorio de -->  /home/zeus/Documentos/python

#Import de os y stat
import os
import stat

#Asignar variables 
path_to_explore="/home/zeus/Documentos/python"
total_size=0
        
# Mostramos ruta de todo.  
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
        #Solo saldrán los que sean diferentes a 0 (inseguros).
        if(permissions <>0):
			print oct(permissions)
        
 
#Lo mismo que en los archivos pero para los directorios. 
    for name in dirs:
        name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
        if(permissions <>0):
			print oct(permissions)
 
print "El tamaño total en B es:" , total_size
