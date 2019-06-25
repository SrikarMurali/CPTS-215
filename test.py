# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:42:47 2017

@author: srika
"""

## Class for node
#class node:
#    __slots__ = ('name','neighbor')
## Node constructor
#def mkNode(name):
#    n = node()
#    n.name = name
#    n.neighbor = []
#    return n
## Find if node is in the graph
#def findNode(nodelist, name):
#    for n in nodelist:
#        if n.name == name:
#            return n
##Creates graph
#def loadGraphFile(file):
#    graph = []
#    for line in file:
#        contents = line.split()
#        movieName = contents[0]
#        actorNames = [contents[i]+ " " + contents[i+1] for i in range(1, len(contents), 2)]
#        movieNode = findNode(graph, movieName)
#        if movieNode == None:
#            movieNode = mkNode(movieName)
#            graph.append(movieNode)
#        for actorName in actorNames:
#            actorNode = findNode(graph,actorName)
#            if actorNode == None:
#                actorNode = mkNode(actorName)
#                graph.append(actorNode)
#            actorNode.neighbor.append(movieNode)
#            movieNode.neighbor.append(actorNode)
#    return graph
#def loadGraphFileName(filename):
#    return loadGraphFile(open(filename))
#
#
#file = loadGraphFileName('test1.txt')
#g = loadGraphFile(file)
