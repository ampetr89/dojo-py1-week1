"""
Assignment: String and List Practice
Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:

- .find()
- .replace()
- min()
- max()
- .sort()
- len()
"""

"""
1. Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
"""
print "--- 1. Find and Replace ---"
words = "It's thanksgiving day. It's my birthday,too!"
i = words.find('day')
print 'First occurance of "day" found at position', i
# print words[i:(i+3)] # gives you back 'day'

"""
Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
"""

print "--- 2. Min and Max ---"
"""
#oops we can use built in min(), max()

def isNumber(x):
	return type(x) in [int, float, long, complex]

def min(x):
	assert len(x) > 0, "Please provide a non-empty list"
	m = x[0]
	for i in range (1, len(x)):
		if x[i] < m:
			assert isNumber(x[i]), "List must contain only numeric types"
			m = x[i]
	return m

def max(x):
	assert len(x) > 0, "Please provide a non-empty list"
	for i in range(len(x)):
		x[i] *= -1
	return -1*min(x)
"""

def minMax(x):
	print "min", min(x)
	print "max", max(x)
x = [2,54,-2,7,12,98]
minMax(x)



"""
3. First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
"""
print "--- 3. First and Last ---"
def first_and_last(x):
	assert len(x) > 0, "Please provide a non-empty list"
	first = x[0]
	last = x[len(x)-1]
	print 'first', first
	print 'last', last
	y = [first, last]
	return y

x = ["hello",2,54,-2,7,12,98,"world"]
print first_and_last(x)

"""
4. New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
"""
print "--- 4. New List ---"
def newList(x):
	x.sort()
	N = len(x)
	# assert N % 2== 0, "even number of elements required"
	front = []
	for i in range(0, N/2):
		front.append(x.pop(0))
	# print front
	# print x

	x.insert(0, front)
	return x

y = [19,2,54,-2,7,12,98,32,10,-3,6]
print(newList(y))
print(y)