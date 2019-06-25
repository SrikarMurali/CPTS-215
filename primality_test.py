# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:40:59 2017

@author: srikar
"""
import math
"""
This function tests first tests if the number is even and greater than 2.
If it is than the program returns False as it is not prime. If not then
it continously does the modulus of n for each number starting from 3 til the
square root of n, plus one more by 2.
"""
def is_prime(n):
    if n%2 == 0 and n > 2:
        return False
    return all(n%i for i in range(3, int(math.sqrt(n)) + 1, 2))
"""
Intialize a result variable, and then iterate from 2 to the number m, while 
using the is_prime function as a helper to test primality. If i is prime
add it to the result.
"""
def sum_primes(m):
    res = 0
    for i in range(2, m+1):
        if is_prime(i):
            res+=i
    return res

def main():
    n = int(input("Please enter an integer >=2: "))
    res = is_prime(n)
    if res:
        print(n, "is prime!")
    else:
        print(n, "is not prime!")
    m = int(input("Please enter an integer >=2: "))
    res = sum_primes(m)
    print("The sum of primes from 2 to ", m, "is:", res)
    
if __name__ == '__main__':
    main()