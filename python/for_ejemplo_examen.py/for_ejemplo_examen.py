# !/usr/bin/python
# -*-coding: utf-8-*-

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

for fil in my_range(1,5,1):
	for col in my_range(1,4,1):
		if (fil ==1):
			if (col ==2):
				print "A",
			elif col ==3:
				print "B",
			elif col==4:
				print "C",
			else:
				print "-",
		else:
			if(col==1):
				print fil-1,
			else:
				if(fil==3 and col ==3) or (fil==4 and col==2):
					print "*",
				else:
					print "-",
	print ""

		
	
