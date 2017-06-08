def filterByLetter(word_list, letter):
	assert type(letter) == str, "second argument should be a single character"
	assert len(letter) == 1, "second argument should be a single character"

	matches = []
	for word in word_list:
		assert type(word) == str, "all list elements should be strings"
		if word.find(letter) != -1:
			matches.append(word)
	return matches

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
print filterByLetter(word_list, char)


# same using list comprehension
def filterByLetter(word_list, letter):
	assert type(letter) == str, "second argument should be a single character"
	assert len(letter) == 1, "second argument should be a single character"
	assert all([type(word)==str for word in word_list]), "all list elements should be strings"

	matches = [word for word in word_list if word.find(letter) != -1]
	return matches


word_list = ['hello','world','my','name','is','Anna']
char = 'o'
print filterByLetter(word_list, char)
