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
	
	## Get the character count dictionary
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
	
	## Determine whether the t is anagram of s or not
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
print()


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
		if isOdd(substring_len): ## find the length is even or odd
			first_part = substring[:center +1]
			second_part = substring[center:][::-1] ## reverse the string
		else:
			first_part = substring[:center]
			second_part = substring[center:][::-1]
		
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
print('Questinn 2 tests results##############################################')
print(question2('aghht atta ghjhfsh gittig ggg'))
print(question2('aghht atta ghjhfsh gititg ggg'))
print(question2('1988 1988891 1881 6253677 222222'))
print(question2('1988 1988891 1881 6253677 222222222'))
print(question2('1988 1988891 1881 6253677 22222 aghht atta  gittig gggg'))
print(question2('1988 198s8891 186h81 6253gg677 22ernb222 aghht at5gvta '))
print(question2(''))
print()



###########Question3###########################################################
'''
Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. 
Vertices are represented as unique strings. 
The function definition should be question3(G)

The keys of the dictionary are the nodes of our graph. 
The corresponding values are lists with the nodes, 
which are connecting by an edge.
An edge size is given as a 2-tuple with nodes , i.e. ("A","3")

'''
###########Question3###########################################################
'''
Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. 
Vertices are represented as unique strings. 
The function definition should be question3(G)

The keys of the dictionary are the nodes of our graph. 
The corresponding values are lists with the nodes, 
which are connecting by an edge.
An edge size is given as a 2-tuple with nodes , i.e. ("A","3")

'''


'''
Some of the part of the codes aquired from https://programmingpraxis.com for 
minimum-spanning-tree-kruskals-algorithm.
And modified accordingly in order to use purpose of this project
'''
class DisjointSet(dict):
    def add(self, item):
        self[item] = item
 
    def find(self, item):
        parent = self[item]
 
        while self[parent] != parent:
            parent = self[parent]
 
        self[item] = parent
        return parent
 
    def union(self, item1, item2):
        self[item2] = self[item1]

import pprint
pp = pprint.PrettyPrinter(indent=2)

from operator import itemgetter

'''
This function get in and return an adjacensy list structure like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
'''
def question3(g):
	
	## Get the nodes list
	g_key_list = list(g.keys())
	
	## convert g to list of edges
	edge_list = []
	for node in g_key_list:
		for edge in g[node]:
			edge_list.append((node, edge[0], edge[1]))
			
	## Use Kruskal algorithum to determine minimum spaning tree
	## The procedure returns edges list that contains the min spanning tree
	def kruskal_min_span_tree(nodes, edges):
		graph = DisjointSet()
		min_span_tree = []
		for node in nodes:
			graph.add(node)
	
		size = len(nodes) - 1
	
		for edge in sorted( edges, key=itemgetter(2)):
			n1, n2, _ = edge
			t1 = graph.find(n1)
			t2 = graph.find(n2)
			if t1 != t2:
				min_span_tree.append(edge)
				size -= 1
				if size == 0:
					#print(forest)
					return min_span_tree
	
				graph.union(t1, t2)
			
	min_span_path_list = kruskal_min_span_tree(g_key_list, edge_list)

	## convert to dictionary
	min_path_dict = {}
	for edge in min_span_path_list:
		if edge[0] in min_path_dict.keys():
			min_path_dict[edge[0]].append((edge[1], edge[2]))
		else:
			min_path_dict[edge[0]] = [(edge[1], edge[2])]
	return min_path_dict

	
## Test cases
g = {'A' : [('B', 7), ('C', 9), ('F', 14)], 
     'B' : [('A', 7), ('C', 10), ('D', 15)], 
     'C' : [('A', 9), ('B', 10), ('D', 11), ('F', 2)],
     'D' : [('B', 15), ('C', 11), ('E', 6)],
     'E' : [('D', 6), ('F', 9)],
     'F' : [('A', 14), ('C', 2), ('E', 9)]
	}

g1 = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
	
g2 = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 1000000)], 
 'C': [('B', 1000000)]}
	
g3 = {'A' : [('B', 7), ('C', 9), ('F', 14)], 
     'B' : [('A', 7), ('C', 10), ('D', 15)], 
     'C' : [('A', 9), ('B', 10), ('D', 11), ('F', 2), ('G', 4)],
     'D' : [('B', 15), ('C', 11), ('E', 6)],
     'E' : [('D', 6), ('F', 9), ('G', 3)],
     'F' : [('A', 14), ('C', 2), ('E', 9), ('G', 5)],
     'G' : [('F', 5), ('E', 3), ('C', 4)]
     }
					
g4 = {'A' : [('B', 10000), ('C', 9), ('F', 14)], 
     'B' : [('A', 10000), ('C', 10), ('D', 15)], 
     'C' : [('A', 9), ('B', 10), ('D', 11), ('F', 10000), ('G', 4)],
     'D' : [('B', 15), ('C', 11), ('E', 6)],
     'E' : [('D', 6), ('F', 100000), ('G', 3)],
     'F' : [('A', 14), ('C', 10000), ('E', 100000), ('G', 5)],
     'G' : [('F', 5), ('E', 3), ('C', 4)]
     }


print('Questinn 3 tests results')
pp.pprint(question3(g))
pp.pprint(question3(g1))
pp.pprint(question3(g2))
pp.pprint(question3(g3))
pp.pprint(question3(g4))
print()



###########Question4###########################################################
'''
Question 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is 
an ancestor of both nodes. For example, the root is a common ancestor of 
all nodes on the tree, but if both nodes are descendents of the root's 
left child, then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres 
to all BST properties. The function definition should look like 
question4(T, r, n1, n2), where T is the tree represented as a matrix, 
where the index of the list is equal to the integer stored in that node 
and a 1 represents a child node, r is a non-negative integer representing 
the root, and n1 and n2 are non-negative integers representing the two nodes 
in no particular order.

'''

class BNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
	def __init__(self, root):
		self.root = BNode(root)

	def insert(self, new_val):
		self.insert_helper(self.root, new_val)

	def insert_helper(self, current, new_val):
		if current.value < new_val:
			if current.right:
				self.insert_helper(current.right, new_val)
			else:
				current.right = BNode(new_val)
		else:
			if current.left:
				self.insert_helper(current.left, new_val)
			else:
				current.left = BNode(new_val)

	## Search path to given node
	def find_path_to(self, find_val):
		return self.find_path_to_helper(self.root, find_val, \
			path = [self.root.value])

	def find_path_to_helper(self, current, find_val, path):
		found = False
		if current:			
			if current.value == find_val:
				found = True
				
			elif current.value < find_val:
				path.append(current.right.value)	
				self.find_path_to_helper(current.right, find_val, path)
				
			else:
				path.append(current.left.value)
				self.find_path_to_helper(current.left, find_val, path)
			#print (found)	
		return path


def question4(T, r, n1, n2):
	
	least_common_ancestor = None	
	if (n1 < r and n2 > r) or (n2 < r and n1 > r):
		print('least_common_ancestor for',n1, 'and', n2, 'is the root' , r)
		print()
		return r
		
	elif n1 == r or n2 == r:
		print(n1, 'or', n2, 'equel to root', r)
		print('No common ancestor')
		print()
		return least_common_ancestor
	else:	
		## Initialize and enter root into tree
		tree = BST(r)	
		
		## Get the list of child nodes from matrix
		def get_children(T, node, temp_lst = []):
			for nod, child in enumerate(T[node]):
				if child == 1:
					temp_lst.append(nod)
			return temp_lst
		
		children = get_children(T, r)	
		## Inser data in to BST
		while children:
			temp_child = []
			for sub_nod in children:
				tree.insert(sub_nod)
				temp_child = get_children(T, sub_nod, temp_child)
			children = temp_child
		
		## Get the path fom root to specific nodes
		path_to_n1 = tree.find_path_to(n1)
		path_to_n2 = tree.find_path_to(n2)
		print(tree.find_path_to(n1))
		print(tree.find_path_to(n2))
		
		## Get the least common ancestor
		for nod_n1 in path_to_n1:
			for idx, nod_n2 in enumerate(path_to_n2):
				if nod_n1 == nod_n2:
					least_common_ancestor = nod_n1
					if least_common_ancestor == n1 or \
									least_common_ancestor == n2:
						least_common_ancestor = path_to_n2[idx -1]
					continue	
		print('least_common_ancestor for',n1, 'and', n2, 'is' , \
									least_common_ancestor)
		print()
		return least_common_ancestor

## Test cases
print('Questinn 4 tests results##############################################')
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]], 3, 1, 4)


question4([[0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [0, 0, 0, 0, 0]],3, 1, 2)


question4([[0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0],
           [0, 1, 0, 1, 0],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],2, 1, 2)

question4([[0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0]],3, 1, 2)

question4([[0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0]],4, 1, 2)

question4([[0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0]],4, 1, 6)
print()

###########Question5###########################################################

'''
Question 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is 
the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number 
from the end". 
'''

class LLNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def get_position(self, position):
		"""Get an element from a particular position.
		Assume the first position is "1".
		Return "None" if position is not in the list."""
		counter = 1
		current = self.head
		if position < 1:
			return None
		while current and counter <= position:
			if counter == position:
				return current
			current = current.next
			counter += 1
		return None
		

def question5(ll, m):
	
	## Get the length of linked list
	def get_length(node):
		"""Get the total length of the linked list."""
		counter = 1
		current = node
		if current:
			while current:
				current = current.next
				counter += 1
			return counter
		else:
			return None
			
	def get_element(l_list, position):
		"""Get an element from a particular position.
		Assume the first position is "1".
		"""
		counter = 1
		current = l_list
		if position < 1:
			return None
		while current and counter <= position:
			if counter == position:
				return current.data
			current = current.next
			counter += 1
		return None
	
	ll_length = get_length(ll)
	
	if m < ll_length:
		m_th_from_end = ll_length - m
		m_th_element = get_element(ll, m_th_from_end)
		print(m,'th/rd/st item from the end is:', m_th_element)
	else:
		print('Error: linked list is smaller than', m)
	print()
	
print('Questinn 5 tests results##############################################')
# Test cases

# Create a linked list
llist = LinkedList()
for i in range(1, 100):
	llist.append(LLNode(i))

question5(llist.get_position(1), 20)


llist = LinkedList()
for i in range(-4, 5):
	llist.append(LLNode(i))
question5(llist.get_position(1), 3)


llist = LinkedList()
for i in [5,3,7,8,0]:
	llist.append(LLNode(i))
question5(llist.get_position(1), 3)

llist = LinkedList()
for i in range(-4, 5):
	llist.append(LLNode(i))
question5(llist.get_position(1), 20)


