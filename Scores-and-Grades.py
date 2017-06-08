import random

def createScore(min, max):
	return random.randint(min, max)

def scoresAndGrades(N, min, max):
	for student in range(N):
		score = createScore(min, max)
		if score < 60:
			grade = 'F' # put just in case
		elif score < 70:
			grade = 'D'
		elif score < 80:
			grade = 'C'
		elif score < 90:
			grade = 'B'
		else:
			grade = 'A'
		print 'Score {}; Your grade is {}'.format(score, grade)

scoresAndGrades(10, 60, 100)