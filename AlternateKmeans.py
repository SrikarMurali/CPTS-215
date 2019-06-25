# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:09:42 2017

@author: srika
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def compareRows(arr1, arr2):
    a1 = sum(arr1)
    a2 = sum(arr2)
    return a1 > a2 

def sort_centroids(samples): #just sorts the samples in increasing order of their sum
    order = [float(i.sum(axis=1)) for i in samples]
    std=sorted(zip(samples,order),key=lambda x: x[1],reverse=True)
    return [i[0] for i in std]

def main():
    test = [
             ([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]),
             ([0.2, 0.5, 0.2, 0.7, 0.5, 0.7, 0.2, 0.1, 0.6]),
             ([0.4, 0.4, 0.5, 0.1, 0.8, 0.9, 0.7, 0.9, 0.6]),
             ([0.2, 0.6, 0.2, 0.2, 0.1, 0.2, 0.3, 0.2, 0.2]),
             ([0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0]),
             ([0.2, 0.2, 0.2, 0.6, 0.6, 0.6, 0.6, 0.5, 0.8])]
    
    test = pd.DataFrame(test)
    
    #print('1', sum(test.iloc[0]))
    #print('2', sum(test.iloc[1]))
    #print('3', sum(test.iloc[2]))
    #print('4', sum(test.iloc[3]))
    #print('5', sum(test.iloc[4]))
    
    data = np.array(pd.read_csv('https://raw.githubusercontent.com/gsprint23/cpts215/master/progassignments/files/cancer.csv',  header=None))
    data = data.T
    df = pd.DataFrame(data[1:], columns=data[0], dtype=float).T
    
    num_centroids = 2
    
    samples = [test.sample(1) for i in range(num_centroids)]
    samples = sort_centroids(samples)
    print(samples)
    
    for i in range(num_centroids): #loop over centroids one by one
        d = test.drop(samples[i].index)
        gt = d.apply(compareRows, 1, arr2=samples[i].squeeze())
        df = pd.concat([d[~gt], samples[i], d[gt]])
        
        
    o=[float(i.sum(axis=1)) for i in samples]
    o.reverse()
    print('here comes o')
    print(o)
    print()
    print(test.sum(axis=1))
    
    print('end')
    print(test)
    
    #print('1', sum(test.iloc[0]))
    #print('2', sum(test.iloc[1]))
    #print('3', sum(test.iloc[2]))
    #print('4', sum(test.iloc[3]))
    #print('5', sum(test.iloc[4]))
    
    hm = plt.pcolor(test, cmap = plt.cm.bwr)
    plt.colorbar(hm)

if __name__ == '__main__':
    main()