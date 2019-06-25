# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:17:56 2017

@author: srika
"""

from collections import deque
import sys
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Vertex:
    '''
    keep track of the vertices to which it is connected, and the weight of each edge
    '''
    def __init__(self, key):
        '''
        
        '''
        self.ID = key
        self.connected_to = {}
        self.visited = False
        self.distance = sys.maxsize
        self.previous = None
        
    def add_neighbor(self, neighbor, weight=0):
        '''
        add a connection from this vertex to another
        '''
        self.connected_to[neighbor] = weight

    def __str__(self):
        '''
        returns all of the vertices in the adjacency list, as represented by the connectedTo instance variable
        '''
        return str(self.ID) + ' connected to: ' + str([x.ID for x in self.connected_to])

    def get_connections(self):
        '''
        returns all of the connections for each of the keys
        '''
        return self.connected_to.keys()

    def get_ID(self):
        '''
        returns the current key id
        '''
        return self.ID

    def get_weight(self, neighbor):
        '''
        returns the weight of the edge from this vertex to the vertex passed as a parameter
        '''
        return self.connected_to[neighbor]
    
    def set_distance(self, dist):
        self.distance = dist
    
    def get_distance(self):
        return self.distance
    
    def set_previous(self, prev):
        self.previous = prev
    
    def set_visited(self):
        self.visited = True
        
    def __lt__(self, other):
        return self.get_distance() < other.get_distance()
    
    
class Graph:
    '''
    contains a dictionary that maps vertex names to vertex objects. 
    '''
    def __init__(self):
        '''
        
        '''
        self.vert_list = {}
        self.num_vertices = 0
        self.edges = []
        self.edge_labels = {}
        
    def __str__(self):
        '''
        
        '''
        edges = ""
        for vert in self.vert_list.values():
            for vert2 in vert.get_connections():
                edges += "(%s, %s)\n" %(vert.get_ID(), vert2.get_ID())
        return edges

    def add_vertex(self, key):
        '''
        adding vertices to a graph 
        '''
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        '''
        
        '''
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        '''
        in operator
        '''
        return n in self.vert_list

    def add_edge(self, f, t, cost=0):
        '''
        connecting one vertex to another
        '''
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
            
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)
        self.vert_list[t].add_neighbor(self.vert_list[f], cost)
        self.store_edges(f, t, cost)
        self.store_edges(t, f, cost)

    def store_edges(self, f, t, edge_label=''):
        self.edges.append((f, t, {f: edge_label}))
        self.edges.append((t, f, {t: edge_label}))
        self.edge_labels[(f, t)] = edge_label
        
    def get_vertices(self):
        '''
        returns the names of all of the vertices in the graph
        '''
        return self.vert_list.keys()
    
    def set_previous(self, current):
        self.previous = current
    
    def get_previous(self, current):
        return self.previous

    def __iter__(self):
        '''
        for functionality
        '''
        return iter(self.vert_list.values())
    
    def shortest(self, v, path):
        '''
        Make shortest path from v.previous
        '''

        if v.previous:
            path.append(v.previous.get_ID())
            self.shortest(v.previous, path)
        return
    

    
    def bfs(self, graph, start, goal):
        '''
        Find shortest path from start to goal and return the Kevin Bacon Number
        First Method 
        '''
        kb = 0
        frontier_queue = deque()
        frontier_queue.appendleft(start)
        discovered_set = set([start])
        try:
            while len(frontier_queue) > 0:
                curr_v = frontier_queue.pop()
                kb+=1

                for adj_v in curr_v.get_connections():
                    if adj_v not in discovered_set:
                        frontier_queue.appendleft(adj_v)
                        discovered_set.add(adj_v)
                    print(curr_v.get_ID() + ' was in a movie with ' + adj_v.get_ID() + 
                              ' in the ' +  curr_v.get_weight(adj_v) + '\n')
                    if goal in curr_v.get_connections():
                        return 'BFS: The Kevin Bacon Number for ' + str(goal.get_ID()) + ' is ' + str(kb)
        except:
            return 'Those vertices are not connected'



    def dijkstra(self, graph, start, goal):
        
        '''
        Find shortest path from start to goal and return the Kevin Bacon Number
        Second Method
        '''
        start.set_distance(0)
        unvisited_queue = [(v.get_distance(), v) for v in graph]
        heapq.heapify(unvisited_queue)
        kb = 0
        try:
            while len(unvisited_queue):
                uv = heapq.heappop(unvisited_queue)
                current = uv[1]
                current.set_visited()
    
                kb+=1
    
                for adj_v in current.get_connections():
                    if adj_v.visited:
                        continue
                    new_dist = current.get_distance()
    
    
                    if new_dist < adj_v.get_distance():
                        adj_v.set_distance(new_dist)
                        adj_v.set_previous(current)
                    print(current.get_ID() + ' was in a movie with ' + adj_v.get_ID() + 
                                  ' in the ' + current.get_weight(adj_v) + '\n')
                    if goal in current.get_connections():
                        return 'Dijkstra: The Kevin Bacon Number for ' + str(goal.get_ID()) + ' is ' + str(kb)
    
                    if kb >= len(unvisited_queue)-1:
                        return 'Those vertices are not connected'
                while len(unvisited_queue):
                    heapq.heappop(unvisited_queue)
                unvisited_queue = [(v.get_distance(), v) for v in graph if not v.visited]
                heapq.heapify(unvisited_queue)
                
    
            return 'Dijkstra: The Kevin Bacon Number for ' + str(goal.get_ID()) + ' is ' + str(kb)
        except:
            return 'Those vertices are not connected'
      
            


def get_file(file):
    with open(file, encoding='latin-1') as file:
        parsed = [l.strip().split('|') for l in file]
    return parsed


def main():
    actors = get_file('actors.txt')
    movies = get_file('movies.txt')
    movie_actors = get_file('movie-actors.txt')
    
    a_dict = {d[0]: d[1:] for d in actors}
    m_dict = {d[0]: d[1:] for d in movies}
    ma_dict = {}
    
    for i in range(len(movie_actors)):
        if movie_actors[i][0] not in ma_dict.keys():
            ma_dict[movie_actors[i][0]] = []
    for i in range(len(movie_actors)):
        ma_dict[movie_actors[i][0]].append(movie_actors[i][1])
        
    edges = []
    for k, v in ma_dict.items():
        for i, aindex1 in enumerate(v[:-1]):
            for aindex2 in v[i+1:]:
                edges.append((a_dict[aindex1][0], a_dict[aindex2][0], m_dict[k][0]))
                
    vertices = []
    for k, v in a_dict.items():
        vertices.append(v[0])
        
        
    g = Graph()
    
    for i in range(len(vertices)):
        g.add_vertex(vertices[i])
    
    for i in range(len(edges)):
        g.add_edge(*edges[i])
        
    '''
    Note: I tried to approach the Kevin Bacon search using two methods: A breadth first search, and Dijkstra's algorithim.
    Both algorithms seems to work, however after multiple tests, it appears that Dijkstra's algorithm is much faster than the BFS.
    Though both algorithms eventually find the goal vertex, on average Dijkstra's usually finds the shortest path.
    However I left both of them in, as they seem to work.
    If you wish you can look at both of them too.
    '''

    kb_actor = input('Please enter in an actor (capitalize the names): ')
#    while kb_actor != 'q':
    print(g.dijkstra(g, g.get_vertex('Kevin Bacon'), g.get_vertex(kb_actor)))
    print(g.bfs(g, g.get_vertex('Kevin Bacon'), g.get_vertex(kb_actor)))
#        kb_actor = input('Please enter in an actor (capitalize the names and q to quit): ')


    G = nx.Graph()
    G.add_nodes_from(g.get_vertices())
    G.add_weighted_edges_from(g.edges)
    
    pos = nx.shell_layout(G)
    nx.draw_networkx(G, pos=pos)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=g.edge_labels)
    plt.show()
    
if __name__ == '__main__':
    main()
