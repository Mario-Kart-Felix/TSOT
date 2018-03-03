import random

class Lsys:
	def widenNetworks(lhch):   # Rule 1
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == 'N':
			if rnum < 10:
				rhstr = '[N][N]'
			elif rnum < 70:
				rhstr = '[N][N][N]'
			else:
				rhstr = '[N][N][N][N]'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr    
			
	def populateBaseNetwork(lhch):   # Rule 2
		rnum = random.randint(0, 100)
		rhstr = ""        
		if lhch == 'N':
			if rnum < 30:
				rhstr = '###'
			elif rnum < 80:
				rhstr = '####'
			else:
				rhstr = '#####'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr
		
	def deepenNetworks(lhch):   # Rule 3
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == '#':
			if rnum < 60:
				rhstr = '#'
			elif rnum < 65:
				rhstr = '#<#>'
			elif rnum < 70:
				rhstr = '#<##>'
			elif rnum < 85:
				rhstr = '#<###>'
			else:
				rhstr = '#<#####>'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr
	  
	def stringifyNetworks(lhch):   # Rule 4
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == '#':
			if rnum < 80:
				rhstr = '#'
			elif rnum < 90:
				rhstr = '#<#>'
			else:
				rhstr = '#<#<#>>'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr
	  
	def createEndpoints(lhch):   # Rule 5
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == '#':
			if rnum < 30:
				rhstr = 'E'
			else:
				rhstr = '#'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr
	  
	def capEndpoints(lhch):   # Rule 6
		rhstr = ""
		if lhch == '#':
			rhstr = 'E'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr
	  
	def vulnerablizeEndpoints(lhch):   # Rule 7
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == 'E':
			if rnum < 60:
				rhstr = 'E'
			elif rnum < 70:
				rhstr = 'E{V}'
			elif rnum < 80:
				rhstr = 'E{VV}'
			elif rnum < 90:
				rhstr = 'E{VVV}'
			else:
				rhstr = 'E{VVVVV}'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr
	  
	def finalizeVulnerabilities(lhch):   # Rule 8
		rnum = str(random.randint(0, 100))
		# add in stuff to make sure you don't get the same vulnerability twice.
		rhstr = ""
		if lhch == 'V':
			rhstr = rnum + ","
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def processString1(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + widenNetworks(ch)
		#print newstr
		return newstr

	def processString2(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + populateBaseNetwork(ch)
		#print newstr
		return newstr

	def processString3(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + deepenNetworks(ch)
		#print newstr
		return newstr
	  
	def processString4(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + stringifyNetworks(ch)
		#print newstr
		return newstr
	  
	def processString5(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + createEndpoints(ch)
		#print newstr
		return newstr
	  
	def processString6(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + capEndpoints(ch)
		#print newstr
		return newstr
	  
	def processString7(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + vulnerablizeEndpoints(ch)
		#print newstr
		return newstr
	  
	def processString8(oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + finalizeVulnerabilities(ch)
		#print newstr
		return newstr

	def __init__(self,numIters,axiom):
		startString = axiom
		endString = ""

		endString = endString + __processString1(startString)
		startString = endString
		endString = ""

		endString = endString + __processString2(startString)
		startString = endString
		endString = ""

		for i in range(numIters):
			endString = endString + __processString3(startString)
			startString = endString
			endString = ""

			endString = endString + __processString4(startString)
			startString = endString
			endString = ""

			endString = endString + __processString5(startString)
			startString = endString
			endString = ""
		
		endString = endString + __processString6(startString)
		startString = endString
		endString = ""

		endString = endString + __processString7(startString)
		startString = endString
		endString = ""

		endString = endString + __processString8(startString)
		startString = endString
		endString = ""
	  
		return startString
		print "done now"
