# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:29:14 2018

@author: lb13
"""


####################################################################
import networkx as nx

class DiGraph(object):
    """ Directed Graph"""
    # Data attribute: self.adj is a dict mapping each node (key) to a list
    #   of adjacent nodes (value)
    # List of nodes can be generated via: list(self.adj.keys())
    def __init__(self):
        self.adj = {}
    def addNode(self,u):
        """ add node u """
        assert u not in  self.adj, "Duplicate node"
        self.adj[u] = []
    def connect(self,u,v):
        """ connect node u to node v """
        assert u in self.adj and v in self.adj, "Node not in graph"
        assert v not in self.adj[u], "Already connected"
        self.adj[u].append(v)
    def __str__(self):
        """ cast graph into a string in which for each node u,
            we have a line  of the form:
            u: adjacent nodes separated commas"""
        s = ''
        for u in self.adj:
            t = ''
            for v in self.adj[u]:
                t= t+str(v)+','
            s = s+str(u)+' : '+t[:-1]+'\n'
            # We need to slice t[:-1] to remove the extra comma
            # Note that if self.adj[u] is empty, t will be the
            # empty string '',  but t[:-1] won't produce an error
            # since in Python, ''[:-1] is the empty string
        return s
    def draw(self):
        G=nx.DiGraph(directed=True)
        G.add_nodes_from(list(self.adj))
        G.add_edges_from([(u, v) for u in self.adj for v in self.adj[u] ])
        nx.draw(G,with_labels=True,node_color='w')









####################################################################
class UndirectedGraph(DiGraph):
    """ Undirected Graph"""
    def connect(self,node1,node2):
        DiGraph.connect(self,node1,node2)
        DiGraph.connect(self,node2,node1)
    def draw(self):
        G=nx.Graph()
        G.add_nodes_from(list(self.adj))
        G.add_edges_from([(u, v) for u in self.adj for v in self.adj[u] ])
        nx.draw(G,with_labels=True,node_color='w')

####################################################################
### Build Graph from file

def  buildGraphFromFile(fileName, undirected = False):
    nameHandle = open(fileName, 'r')
    adj = {}
    for line in nameHandle:
        if len(line.strip())!=0:
            L=line.strip().split(':')
            u = L[0].strip()
            if L[1].strip()=='':
                adj[u]=[]
            else:
                adj[u] = [s.strip() for s in L[1].split(',')]
    nameHandle.close()
    for u in adj:
        for v in  adj[u]:
            assert v in adj, "Invalid Input"
            if undirected:
                assert u in adj[v], "Invalid Input!"

    if undirected:
        G= UndirectedGraph()
    else:
        G= DiGraph()
    G.adj = adj
    return G


#G = buildGraphFromFile("DiGraph1.txt", undirected = False)
#G.draw()
#G = buildGraphFromFile("UndirectedGraph1.txt", undirected =True)
#G.draw()
####################################################################
### Graph Depth First Search (DFS)

def DFSVisit(G,u,parent):
    """ Recursive Depth First Search function
        Assumes G is a directed or undirected graph and u is node in G
        parent is a dict mapping each node (key) to its parent (value) in DFS traversal    """
    for v in G.adj[u]:
        if v not in parent:
            # If not visited yet, to avoid getting stuck in cycles
            parent[v]=u
            DFSVisit(G,v,parent)



####################################################################
### Graph Breadth First Search (BFS)

from circularQueue import Queue
def BFS(G,s):
    """ Breadth First Search function
        Assumes G is a directed or undirected graph and u is node in G
        Returns dict distance  mapping each node u (key) to the length of the  shortest
                     path from source s to u (value)
            and dict parent mapping each node (key) to its parent (value) in shotest path to source """
    assert s in G.adj, "node not in graph"
    parent = {s:None} # Initialize dict parent
    distance = {s:0} # Initialize dict distance
    # Initialize Q of max size the number of nodes in G: len(G.adj)
    Q = Queue(len(G.adj))
    Q.enqueue(s)
    while not Q.isEmpty():
#        print("Q:", Q)
#        print("distance:", distance)
#        print("parent",  parent)
#        print("--------")
        u = Q.dequeue()
        for v in G.adj[u]:
            if v not in distance:
                distance[v]=distance[u]+1
                parent[v]=u
                Q.enqueue(v)
    return (distance,parent)
