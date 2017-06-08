def odd_even(N):
	msg = {
		0: 'This number is even',
		1: 'This number is odd'
	}
	start = 1
	j = start % 2
	for i in range(1, N+1):
		print i, msg[j]
		j = 1 - j

if False:
	odd_even(10)



def multiply(arr0, x):
	arr = list(arr0) # make a copy so we dont change the value of the original array
	for i in range(len(arr)):
		arr[i] *= x
	return arr

	# list comprehension equivalent
	# return [a*x for a in arr]
if False:
	a = [2,4,10,16]
	b = multiply(a, 5)
	print a  # make sure we didnt change a
	print b


def layered_multiples(arr):
	layeredList = []
	for x in arr:
		layeredList.append([1 for i in range(x)])
	return layeredList

if False:
	x = layered_multiples(multiply([2,4,5], 3))
	print x