# !/usr/bin/python
# -*- coding: utf-8 -*-

import os

os.system('clear')

#Bucle en el que utilizamos la variable extra para poder hacer el intercambio de manos.

mano_der = "movil"
mano_izq = "bocadillo\n"

print mano_der
print mano_izq

mano_extra = mano_der
mano_der = mano_izq
mano_izq = mano_extra

print "Hacemos el intercambio\n"
print mano_der
print mano_izq
