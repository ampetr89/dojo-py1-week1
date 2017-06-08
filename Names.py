""" define two formatting functions for names.
The first one, formatName1, just prints the first and last name in camel case
The second one, formatName2, prints the id number, the full name in upper case, and the number of charachters in the name
"""
def formatName1(name, num=None):
	return '{} {}'.format(name['first_name'], name['last_name'])

def formatName2(name, num):
	first_name = name['first_name'].upper()
	last_name = name['last_name'].upper()
	nchar = len(first_name) + len(last_name) 
	return '{} - {} {} - {}'.format(num+1, first_name, last_name, nchar)

"""
given a list of first and last names, print them out and
use a particular formatting function
"""
def writeNames(nameList, fmtFunc):
	for i in range(len(nameList)):
		name = nameList[i]
		print fmtFunc(name, i)

"""
in the user ground, there are name lists nested inside a
dictionary. reuse the writeNames function, but use a 
different formatting function (as required by the assignment instructions)
"""
def writeUserGroups(userList, formatName1):
	for utype, nameList in userList.items():
		print utype
		writeNames(nameList, formatName2)




print(' ---Part I ---')
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

writeNames(students)

print('\n ---Part II ---')
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

writeUserGroups(users)