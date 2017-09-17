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
	## Only proceed if valid strings there
	if len(list(s)) == 0 or len(t) == 0:
		print('Error: At least one input is not a valid string')
		return False
	
	## Convert the strings to lower case
	s = s.lower()
	t = t.lower()
	
	def word_letter_count(word_):
		word_dict = {}
		for letter in word_:
			if letter in word_dict.keys():
				word_dict[letter] = word_dict[letter] + 1
			elif letter not in word_dict.keys():
				word_dict[letter] = 1
		return word_dict
		
	t_dict = word_letter_count(t)
	len_tdict = len(t_dict)

	for word in s.split():	
		s_word_dict = word_letter_count(word)
		count = 0
		for letr in t_dict.keys():
			if letr in s_word_dict.keys() and \
					t_dict[letr]  == s_word_dict[letr]:
				count += 1

		if count == len_tdict:
			print('"',t,'"', 'is a anagram of the given string')
			return True
	print('"',t,'"', 'is not a anagram of the given string')
	return False

## Question 1 test cases
print('Questinn 1 tests results')
print(question1('udasity', 'ad'))
print(question1('determine some anagram of t is a substring of', 'some'))
print(question1('determine some anagram of t is a substring of', 'like'))
print(question1('', 'like'))
print(question1('', ''))


