"""
Multiples
"""

"""
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
"""
print('--- part 1 ---')
def part1():
	for i in range(0, 500): 
		print i*2 + 1

part1()


"""
Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
"""
print('--- part 2 ---')
def part2():
	for i in range(1,100/5 + 1):  # replace 100 with 1000000
		print i*5

part2()


"""
Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""
print('--- sum ---')
def isNumber(x):
	return type(x) in [int, float, long, complex]

def mySum(a):
	# return sum(a)
	s = 0.0
	for val in a:
		assert isNumber(val), "all values must be numeric"
		s += val
	return s
a = [1, 2, 5, 10, 255, 3]
print mySum(a)

"""
Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""
print('--- average ---')
def myAvg(a):
	s = sum(a) # returns a float so we are good
	n = len(a)
	return s/n

a= [1, 2, 5, 10, 255, 3]
print myAvg(a)