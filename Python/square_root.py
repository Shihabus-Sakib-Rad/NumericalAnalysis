# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 02:36:39 2020

@author: shiha
"""
error = 1


def relative_approx(old, new):
    return abs(old-new)/new *100

def find_next(old, x, n):
    factor = old**(n-1)
    return (old + x/factor)/2


def find_root(x, n=2):
    old = x/n
    new = find_next(old, x, n)
    global count
    count = 0
    while(relative_approx(old, new) > error):
        old = new
        new = find_next(old, x, n)
        count = count + 1
        print(new)
    
    return new


find_root(8000, 2)
print(count)