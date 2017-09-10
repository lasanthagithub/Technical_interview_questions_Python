## Question 1
"""
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False
"""

def question1(s, t):
	'''
	s and t are two strings.
	This function determine whether t is an anagram of s or not
	'''
	
	## converting strings to lists
	s_list = list(s)
	s_list.sort()
	t_list = list(t)
	t_list.sort()
	
	print (s_list)
	
	if t_list in t_list:
		return True
	else:
		return False
	

## Questinn 1 test
print(question1('udasity', 'ad'))