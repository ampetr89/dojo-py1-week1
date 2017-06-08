
def fmtRow(row, digits):
	return ' '.join([str(val).rjust(digits, ' ') for val in row])

def fmtLabel(i, digits):
	return str(i).ljust(digits, ' ')

def makeTable(nmax):
	nums = range(1, nmax+1)
	largest = nmax**2
	tabdigits = len(str(largest))
	numdigits = len(str(nmax))

	frontSpace = ''.join([' ' for i in range(numdigits +1)])
	toplabel =  frontSpace + fmtRow(nums, tabdigits)
	topbar =  frontSpace + ''.join('-' for i in range(len(toplabel) - len(frontSpace)))

	# output the table
	print toplabel
	print topbar
	for i in nums:
		row = [ j*i for j in nums]
		print fmtLabel(i, numdigits) + '|' + fmtRow(row, tabdigits)


nmax = 12 # largest factor in the table
makeTable(nmax)

makeTable(9)