# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:56:11 2017

@author: srika
"""
from collections import defaultdict
from collections import Counter
import string
import sys
import numpy as np


class HashTable:
    '''
    
    '''
    def __init__(self, size=11):
        '''
        
        '''
        self.size = size
        self.slots = [None] * self.size
        
    def put(self, item):
        '''
        Place an item in the hash table.
        Return slot number if successful, -1 otherwise (no available slots, table is full)
        '''
        hashvalue = self.hashfunction(item)
        slot_placed = -1
        if self.slots[hashvalue] == None or self.slots[hashvalue] == item: # empty slot or slot contains item already
            self.slots[hashvalue] = item
            slot_placed = hashvalue
        else:
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] != None and self.slots[nextslot] != item: 
                nextslot = self.rehash(nextslot)
                if nextslot == hashvalue: # we have done a full circle through the hash table
                    # no available slots
                    return slot_placed

            self.slots[nextslot] = item
            slot_placed = nextslot
        return slot_placed
    
    def insert(self, key):
        '''
        Insertion method using chaining. 
        Inserts new key into chain or returns -1 if there is no need
        '''
        slot = self.hashfunction(key)
        if key in self.slots[slot]:
            return -1
        else:
            self.slots[slot].append(key)
            return slot
        
    def get(self, item):
        '''
        returns slot position if item in hashtable, -1 otherwise
        '''
        startslot = self.hashfunction(item)
        
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1
    
    def remove(self, item):
        '''
        Removes item.
        Returns slot position if item in hashtable, -1 otherwise
        '''
        startslot = self.hashfunction(item)
        
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
                self.slots[position] = None
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1

    def hashfunction(self, item):
        '''
        Remainder method
        '''
        return item % self.size

    def rehash(self, oldhash):
        '''
        Plus 1 rehash for linear probing
        '''
        return (oldhash + 1) % self.size

class Map(HashTable, dict):

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

#    def __unicode__(self):
#        return unicode(repr(self.__dict__))

class DictEntry:
    
    def __init__(self, word, prob):
        d = dict()
        d[word] = prob
        
        
    def get_word(self):
        return self.word
    
#    def put(self, word, prod):
    
    
    def get_prob(self):
        return self.prob
    
    def match_pattern(self, pattern):
        if self.word == pattern:
            return self.word
        
class WordPredictor(DictEntry, Map):
    
    def __init__(self):
        self.total = 0
#        self.total = 0
        self.word_to_count = dict()
        self.prefix_to_entry = dict()
#        self.prefix_to_entry = Map(prefix, dictEntry)
    
    def train(self, training_file):
        try:
            f = open(training_file)
            contents = f.read()
            punctuation = contents.split()
            words = [w.strip(string.punctuation).lower() for w in punctuation]
            c = np.unique(words, return_counts=True)
#            freq = {}
            ct = 0
            for i in c[0]:
                self.word_to_count[i] = c[1][ct]
                self.total+=1
#                freq[i] = (c[1][ct])/len(words)
                ct+=1
#            for i in freq:
            return self.word_to_count
                
        except IOError:
            print("Sorry, I could not find the file", sys.argv[1])
            print("Please try again.")
            sys.exit()
    
    def train_word(self,word):
        if self.word_to_count[word] != None:
            self.word_to_count[word]+=1
        else:
            self.word_to_count[word] = 1
        return self.word_to_count
    
    def get_training_count(self):
        return self.total
    
    def get_word_count(self, word):
        if self.get_word_count[word] != None:
            return self.get_word_count[word]
        else:
            return 0
    
    def build(self):
        
        for key, value in enumerate(self.word_to_count):
            freq = value/self.total
            d = DictEntry(key, freq)
            for key, value in enumerate(self.prefix_to_entry):
                if self.prefix_to_entry[key][key] > d[key] or self.prefix_to_entry[key] == None:
                    self.prefix_to_entry[key] = d
    
    def get_best(self, prefix):
        return self.prefix_to_entry[prefix][0]
        
    def build_prob(wordlst):
        strings = wordlst.split()
        
        d = defaultdict(list)
        prev = ''
        for curr in strings:
            if prev != '':
                d[prev].append(curr)
            prev = curr
        
        
        for k in d.keys():
            n = d[k]
            unique_words = set(n)
            total = len(strings)
            probs = {}
            for unique_word in unique_words:
                probs[unique_words] = float(n.count(unique_words)/total)
           
            
        return probs
    
    def predict(probs, curr, nxt):
        if probs.has_key(curr):
            return probs[curr]
        return 0.0
    
#c = ['cat', 'dog', 'mouse', 'cat', 'dog']
#g = np.unique(c, return_counts=True)
#print(g)
#freq = {}
#ct = 0
#for i in g[0]:
#    print(ct)
#    freq[i] = (g[1][ct])/len(c)
#    ct+=1
#    
#print(freq)

w = WordPredictor()
w.train('C:/Users/srika/Documents/cpts215/prog_assignments/PA4/moby.txt')
print(w.build())

#print(w)  
#ht = HashTable()
#print(ht.put(61))
#print(ht.put(7))
#print(ht.put(12))
#print(ht.put(44))
#print(ht.put(92))
#print(ht.put(55))
#print(ht.put(9))
#print(ht.put(4))
#print(ht.put(21))
#print(ht.slots)
#print(ht.put(23))
#print(ht.put(39))
#print(ht.slots)
## hash table is full, no room to put again
#print(ht.put(90))
#print(ht.slots)
#print(ht.remove(55))
#print(ht.slots)