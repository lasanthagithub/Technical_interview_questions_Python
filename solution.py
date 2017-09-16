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
			word_combination.append(word) ## to save the space this line 
								 ## canbe omited
	
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


###########Question2###########################################################
'''
Given a string a, find the longest palindromic substring contained in a. Your 
function definition should look like question2(a), and return a string
'''

def question2(a):
	
	## convert to lowercase if the string contain letters
	a = str(a)
	a = a.lower()

	longest_length = 0
	longest_substr = None
	
	a = a.rstrip() ## remove spaces at the end
	a_list = a.split() ## split the string by spaces
	
	for substring in a_list:
		substring_len = len(substring)
		center = int(substring_len / 2) ## get the centre
		
		## Seperate the substring into two parst by centre
		## Sort the two parts
		if isOdd(substring_len): ## find the length is even or odd
			first_part = ''.join(sorted(substring[:center +1]))
			second_part = ''.join(sorted(substring[center:]))
		else:
			first_part = ''.join(sorted(substring[:center]))
			second_part = ''.join(sorted(substring[center:]))
		
		## Check the substring is palindromic or not
		## return the longest palindromic substring
		if first_part == second_part:
			if substring_len > longest_length:
				longest_length = substring_len
				longest_substr = substring
				
	return longest_substr
			
## Check wether a number is even or odd
def isOdd(numb):
	remainder = numb % 2
	if  remainder != 0:
		return True
	else:
		return False

print(question2('aghht atta ghjhfsh gittig gggg'))
print(question2('1988 1988891 1881 6253677 222222'))
print(question2('1988 1988891 1881 6253677 222222222'))
print(question2('1988 1988891 1881 6253677 22222 aghht atta  gittig gggg'))
print(question2('1988 198s8891 186h81 6253gg677 22ernb222 aghht at5gvta '))
print(question2(''))