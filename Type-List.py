def listTypes(x):
	# check the list has elements
	if len(x)==0:
		print "x is empty"
		return

	# initiate a blank string and 0 zum
	xstr = ''
	xsum = 0

	# these switches will turn on as soon as one value 
	# is found with either num or str type, respectively
	hasNum = False
	hasStr = False

	# initiate the types list with the type of the 
	# first value
	first = type(x[0])
	types = [first]

	# check the type of each value. if new values are
	# found, add them to the types list. as soon as
	# number or string found, keep track with hasNum / hasStr
	for val in x:
		valtype = type(val)
		if valtype not in types:
			types.append(valtype)

		if valtype == str:
			xstr += ' '+val
			hasStr = True
		elif valtype in [int, float, long]:
			# note there are multiple numeric types
			xsum += val
			hasNum = True

	# show the user the input array (optional but helpful)
	print "input array", x

	# look at the types list. if theres more than one then
	# print that the list has mixed types 
	if len(types) > 1:
		print "The list contains mixed types"

	# only print sum / string if it was used.
	# note, sum could be 0 if we had x=[-1, 1]
	if hasNum:
		print "Sum:", xsum
	if hasStr:
		print "String:", xstr

listTypes(['magical unicorns',19,'hello',98.98,'world'])

listTypes([2,3,1,7,4,12])
listTypes([2,3,1,7,4,12.0])

listTypes(['magical','unicorns'])
