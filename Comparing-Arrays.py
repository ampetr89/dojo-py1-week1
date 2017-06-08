def listEq(list1, list2):
	if len(list1) != len(list2):
		return False
	i=0
	while i < len(list1):
		if list1[i] != list2[i]:
			return False
		i += 1
	return True

Lists= [
	[[1,2,5,6,2], [1,2,5,6,2]],
	[[1,2,5,6,5], [1,2,5,6,5,3]],
	[[1,2,5,6,5,16], [1,2,5,6,5]],
	[['celery','carrots','bread','milk'],['celery','carrots','bread','cream']]
]
for lists in Lists:
	list_one = lists[0]
	list_two = lists[1]
	if listEq(list_one, list_two):
		print "The lists are the same"
	else:
		print "The lists are different"
