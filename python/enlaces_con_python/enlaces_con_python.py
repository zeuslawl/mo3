# !/usr/bin/python

#Te dice los directorios que hay en la carpeta donde esta el .py

import os
print "Primer Ejemplo"
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

print "######################"
print "######################"

#Lo que consume cada archivo.
print "Segundo Ejemplo"
print "Lo que consume cada archivo"
print "---------------"
from os.path import join, getsize 
for root, dirs, files in os.walk('/tmp'):
    print root, "consumes",
    print sum([getsize(join(root, name)) for name in files]),
    print "bytes in", len(files), "non-directory files"


print "######################"
print "######################"


#Imprime todos los directorios, subdirectorios y archivos de la ruta de acceso.
print "Tercer Ejemplo"
import os
print "*" * 20
for root, dirs, files in os.walk("/var/log"):
    print root
    print dirs
    print files
