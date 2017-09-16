'''
Question 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is 
the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number 
from the end". 
'''


class Node(object):
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
		print(m,'th item from the end is:', m_th_element)
	else:
		print('Error: linked list is smaller than', m)
	print()

# Test cases

# Create a linked list
llist = LinkedList()
for i in range(1, 100):
	llist.append(Node(i))

question5(llist.get_position(1), 20)


llist = LinkedList()
for i in range(-4, 5):
	llist.append(Node(i))
question5(llist.get_position(1), 3)


llist = LinkedList()
for i in [5,3,7,8,0]:
	llist.append(Node(i))
question5(llist.get_position(1), 3)

llist = LinkedList()
for i in range(-4, 5):
	llist.append(Node(i))
question5(llist.get_position(1), 20)