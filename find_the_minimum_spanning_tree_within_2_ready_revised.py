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
###############################################################################
'''Some of the parts of the classes in this block is aquired form Udacity 
class notes '''
class GNode(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = GNode(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]

    def get_edge_dict(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        e_dict = {}
        for e in self.edges:
            e_dict[self.node_names[e.node_from.value]+'_'+ \
                   self.node_names[e.node_to.value]] = e.value
        return e_dict

    def get_edge_list_names(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node Name, To Node Name)"""
        return [(edge.value,
                 self.node_names[edge.node_from.value],
                 self.node_names[edge.node_to.value])
                for edge in self.edges]

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)
    
    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def dfs_helper(self, start_node):
        """The helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        REQUIRES: self._clear_visited() to be called before
        MODIFIES: the value of the visited property of nodes in self.nodes 
        RETURN: a list of the traversed node values (integers).
        """
        ret_list = [start_node.value]
        start_node.visited = True
        edges_out = [e for e in start_node.edges
                     if e.node_to.value != start_node.value]
        for edge in edges_out:
            if not edge.node_to.visited:
                ret_list.extend(self.dfs_helper(edge.node_to))
        return ret_list        
        

    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

###############################################################################

'''
This part og the codes auired from https://programmingpraxis.com for 
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
## Use Kruskal algorithum to determine minimum spaning tree path
## The procedure returns edge lists that contains the minimum spaniing tree
def kruskal(nodes, edges):
	forest = DisjointSet()
	mst = []
	for n in nodes:
		forest.add( n )
	#print(forest)
	sz = len(nodes) - 1

	for e in sorted( edges, key=itemgetter(2)):
		n1, n2, _ = e
		t1 = forest.find(n1)
		t2 = forest.find(n2)
		if t1 != t2:
			mst.append(e)
			sz -= 1
			if sz == 0:
				#print(forest)
				return mst

			forest.union(t1, t2)


'''
This function get in and return an adjacensy list structure like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
'''
def question3(g):
	
	
	
	
	
	'''
	## Asumptions: all the nodes 
	g_key_list = list(g.keys())
	graph = Graph()
	
	## set and convert node names to numerical values
	graph.set_node_names(g_key_list)

	## convert g to Graph. Insert edges and nodes
	for node in g_key_list:
		for edge in g[node]:
			graph.insert_edge(int(edge[1]), g_key_list.index(node),\
			g_key_list.index(edge[0]))
			
			
	## Get potential paths			
	def get_paths(paths_, nod_names, key_list):
		for i in range(len(key_list)):
			path = nod_names(i)
			if path in paths or path[::-1] in paths: continue
			paths_.append(path)
		return paths_
	
	paths = []
	#paths = get_paths(paths, graph.bfs_names, g_key_list)
	paths + get_paths(paths, graph.dfs_names, g_key_list)
	
	## Ge the total score for the path
	def get_edges_score(path_):
		path_len = len(path_)
		edge_dist = graph.get_edge_dict()
		path_dict = {}
		end = 2
		start = 0
		total_length = 0
		while end -1  < path_len:			
			#edge = path_[start: end]
			edge1 = path_[start] +'_'+path_[start+1]
			
			if edge1 in edge_dist.keys():
				dist = edge_dist[edge1]
			else:
				dist = 10e20
				
			total_length += dist
			path_dict[path_[start]] = (path_[start+1], dist)
			start = end -1
			end = end + 1
		return [total_length, path_dict]
		
	## Get the minimum path dictionary
	def edge_sequence(paths_list):
		paths_dict = {}
		min_dist = 0
		min_path = None
		min_dict = None
		for idx, path in enumerate(paths_list):
			edge_info = get_edges_score(path)
			score = edge_info[0]
			paths_dict[idx] = [path, score]
			if idx == 0 or min_dist > score:
				min_dist = score
				min_path = path
				min_dict = edge_info[1]
			
		return [paths_dict, min_dist, min_path, min_dict]

	edge_sequence(paths)
	
	## Print for displaying
	import pprint
	print('Minimum spanning path')
	pp = pprint.PrettyPrinter(indent=2)	
	pp.pprint(edge_sequence(paths)[3])

	## Return the minimum spanning path 
	return edge_sequence(paths)[3]
	'''
	
	
	g_key_list = list(g.keys())
	
	## convert g to list of edges
	edge_list = []
	for node in g_key_list:
		for edge in g[node]:
			edge_list.append((node, edge[0], edge[1]))
			
	min_span_path_list = kruskal(g_key_list, edge_list)
	pp.pprint(min_span_path_list)
	
	## convert to dictionary
	min_path_dict = {}
	for edge in min_span_path_list:
		if edge[0] in min_path_dict.keys():
			min_path_dict[edge[0]].append((edge[1], edge[2]))
		else:
			min_path_dict[edge[0]] = [(edge[1], edge[2])]
	pp.pprint(min_path_dict)
	
	
	
	
	
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
question3(g)
question3(g1)
question3(g2)
question3(g3)
question3(g4)
print()
