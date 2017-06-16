# !/usr/bin/python
# coding:utf-8
import os
import time
import stat


path_to_explore=('/home/zeus/Documentos/abc')

peso=0

for root,dirs,files in os.walk(path_to_explore):

	for name in files:
		#Ruta
		ruta=os.path.join(root,name)
		
		#Peso
		peso=os.stat(ruta).st_size
		print name
		print peso
		
		#Ver permisos
		permissions = stat.S_IMODE ( os.stat (path_to_explore).st_mode )
		print oct(permissions)
		
		#Cambiar permisos
		os.chmod(path_to_explore,0770)
		
		#Fecha ultimo acceso
		print time.ctime(os.path.getatime(path_to_explore))
		
		#Fecha ultima modificación
		print time.ctime(os.path.getmtime(path_to_explore))
