# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:07:48 2017

@author: srikar murali
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import random
#%matplotlib inline

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

#def chooseCenter(data, centers):
#    length = data.shape
#    cent = []
#    while len(cent) < centers :
#        x = random.randrange(0,length[0])
#        y = random.randrange(0,length[1])
#        if data.iloc[x][y] not in cent:
#            d = truncate(data.iloc[x][y],2)
#            cent.append(d)
#    return cent


#def distance(val, center):
#    return math.sqrt((val- center)**2)



def getDistance(arr1, arr2):
    trDist = []
    for i in range(len(arr1)):
        trDist.append(abs(arr1[i]-arr2[i]))
    #print(trDist)
    return sum(trDist)
    
    
    
#def getDistances(centers, data):
#    length = data.shape
#    dist = []
#    for i in range(length[0]):
#        for j in range(length[1]):
#            y = []
#            for k in range(len(centers)):
#                val = distance(data.iloc[i][j], centers[k]) 
#                y.append(truncate(val,3))
#            dist.append(y)
#    return dist

#gets center
def getCenter(df, k):
    n = random.randint(0, len(df)-1)
    return df.iloc[n]

#computes distance to center
def computeDistance(df, k, centroid):
     c = np.array_split(df, k)
     d = []
     overSum = 0
#     for i in range(len(c)):
#         n = pd.DataFrame(np.array(c[i]))
#         cent = getCenter(n, k)
#         y = []
#         for j in range(len(n)):
#             dist = getDistance(cent, n.iloc[j])
#             y.append(dist)
#         d.append(y)
#         overSum+=sum(y)
#     return overSum
     print(len(c))
     for i in range(len(c)):
         n = pd.DataFrame(np.array(c[i]))
         y = []
         for j in range(len(n)):
             dist = getDistance(centroid, n.iloc[j])
             y.append(dist)
         d.append(y)
         overSum+=sum(y)
     return overSum


def splitIntoClusters(df, k):
    d = []
    for i in range(k):
        d.append([])
    return d

def compareRows(arr1, arr2):
    a1 = sum(arr1)
    a2 = sum(arr2)
    return a1 > a2

#checks if function is in cluster
def checkCluster(df, k, cluster, row):
    c = np.array_split(df, k)
    n = pd.DataFrame(c[cluster-1])
    return row in n

#gets seconds lowest value
def ss(e):
    if len(e)==2 and e[0]<=e[1]:return e[1]
    return ss(e[:-1]) if e[0]<=e[-1]>=e[1] else ss([e[-1]]+e[:-1])

def main():
    data = np.array(pd.read_csv('https://raw.githubusercontent.com/gsprint23/cpts215/master/progassignments/files/cancer.csv',  header=None))
    data = data.T
    #print(data)
    df = pd.DataFrame(data[1:], columns=data[0], dtype=float).T
    test = [
         ([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]),
         ([0.2, 0.5, 0.2, 0.7, 0.5, 0.7, 0.2, 0.1, 0.6]),
         ([0.4, 0.4, 0.5, 0.1, 0.8, 0.9, 0.7, 0.9, 0.6]),
         ([0.2, 0.6, 0.2, 0.2, 0.1, 0.2, 0.3, 0.2, 0.2]),
         ([0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0]),
         ([0.2, 0.2, 0.2, 0.6, 0.6, 0.6, 0.6, 0.5, 0.8])]
    
    test = pd.DataFrame(test)
    sampled = df.sample(1)
    d = df.drop(sampled.index)
    gt = d.apply(compareRows, 1, arr2=sampled.squeeze())
    df = pd.concat([d[~gt], sampled, d[gt]])
#    curr = computeDistance(test, k, sampled)
    
    hm = plt.pcolor(df, cmap = plt.cm.bwr)
    plt.colorbar(hm)
    #print(df)
    #df = df.iloc[::-1]
#    print(df)
#    print(df.iloc[1][9])
#    print(df)
#    print(df.iloc[0][1])
#    heatmap = plt.pcolor(df, cmap=plt.cm.bwr)
#    plt.colorbar(heatmap)
#    c = chooseCenter(df, 3)
#    print(c)
#    #print(len(c))
#    dist = getDistances(c, df)
#    #print(dist)
#    y = findClosest(df, dist)
##    q = []
##    for i in range(len(c)):
##        q.append([])
##    #print(q)
#    j = computeNewCenter(df, y)
#    #print(j)
#    length = df.shape
#    oldFrame = pd.DataFrame(np.ndarray((length[0],length[1])))
#    oldFrame = oldFrame.fillna(0)
#    ct=0
#    while y.equals(oldFrame) == False:
#        ct+=1
#        oldFrame = y.copy()
#        c = computeNewCenter(df, oldFrame)
#        #print(c)
#        dist = getDistances(c, df)
#        #print(dist)
#        y = findClosest(df, dist)
#        #print(y)
#    #plt.pcolor(df, cmap=plt.cm.bwr)
#
#    l = []
#    for i in range(len(y)):
#        for j in range(len(y[0])):
#            if y.iloc[i][j] == 1:
#                l.append(df.iloc[i][j])
#    
#    for i in range(len(y)):
#        for j in range(len(y[0])):
#            if y.iloc[i][j] == 2:
#                l.append(df.iloc[i][j])
#    for i in range(len(y)):
#        for j in range(len(y[0])):
#            if y.iloc[i][j] == 0:
#                 l.append(df.iloc[i][j])
#   
#    
#    l = np.ndarray((length[0],length[1]))
#    l = pd.DataFrame(l)
#    print(l)
#    hm = plt.pcolor(l, cmap=plt.cm.bwr)
#    plt.colorbar(hm)    
#    print(y)
#    print(c)
#    print(ct)
    #plt.pcolor(y, cmap=plt.cm.bwr)
    #print(df.iloc[0])
    #print(getDistance(df.iloc[3], df.iloc[4]))
    k = 2
#    count = 0
#    count2 = len(df)//2 - 1
#    print(count2)
    c = splitIntoClusters(df, k)
    centroid = getCenter(df, k)
    #print(centroid)
#    n = np.array(df)
#    df2 = df.iloc[:(len(df)//2)].copy()
#    df3 = df.iloc[len(df)//2:].copy()
#    print('0', df2.iloc[0])
#    print('dfend', df.iloc[len(df)-1])
#    df2.iloc[0] = df.iloc[len(df)-1]
#    print(df2.iloc[0])
    
#    g = 0
    
#    sampled = df.iloc[0]
#    del sampled.index.name
#    print(sampled)
#    curr = computeDistance(test, k, sampled)
#    print('curr', curr)
#    print('curr', curr)
#    old = curr
#    while float(curr) <= float(old):
    
#    print('curr', curr)
#    print('old', old)
#    print(df)
#    while curr <= old:
#    count = 0
#    count2 = len(df)//2 - 1
#    centroid = getCenter(df, k)
#    for i in range(len(df)):
##        print('i ', df.iloc[i])
#        if not compareRows(centroid, df.iloc[i]):
#            df2.append(df.iloc[i])
#            count+=1
#        else:
#            df3.append(df.iloc[i])
#            count2+=1
##        print('c', count)
##        print('c2', count2)
#    df2.append(df3)
#    print(df2)
#    old = curr
#    curr = computeDistance(df2, k, centroid)
#    print('old', old)
#    print('curr', curr)
#    print(g)   
    #print(df2)
#    print(c)
 
#    c = computeDistance(df, k)
#    print(c)
#    print(df.iloc[0])
#    df.iloc[1],df.iloc[2] = df.iloc[2].copy(), df.iloc[1].copy()
#    df.iloc[3], df.iloc[4] = df.iloc[4].copy(), df.iloc[3].copy()
#    print(df)
#    c = computeDistance(df, k)
#    print(c)
#    k = 2
#    distances = []
#    i = 0
#    curr = computeDistance(df, k)
#    old = curr
#    cluster = 0
#    z = 0
##    for i in range(1000):
#    while curr <= old:
#        
#        for i in range(len(df)):
#            y = []
#            for j in range((len(df) - i + 1)//k):
#                p = getDistance(df.iloc[i], df.iloc[j])
#                y.append(truncate(p, 2))
#            distances.append(y)
#            mi = y.index(min(y))
#            mx = y.index(max(y))
##            if not checkCluster(df, k, cluster, mi):
#            df.iloc[mi], df.iloc[mx] = df.iloc[mx].copy(), df.iloc[mi].copy()
#    #            if z > (len(df)//k-1):
#    #                cluster+=1
#    #                z = 0
#    #                if cluster > (k-1):
#    #                    cluster = 0
#    #            z+=1
#    #            print(cluster)
#        old = curr
#        curr = computeDistance(df, k)
#    print('curr', curr)
#    print('old', old)
#    print(distances)
#    print(df)
#    hm = plt.pcolor(df, cmap=plt.cm.bwr)
#    plt.colorbar(hm)
#        
#    distances = []
#    i = 0
##    flag = 1
#    dist = computeDistance(df, k)
#    dist2 = computeDistance(df, k)
#    while dist <= dist2:
#        while i < len(df):
#            y = []
#            for j in range(i, len(df)):
#                
#                p = getDistance(df.iloc[i], df.iloc[j])
#                y.append(truncate(p, 2))
#            distances.append(y)
#            mi = y.index(ss(y))
#            mx = y.index(max(y))
#            df.iloc[mi], df.iloc[mx] = df.iloc[mx].copy(), df.iloc[mi].copy()
##            if flag == 1:
##                i = i + len(df)//2 + 1
##            else:
##                i= i - len(df)//2 + 1
##            flag*=-1
#        dist = dist2
#        dist2 = computeDistance(df, k)
##    print(distances)
##    print(df)
#    hm = plt.pcolor(df, cmap = plt.cm.bwr)
#    plt.colorbar(hm)
#    
 

###get distance for each cluster and overall distance to work
###make sure the random center function works
###traverse to the next cluster, and make sure swaps aren't happening in the same cluster
   
if __name__ == '__main__':
    main()

