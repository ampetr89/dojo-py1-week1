import numpy as np 

"""ndarray
https://docs.scipy.org/doc/numpy-1.12.0/reference/arrays.ndarray.html
"""
arr = np.ndarray(shape=(2,2), dtype=np.int32)
print arr # wat!

arr = np.array([[1, 2, 3], [4, 5, 6]])
print 'arr', arr
print 'shape', arr.shape

print 'second column', arr[:,1] # 2nd column of the array
print 'cumul sum of 2nd axis', arr.cumsum(1)

# math functions that map to every element in the array
print arr.__pow__(2)
arr.__iadd__(1) # add 1 in place (updates arr)
print arr


# linear algebra
a = [1,1,1]
b = [2,2,2]
print np.dot(a,b) # = 2*1 + 2*1 + 2*1 = 6

# stats
vals = [1,3,2,5,6,3,2,5,4,3,9,6,3,5]
h = np.histogram(vals)
# print h
bins = h[1]
count = h[0]
for i in range(len(count)):
	print '[{} - {}): {}'.format(bins[i], bins[i+1], count[i])
