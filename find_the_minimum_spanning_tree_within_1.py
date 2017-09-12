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
	
	paths = {} ## {path1: [[A, B, C,D..], total_edge_val]}
	
	for node in g_key_list:
		
		for edge in g[node]:
			to_node = edge[0]
			print(to_node)
		

def convert_to_graph():
	


g = {'A' : [('B', 7), ('C', 9), ('F', 14)], 
     'B' : [('A', 7), ('C', 10), ('D', 15)], 
     'C' : [('A', 9), ('B', 10), ('D', 11), ('F', 2)],
     'D' : [('B', 15), ('C', 11), ('E', 6)],
     'E' : [('D', 6), ('F', 9)],
     'F' : [('A', 14), ('C', 2), ('E', 9)]
	}

question3(g)

