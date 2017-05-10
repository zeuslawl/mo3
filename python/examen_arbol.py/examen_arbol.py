# !/usr/bin/python
# -*-coding: utf-8-*-

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

for fil in my_range(1,6,1):
	for col in my_range(1,5,1):
		if(fil==4):
			print "A",
		elif (fil==3 and col==2) or (fil==3 and col==3) or (fil==3 and col==4):
			print "A",
		elif (fil==1 and col==3):
			print "*",
		elif (fil==2 and col==3):
			print "A",
		elif (fil==5 and col==3) or (fil==6 and col==3):
			print "N",
		else:
			print " ",
	print ""
