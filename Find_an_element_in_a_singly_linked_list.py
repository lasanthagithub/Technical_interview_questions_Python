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



	def insert(self, new_element, position):
		"""Insert a new node at the given position.
		Assume the first position is "1".
		Inserting at position 3 means between
		the 2nd and 3rd elements."""
		counter = 1
		current = self.head
		if position > 1:
			while current and counter < position:
				if counter == position - 1:
					new_element.next = current.next
					current.next = new_element
				current = current.next
				counter += 1
		elif position == 1:
			new_element.next = self.head
			self.head = new_element


	def delete(self, data):
		"""Delete the first node with a given data."""
		current = self.head
		previous = None
		while current.data != data and current.next:
			previous = current
			current = current.next
		if current.data == data:
			if previous:
				previous.next = current.next
			else:
				self.head = current.next




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
		Return "None" if position is not in the list."""
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
		print(m_th_element)
	else:
		print('Error: linked list is smaaler than', m)

	

# Test cases
# Create a linked list
llist = LinkedList()
for i in range(1, 100):
	llist.append(Node(i))
'''
print (llist.get_position(1).data)
# Should print 4 now
print (llist.get_position(2).data)
# Should print 3 now
print (llist.get_position(3).data)
'''
question5(llist.get_position(1), 20)





