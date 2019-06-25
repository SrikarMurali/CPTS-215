# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:40:19 2017

@author: srikar
# CPTS 215 
# MA6
# 11/30/2017
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as s
from BinaryTree import BinaryTree

class BinaryMinHeap:

    def __init__(self):

        self.heap_list = [0]
        self.size = 0
        
    def __str__(self):

        return str(self.heap_list)
    
    def __len__(self):
 

        return self.size
    
    def __contains__(self, item):

        return item in self.heap_list
    
    def is_empty(self):

        return self.size == 0
    
    def find_min(self):

        if self.size > 0:
            min_val = self.heap_list[1]
            return min_val
        return None
        
    def insert(self, item):

        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size-1)
        
    def del_min(self):

        min_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.size]
        self.size = self.size - 1
        self.heap_list.pop()
        self.percolate_down(0)
        return min_val

    def min_child(self, index):

        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
            
    def build_heap(self, alist):

        index = len(alist) // 2 # any nodes past the half way point are leaves
        self.size = len(alist)
        self.heap_list = [0] + alist[:]
        while (index > 0):
            self.percolate_down(index)
            index -= 1
        
    def percolate_up(self, index):

        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index //= 2
            
    def percolate_down(self, index):

        while (index * 2) <= self.size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc
            
class HierarchicalCluster(BinaryTree):
    
    def __init__(self, root):
        super().__init__(root)
        
    def build_tree(self, lst):
        for i in range(len(lst)):
            if (2*i) < len(lst):
                self.insert_left(lst[i])
            if (2 * i + 1) < len(lst):
                self.insert_right(lst[i])
    
#    def pre_order_traversal(self):
#        return BinaryTree.pre_order_traversal(self)

    def pre_order_traversal(self):
        '''
        
        '''
        if not self.is_empty():
            self.pre_order_helper(self)
            print()
        else:
            print("Empty tree")
            
    def pre_order_helper(self, tree):
        '''
        
        '''
        if tree is not None:
            print(tree.root_data.centroid, end=" ")
            self.pre_order_helper(tree.left_child)
            self.pre_order_helper(tree.right_child)
            
class Pair:
    
    def __init__(self, items):
        self.items = items
        self.centroid = s.mean(items)
        
    
    
    def __lt__(self, other):
        return self.centroid < other.centroid
    
    def __le__(self, other):
        return self.centroid <= other.centroid

def get_data(data):
    data = np.array(pd.read_csv(data,  header=None))
    data = data.T
#    print(len(data))
    df = pd.DataFrame(data[1:], columns=data[0], dtype=float).T
    return df

def initialise(df):
    pairs_list = []
    for i in range(len(df.index)):
        pair = Pair(df.iloc[i])
        pairs_list.append(pair)
    return pairs_list

def get_pairs(lst):
    temp_list = lst.copy()
#    print(temp_list)
    while len(temp_list) > 1:
        for i in range(0, len(temp_list), 2):
            if  (2*i < len(temp_list) and (2*i + 1) < len(temp_list)):
                pair = Pair(temp_list[i].items + temp_list[i+1].items)
#                print(len(heap.heap_list))
                del temp_list[0]
                del temp_list[0]
#                print(len(heap.heap_list))
                lst.append(pair)
                temp_list.append(pair)
    return lst

def create_heatmap(df, heap_list):
    hm_list = []
    for i in range(len(heap_list)):
        hm_list.append(heap_list[i].items)
#    print(hm_list)
    h_clust = HierarchicalCluster(heap_list[0])
    h_clust.build_tree(heap_list[1:])
#    h_clust.pre_order_traversal()
    df2 = np.array(hm_list)
    df2 = pd.DataFrame(df2.reshape(2*df.shape[0]-1, df.shape[1]))
    hm = plt.pcolor(df2, cmap = plt.cm.bwr)
    plt.colorbar(hm)
    
def main():
#    data = np.array(pd.read_csv('https://raw.githubusercontent.com/gsprint23/cpts215/master/progassignments/files/simple.csv',  header=None))
#    data = data.T
##    print(len(data))
#    df = pd.DataFrame(data[1:], columns=data[0], dtype=float).T
    df = get_data('https://raw.githubusercontent.com/gsprint23/cpts215/master/progassignments/files/simple.csv')
#    print(df.shape)
#    pairs_list = []
#    for i in range(len(df.index)):
#        pair = Pair(df.iloc[i])
#        pairs_list.append(pair)
    pairs_list = initialise(df)
#    for i in range(6):
#        print(pairs_list[i].centroid)
    
    heap = BinaryMinHeap()
    heap.build_heap(pairs_list)
    heap.heap_list = heap.heap_list[1:]
#    print(heap.heap_list)
    heap.heap_list.sort(key=lambda x: x.centroid)
#    for i in range(heap.size):
#        print(heap.heap_list[i].centroid)
#    temp_list = heap.heap_list.copy()
#    print(temp_list)
#    while len(temp_list) > 1:
#        for i in range(0, len(temp_list), 2):
#            if  (2*i < len(temp_list) and (2*i + 1) < len(temp_list)):
#                pair = Pair(temp_list[i].items + temp_list[i+1].items)
##                print(len(heap.heap_list))
#                del temp_list[0]
#                del temp_list[0]
##                print(len(heap.heap_list))
#                heap.heap_list.append(pair)
#                temp_list.append(pair)
    heap.heap_list = get_pairs(heap.heap_list)
    create_heatmap(df, heap.heap_list)
#    for i in range(len(heap.heap_list)):
#        print(heap.heap_list[i].centroid)
#    hm_list = []
#    for i in range(len(heap.heap_list)):
#        hm_list.append(heap.heap_list[i].items)
##    print(hm_list)
#    h_clust = HierarchicalCluster(heap.heap_list[0])
#    h_clust.build_tree(heap.heap_list[1:])
##    h_clust.pre_order_traversal()
#    df2 = np.array(hm_list)
#    df2 = pd.DataFrame(df2.reshape(2*df.shape[0]-1, df.shape[1]))
#    hm = plt.pcolor(df2, cmap = plt.cm.bwr)
#    plt.colorbar(hm)
if __name__ == '__main__':
    main()