# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:04:14 2017

@author: srikar
Programming Assignment #1
"""
import sys
import re
from scanner import Scanner
"""
Creates a scanner object from the file, and then reads each line in the file.
Aftewards it creates a list, but before that first filters out all of the Nones
from the list before returning.
"""
def read_records(file):
    s = Scanner(file)
    lst = []
    while s.readline():
        line = s.readline().rstrip()
        line = line.replace("@", "")
        lst.append(line)
    lst = list(filter(None, lst))
    return lst

#def find_hashtag(file):
#    s = Scanner(file)
#    hashtag = dict()
#    indices = []
#    while s.readline():
#        line = s.readline().rstrip()
#        if '#' in line:
#            idx = line.index('#')
#            indices.append(line[idx:])
#    eachline = indices.split(' ')
#    for i in range(len(eachline)):
#        if '#' not in eachline[i]:
#            eachline.remove(eachline[i])
#    print(eachline)
"""
Takes a scanner object, reads each line and puts it in a list.
"""
def create_records(scan):
    x = scan.readline()
    x = x.replace("@", "")
    y = list([x])
    return y
"""
Code first finds the index the date begins at, then creates two date objects.
It then splits the date into its components, year, month, etc.
Then iterates over the date object. If it gets to the hour:minute:second part,
it converts it all to seconds for ease of comparision.
"""
def is_more_recent(rec1, rec2):
    idx1 = rec1.rindex('" ')
    idx2 = rec2.rindex('" ')
    date1 = rec1[idx1+1:]
    date2 = rec2[idx2+2:]
    lst1 = list(date1.split())
    lst2 = list(date2.split())
    i = 0
    while i < 4:
        if ':' in lst1[i]:
            time = lst1[i].rsplit(':')
            seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
            lst1[len(lst1)-1] = seconds
        if ':' in lst2[i]:
            time = lst2[i].rsplit(':')
            seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
            lst2[len(lst2)-1] = seconds
        if int(lst1[i]) > int(lst2[i]):
            return True
        elif int(lst1[i]) <= int(lst2[i]):
            return False
        else:
            i+=1
"""
Code compares each tweet in both lists, and adds the more recent one
to the final list.
"""
def merge_and_sort_tweets(lst1, lst2):
    fin = []
    i, j = 0, 0
    total = len(lst1) + len(lst2)
    while len(fin) != total:
        if len(lst1) == i:
            fin += lst2[j:]
        elif len(lst2) == j:
            fin+= lst1[i:]
        elif is_more_recent(lst1[i], lst2[j]):
            fin.append(lst1[i])
            i+=1
        else:
            fin.append(lst2[j])
            j+=1
    return fin
"""
Function takes a list and the name of the file,
and writes each line to the new file.
"""
def write_records(lst, name):
    file = open(str(name), 'w')
    for item in lst:
        file.write("%s\n" % item)
"""
Main program which takes input, and calls other function. Prints first five tweets.
"""
def main():
#    find_hashtag('tweet1_demo.txt')
    print('Reading files...')
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output = sys.argv[3]
    lst1 = read_records(file1)
    lst2 = read_records(file2)
   
    if len(lst1) > len(lst2):
        print("tweet1.txt has the most tweets with", len(lst1), '.')
    else:
        print("tweet2.txt has the most tweets")
    print('Merging files...')
    lst = merge_and_sort_tweets(lst1, lst2)
    print('Writing files...')
    write_records(lst, output)
    lst = lst[::-1]
    for i in range(5):
        idx = lst[i].index('" ')
        print(lst[i][:idx+1])

if __name__ == '__main__':
    main()
    