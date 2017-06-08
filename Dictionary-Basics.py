me = {
	'name': 'Anna', 
	'age': 27, 
	'country': 'US',
	'lang': 'SQL'
}

phrases = {
	'name': 'My name is {}.', 
	'age': 'I am {} years old.', 
	'country': 'I was born in the {}.',
	'lang': 'My favorite programming language is {}.'
}

""" if we want the statements to appear in a specific
order we must specify. Otherwise dictionary key-value pairs
are returned in no particular order
"""
statement_order = [
'name',
'age',
'country',
'lang'
]

for key in statement_order:
	print phrases[key].format(me[key])
