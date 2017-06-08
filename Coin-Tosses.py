import random

"""
we'll represent heads by 0 and tails by 1
"""
side = {
	0: 'head',
	1: 'tail'
}
count = dict.fromkeys(side.keys(), 0)


def flip():
	return int(round(random.random()))

N = 5000
for i in range(N):
	result = flip() # if result = 0 means heads, result = 1 means tails
	count[result] += 1
	
	ratio = int(count[0]/float(i+1)*100), int(count[1]/float(i+1)*100)
	print "Attempt #{0}: Throwing a coin... It's a {1}! ... Got {2} {1}(s) so far. Ratio is {3},".format(
		i+1, side[result], count[result], str(ratio[0])+':'+str(ratio[1]))
	

