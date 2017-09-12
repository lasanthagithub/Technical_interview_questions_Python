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
class Node(object):
	def __init__(self, value):
		self.value = value
		self.edges = []

class Edge(object):
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to

class Graph(object):
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges

	def insert_node(self, new_node_val):
		new_node = Node(new_node_val)
		self.nodes.append(new_node)
	
	def insert_edge(self, new_edge_val, node_from_val, node_to_val):
		from_found = None
		to_found = None
		for node in self.nodes:
			if node_from_val == node.value:
				from_found = node
			if node_to_val == node.value:
				to_found = node
		if from_found == None:
			from_found = Node(node_from_val)
			self.nodes.append(from_found)
		if to_found == None:
			to_found = Node(node_to_val)
			self.nodes.append(to_found)
		new_edge = Edge(new_edge_val, from_found, to_found)
		from_found.edges.append(new_edge)
		to_found.edges.append(new_edge)
		self.edges.append(new_edge)

	def get_edge_list(self):
		edge_list = []
		for edge_object in self.edges:
			edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
			edge_list.append(edge)
		return edge_list
	
	def get_adjacency_list(self):
		max_index = self.find_max_index()
		adjacency_list = [None] * (max_index + 1)
		for edge_object in self.edges:
			if adjacency_list[edge_object.node_from.value]:
				adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
			else:
				adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
		return adjacency_list
	
	def get_adjacency_matrix(self):
		max_index = self.find_max_index()
		adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
		for edge_object in self.edges:
			adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
		return adjacency_matrix
	
	def find_max_index(self):
		max_index = -1
		if len(self.nodes):
			for node in self.nodes:
				if node.value > max_index:
					max_index = node.value
		return max_index

###############################################################################

'''
This function get in and return an adjacensy list tructure like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
'''
def question3(g):
	## Asumptions: all the nodes 
	g_key_list = g.keys()
	#print(g_key_list)
	
	start_node = 'A'
	gr = Graph()

	
	paths = {} ## {path1: [[A, B, C,D..], total_edge_val]}
	
	## Inser nodes
	#for node in g:
	#	gr.insert_node(node)
	
	## Insert edges and nodes
	for node in g:
		for edge in g[node]:
			gr.insert_edge(int(edge[1]), node, edge[0])
	
	for node in gr.nodes:
		print(node.value)
	print(gr.get_edge_list())
	print(gr.get_adjacency_matrix())

def convert_to_graph():
	pass


g = {'A' : [('B', 7), ('C', 9), ('F', 14)], 
     'B' : [('A', 7), ('C', 10), ('D', 15)], 
     'C' : [('A', 9), ('B', 10), ('D', 11), ('F', 2)],
     'D' : [('B', 15), ('C', 11), ('E', 6)],
     'E' : [('D', 6), ('F', 9)],
     'F' : [('A', 14), ('C', 2), ('E', 9)]
	}

question3(g)


