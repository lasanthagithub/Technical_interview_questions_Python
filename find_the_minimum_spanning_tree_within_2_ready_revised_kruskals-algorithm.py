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
