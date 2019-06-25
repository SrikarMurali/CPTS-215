# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:46:35 2017

@author: srika
"""

class BinaryTree:
    '''
    
    '''
    def __init__(self, root_data=None, left_child=None, right_child=None):
        '''
        
        '''
        self.root_data = root_data
        self.left_child = left_child
        self.right_child = right_child
        
    def get_right_child(self):
        '''
        
        '''
        return self.right_child

    def get_left_child(self):
        '''
        
        '''
        return self.left_child

    def set_root_data(self, data):
        '''
        
        '''
        self.root_data = data

    def get_root_data(self):
        '''
        
        '''
        return self.root_data
    
    def is_empty(self):
        '''
        
        '''
        return self.root_data == None
    
    def insert_left(self, new_data):
        '''
        
        '''
        if self.left_child == None:
            self.left_child = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self, new_data):
        '''
        
        '''
        if self.right_child == None:
            self.right_child = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right_child = self.right_child
            self.right_child = t
    
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
            print(tree.root_data, end=" ")
            self.pre_order_helper(tree.left_child)
            self.pre_order_helper(tree.right_child)
            
    def post_order_traversal(self):
        '''
        
        '''
        if not self.is_empty():
            self.post_order_helper(self)
            print()
        else:
            print("Empty tree")
            
    def post_order_helper(self, tree):
        '''
        
        '''
        if tree is not None:
            self.post_order_helper(tree.left_child)
            self.post_order_helper(tree.right_child)
            print(tree.root_data, end=" ")
            
    def level_order_traversal(self):
        '''
        
        '''
        if not self.is_empty():
            queue = [self.root_data]
            self.level_order_helper(self, queue)
            for data in queue:
                print(data, end=" ")
            print()
        else:
            print("Empty tree")
            
    def level_order_helper(self, tree, queue):
        '''
        
        '''
        if tree is not None:
            if tree.left_child is not None:
                queue.append(tree.left_child.root_data)
            if tree.right_child is not None:
                queue.append(tree.right_child.root_data)
            self.level_order_helper(tree.left_child, queue)
            self.level_order_helper(tree.right_child, queue)
            
    def in_order_traversal(self):
        '''
        
        '''
        if not self.is_empty():
            self.in_order_helper(self)
            print()
        else:
            print("Empty tree")
            
    def in_order_helper(self, tree):
        '''
        
        '''
        if tree is not None:
            self.in_order_helper(tree.left_child)
            print(tree.root_data, end=" ")
            self.in_order_helper(tree.right_child)