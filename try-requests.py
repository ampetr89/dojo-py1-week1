import requests
# print requests.__file__

"""
requuests library documentation:
http://docs.python-requests.org/en/master/
"""

"""
An API of Ice and Fire (Game of Thrones fan API)
https://anapioficeandfire.com/Documentation
"""

base_url = 'http://www.anapioficeandfire.com/api/'

# get some characters
char_params = {
	'page': 1,
	'pageSize': 100
}
# https://anapioficeandfire.com/Documentation#characters

r = requests.get(base_url+'characters', params = char_params)
print 'request status', r.status_code
characters = r.json()
# print len(characters)
for character in characters:
	if character['name']:
		for key, val in character.items():
			if type(val) == list and len(val) == 0:
				del character[key]
			elif type(val) in [str, unicode] and len(val.strip())==0:
				del character[key]
			elif val is None:
				del character[key]

		character.setdefault('born', 'Unknown')
		character.setdefault('died', 'Unknown')
		character.setdefault('titles', '')
		character.setdefault('culture', 'Unknown')

		character.update({
			'titles': ', '.join(character['titles'])
			})
		print '{name}, {gender} (Born: {born}, Died: {died}), {titles} from {culture} culture.'.format(**character)
