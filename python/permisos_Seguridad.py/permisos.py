# !/usr/bin/python
# coding:utf-8
import os
import stat
 
path_to_explore="/home/zeus/Documentos/python"
total_size=0
   	 
# Mostramos la ruta  
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
    	name_path=os.path.join(root, name)
    	print(name_path) ,
    	print os.stat(name_path).st_size
    	total_size=total_size+os.stat(name_path).st_size
    	permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
    	print oct(permissions)
 
 
    for name in dirs:
    	name_path=os.path.join(root, name)
    	print(name_path) ,
    	print os.stat(name_path).st_size
