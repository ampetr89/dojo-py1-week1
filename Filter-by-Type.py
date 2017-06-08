def whatsYourType(x):
	xtype = type(x)
	if xtype == int:
		if x < 100:
			"""If the integer is greater than or equal to 100,
			 print "That's a big number!" If the integer is 
			 less than 100, print "That's a small number"
			"""
			print "That's a small number"
		else:
			print "That's a big number!"

	elif xtype == str:
		"""
		f the string is greater than or equal to 50 characters 
		print "Long sentence." If the string is shorter than
		 50 characters print "Short sentence.
		"""
		if len(x) < 50:
			print "Short sentence"
		else:
			print "Long sentence"

	elif xtype == list:
		"""
		If the length of the list is greater than or equal to 10 
		print "Big list!" If the list has fewer than 10 values
		print "Short list."
		"""
		if len(x) < 10:
			print "Short list"
		else:
			print "Big list!"
	else:
		print "don't care about this type:", xtype.__name__

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23

sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""

aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

tu = (1,2,3)

print '-- Ints --'
whatsYourType(sI)
whatsYourType(mI)
whatsYourType(bI)
whatsYourType(eI)
whatsYourType(spI)

print '-- Strings --'
whatsYourType(sS)
whatsYourType(mS)
whatsYourType(bS)
whatsYourType(eS)

print '-- Lists --'
whatsYourType(aL)
whatsYourType(mL)
whatsYourType(lL)
whatsYourType(eL)
whatsYourType(spL)

print '-- Tuple --'
whatsYourType(tu)