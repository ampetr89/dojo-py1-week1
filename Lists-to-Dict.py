def lists2dict(L1, L2):
	if len(L1) == len(L2):
		return dict(zip(L1, L2))

	# otherwise
	if len(L1) > len(L2):
		keylist = L1
		vallist = L2
	else:
		keylist = L2
		vallist = L1

	dflt = None # default when there is no value for a key
	mydict = dict.fromkeys(keylist, dflt) 
	for i in range(len(vallist)):
		mydict[keylist[i]] = vallist[i]

	return mydict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
print lists2dict(name, favorite_animal)


# extra person
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Bob"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
print lists2dict(name, favorite_animal) 

''' extra animal (therefore animal list being longer will become the dictionary keys. 
hopefully no two people have the same favorite animal!
'''
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "tiger"]
print lists2dict(name, favorite_animal) 

'''
even if horse appears twice in the animal list, this is fine...
'''
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "horse"] # <- oh no, horse is here twice
print lists2dict(name, favorite_animal) 

'''
...due to the fact that this is fine:
'''
print dict.fromkeys(['horse', 'horse', 'cat'], 'Anna')