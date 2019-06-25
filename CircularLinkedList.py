# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:03:49 2017

@author: Srikar Murali
Class: CPTS 215 Fall 2017
Assignment: PA 3
Professor Ludlow


"""
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import timeit

class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.data)
class CDLLwS(object):
    def __init__(self, nodeClass):
        self.head = None
        self.nodeClass = nodeClass

        self.sentinel = self.nodeClass(None)
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self.len = 0
		
    def __len__(self):
        return self.len

    def __iter__(self):
        x = self.sentinel.next
        while x != self.sentinel:
            yield x
            x = x.next

    def __getitem__(self, i):
        if not -1 <= i < len(self):
            raise IndexError()
        elif i == 0:
            return self.sentinel.next
        elif i == -1:
            if len(self) > 0:
                return self.sentinel.prev
            else:
                raise IndexError()
        else:
            for j, x in enumerate(self):
                if j == i: return x

    def _insert_node(self, node, nextNode):
        node.prev = nextNode.prev
        node.next = nextNode
        node.prev.next = node
        node.next.prev = node
        self.len += 1

    def insert(self, i, node):
        self._insert_data(
                node,
                self.__getitem__(i, getNode=True) if len(self) > 0 else self.sentinel
        )

    def append(self, node):
        self._insert_node(
                node,
                self.sentinel
        )

    def pop(self, i=-1):
        x = self[i]

        x.prev.next = x.next
        x.next.prev = x.prev
		
        self.len -= 1
        return x

    def find(self, s, propName="data"):
        for x in self:
            if getattr(x, propName) == s:
                return x
        return None
    def __lt__(self,n1, n2):
       
        return n1.data < n2.data
    
    def __ge__(self, n1, n2):
        return n1.data >= n2.data
        
    def __str__(self):
        return str(map(lambda x:x.data, self))	
    def insertionSort(self, items):
        loops = 0
        comparisions = 0
        assignments = 1
        control = 0
        other = 0
        i = 1
        while i < items.len:
            j = i
            loops+=1
            assignments+=1
            comparisions+=1
            while j > 0:
                loops+=1
                if self.__lt__(self.__getitem__(j), self.__getitem__(j-1)):
                    tmp = self.__getitem__(j)
                    jint = tmp.data
                    tmp.data = tmp.prev.data
                    tmp.prev.data = jint
                    assignments+=4
                    comparisions+=1
                else:
                    other+=1
                    break 
                j-=1
                control+=1
    
            i+=1
            control+=1
        print('comparisions', comparisions)
        print('loops', loops)
        print('assignments', assignments)
        print('control', control)
        print('other', other)
        print('total', comparisions+loops+assignments+control+other)
        return items
    
    def merge(self, first, second):
        #print('inside merge')
        if first is None or first is self.sentinel:
            return second
        if second is None or second is self.sentinel:
            return first
#        print(first.data, second.data)
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
    
    def mergeSort(self, head):
        loops = 0
        comparisions = 0
        assignments = 1
        control = 0
        other = 0
#        if head is None or head is self.sentinel or head.next is None or head.next is self.sentinel:
            #return head
        if head is None or head is self.sentinel: 
            return head
        if head.next is None or head.next is self.sentinel:
            return head
         
        #print('here')
        second = self.split(head)
        loops+=1
        assignments+=4
        other+=1
        comparisions+=2
        #print('after split')
        head = self.mergeSort(head)
        second = self.mergeSort(second)
        assignments+=3
        comparisions+=1
        other+=1
        print('comparisions', comparisions)
        print('loops', loops)
        print('assignments', assignments)
        print('control', control)
        print('other', other)
        print('total', comparisions+loops+assignments+control+other)
        return self.merge(head, second)
    
    def split(self, head):
        fast = slow = head
        #print('fast1', fast.data)
        #print('slow1', slow.data)
        while True:
            if  fast.next is None or fast.next is self.sentinel:
                #print('inside fast.next')
                break
            if fast.next.next is None or fast.next.next is self.sentinel:
                #print('inside fast.next.next')
                break
            fast = fast.next.next
            slow = slow.next
       
#        print('slow', slow)
#        print('slow.next', slow.next)
        temp = slow.next
        slow.next = None

        
#        print('temp',temp.data)
        return temp
    def partition(self, left, head):
        
        #print('in partition')
        x = head.data
        i = left.prev
        j = left
        while j is not head:
            #print('j.data', j.data)
            if j.data <= x:
                if i is None:
                    i = left
                else:
                    i = i.next
                i.data, j.data = j.data, i.data
            j = j.next
        
        if i is None:
            i = left
        else:
            i = i.next
        i.data, head.data = head.data, i.data
        return i
    
    def quicksort(self, node):
        #print('in main quicksort')
        loops = 0
        comparisions = 0
        assignments = 1
        control = 0
        other = 0
        head = self.sentinel.prev
        #print(head, node)
        self.quicksortHelper(node, head)
        assignments+=1
        comparisions+=2
        print('comparisions', comparisions)
        print('loops', loops)
        print('assignments', assignments)
        print('control', control)
        print('other', other)
        print('total', comparisions+loops+assignments+control+other)
        
    
    def quicksortHelper(self, left, head):
        #print('in helper')
        #print(head, head.next, left)
        if head is not None and left is not head and left is not head.next:
            temp = self.partition(left, head)
            #print(temp)
            self.quicksortHelper(left, temp.prev)
            self.quicksortHelper(temp.next, head)
    
    
    def selectionsort(self, head):
        loops = 0
        comparisions = 0
        assignments = 0
        control = 0
        other = 0
        node1 = head
        assignments+=1
        #print(node1.data)
        while node1 is not None and node1 is not self.sentinel:
            minval = node1
            node2 = node1
            assignments+=2
            control+=1
            loops+=1
            while node2 is not None and node2 is not self.sentinel:
                if minval.data > node2.data:
                    comparisions+=1
                    minval = node2
                    assignments+=1
                node2 = node2.next
                assignments+=1
                loops+=1
            
            node1.data, minval.data = minval.data, node1.data
            node1 = node1.next
            assignments+=3
        print('comparisions', comparisions)
        print('loops', loops)
        print('assignments', assignments)
        print('control', control)
        print('other', other)
        print('total', comparisions+loops+assignments+control+other)

        return node1.next 
    
    def bubblesort(self, head):
        loops = 0
        comparisions = 0
        assignments = 0
        control = 0
        other = 0
        end = None
        swapped = True
        assignments+=2
        while swapped:
            curr = head
            #print('curr head', curr.data)
            swapped = False
            assignments+=1
            loops+=1
            while curr is not end and curr.next is not self.sentinel:
                #print('curr', curr.data)
                #print('curr.next.data', curr.next.data)
                loops+=1
                control+=1
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = True
                    assignments+=3
                    comparisions+=1
                curr = curr.next
                assignments+=1
            end = curr
            assignments+=1
        print('comparisions', comparisions)
        print('loops', loops)
        print('assignments', assignments)
        print('control', control)
        print('other', other)
        print('total', comparisions+loops+assignments+control+other)
            #print('end.data', end.data)
    
    def shellsort(self, gap, head, items):
        
        loops = 0
        comparisions = 0
        assignments = 0
        control = 0
        other = 0
        k = gap
        assignments+=1
        while k > 1:
            loops+=1
            comparisions+=1
            for i in range(k, items.len):
                temp = self.__getitem__(i)
#                print('temp.data', temp.data)
                j = i
                control+=1
                assignments+=2
                loops+=1
                while j >= k and self.__getitem__(j-k).data > temp.data:
                    x = self.__getitem__(j)
                    y = self.__getitem__(j-k)
                    x.data, y.data = y.data, x.data
                    other+=2
                    assignments+=2
                    comparisions+=2
#                    print('x.data', x.data)
#                    print('y.data', y.data)
                    j-=k
                    loops+=1
                z = self.__getitem__(j)
#                print('z.data', z.data)
#                print('temp2.data', temp.data)
                z.data, temp.data = temp.data, z.data
                assignments+=3
            k//=2
            assignments+=1
            if k == 1:
                self.insertionSort(items)
        print('comparisions', comparisions)
        print('loops', loops)
        print('assignments', assignments)
        print('control', control)
        print('other', other)
        print('total', comparisions+loops+assignments+control+other)
        
    def printList(self, node):
        temp = node
        print("Forward Traversal using next poitner")
        while(node is not None):
            print(node.data,)
            temp = node
            node = node.next
        print("\nBackward Traversal using prev pointer")
        while(temp):
            print(temp.data,)
            temp = temp.prev
            
            
def main():
    
#    df = pd.DataFrame(pd.read_csv('dataframe.csv'))
#    print(df)
#    df.to_csv('merge_sort_results.csv')
#    insertionSort = pd.Series([440030, 432137, 433564, 432026], index=[500, 1000, 5000, 10000], name="Insertion Sort")
#    selectionSort = pd.Series([258667, 1018805, 25109559, 100224049], index=[500, 1000, 5000, 10000], name="Selection Sort")
#    quickSort = pd.Series([4, 4, 4, 4], index=[500, 1000, 5000, 10000], name="Quick Sort")
#    bubbleSort = pd.Series([953702, 3810890, 98405570, 398232410], index=[500, 1000, 5000, 10000], name="Bubble Sort")
#    shellSort = pd.Series([37892, 88505, 379716, 1794158], index=[500, 1000, 5000, 10000], name="Shell Sort")
#    mergeSort = pd.Series([14, 14, 14, 14], index=[500, 1000, 5000, 10000], name="Merge Sort")
#    sers = [insertionSort, selectionSort, quickSort, bubbleSort, shellSort, mergeSort]
#    
#    x_locs = np.arange(1, 5)
#    x_labels = [500, 1000, 5000, 10000]
#    f, ax = plt.subplots()
#    ax.set_title("Random")
#    ax.set_ylabel("Total Operations")
#    ax.set_xlabel("List size N")
#    ax.set_xticks(x_locs)
#    ax.set_xticklabels(x_labels)
#    for ser in sers:
#        print(ser.name)
#        plt.plot(x_locs, ser, label=ser.name)
#    plt.legend(loc=0)
#    plt.savefig("Random")
    #print(df.iloc[0][0])
    x = CDLLwS(Node)
    for i in range(1,11):
        j = Node(random.randint(1, 10))
        x.append(j)
    start = time.time()
    x.bubblesort(x.sentinel.next)

    end = time.time()
    print('seconds', end-start)
#    for elem in x:
#        print(elem)
#    start_time = time.time()
#    x.insertionSort(x)
#    print(time.time() - start_time)
#    
    

if __name__ == '__main__':
    main()        
#x.append(Node(3))
#x.append(Node(4))
#x.append(Node(20))
#x.append(Node(5))
#x.append(Node(7))
#x.append(Node(12))
#x.append(Node(9))
#x.append(Node(18))
#x.append(Node(21))
#x.append(Node(25))
#x.append(Node(19))
#x.append(Node(37))
#for elem in x:
#   print(elem)

#print(x.sentinel)
#y = CDLLwS(Node)
#print('sent',x.sentinel.next)
#print(x.sentinel.prev)
#print('starting quicksort')
#x.quicksort(x.sentinel.next)
#for elem in x: # for quicksort do not assign to y
#    print(elem)
#x.printList(x.sentinel)
#x.insertionSort(x)
#x.shellsort(x.len//2, x.sentinel.next, x)
#for elem in x:
#    print(elem)

#for quick sort and insertion sort use for i in x

#for mergesort use the printlist function
