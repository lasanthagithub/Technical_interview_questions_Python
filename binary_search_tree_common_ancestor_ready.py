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
	least_common_ancestor = None
	if n1 == r or n2 == r:
		print(n1, 'or', n2, 'equel to root', r)
		print('No common ancestor')
		print()
		return least_common_ancestor
	
	for nod_n1 in path_to_n1:
		for idx, nod_n2 in enumerate(path_to_n2):
			if nod_n1 == nod_n2:
				least_common_ancestor = nod_n1
				if least_common_ancestor == n1 or \
								least_common_ancestor == n2:
					least_common_ancestor = path_to_n2[idx -1]
				continue	
	#common_path = list(set(path_to_n1) & set(path_to_n2))
	#common_path = list(set(path_to_n1) - set(path_to_n2))
	print('least_common_ancestor for',n1, 'and', n2, 'is' , \
								least_common_ancestor)
	print()
	return least_common_ancestor

## Test cases
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
