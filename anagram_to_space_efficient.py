###########Question1###########################################################

"""
Given two strings s and t, determine whether some anagram of t is a substring 
of s. For example: if s = "udacity" and t = "ad", then the function returns 
True. Your function definition should look like: 
question1(s, t) and return a boolean True or False
"""

def question1(s, t):
	'''
	s and t are two strings.
	s is the main string and t is the string to create anagrms
	This function determine whether t is an anagram of s or not
	'''
	import itertools
	
	## Convert the strings to lower case
	s = s.lower()
	t = t.lower()

	## converting strings to lists
	t_list = list(t)

	## finding posible anagrams
	word_combination_list = list(itertools.permutations(t_list, len(t_list)))
	
	## create word combinations
	is_anagram = False
	word_combination = []
	for combination in word_combination_list:
		word = ''
		for letter in combination:
			## combine letters to a word
			word = word + letter
		## Chech wheather the word is in given main string
		if word in s and s != '':
			is_anagram =True
			word_combination.append(word) ## to save space this line can
								 ## be omited
	
	if is_anagram:
		print('The anagrams in the main string string given: ', \
										word_combination)
		return True		
	else:
		print('No anagrams found in the main string string given:')
		return False
	
## Question 1 test cases
print('Questinn 1 tests results')
print(question1('udasity', 'ad'))
print(question1('determine some anagram of t is a substring of', 'some'))
print(question1('determine some anagram of t is a substring of', 'like'))
print(question1('', 'like'))
print(question1('', ''))


