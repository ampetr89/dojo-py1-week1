from math import ceil

def drawStars(arr):
	for x in arr:
		if type(x) == str:
			sym = x[0].lower()
			n = len(x)
		else:
			# numeric type
			sym = '*'
			n = int(ceil(x))

		print ''.join([sym for i in range(n)])

print 'Part I - numbers only'
drawStars( [4, 6, 1, 3, 5, 7, 25])

print 'Part II - numbers and strings'
drawStars( [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])