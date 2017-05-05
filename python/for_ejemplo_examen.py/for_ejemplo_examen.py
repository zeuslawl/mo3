#!/usr/bin/env python
# -*- coding: utf-8 -*-


for fil in xrange(1,5,1):
	print " "
	for col in xrange(1,4,1):
		if (fil == 1):
			if (col ==2):
				print "A",
			elif col == 3 :
				print "B",
			elif col == 4 : 
				print "C",
		else: 
			print "-",
		if (col==1):
			print fil-1
		else:
			print "-",
		
	
