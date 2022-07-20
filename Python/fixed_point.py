# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 05:15:34 2020

@author: shiha
"""
import math 

def f(x):
    return (math.e)**(-x) - x

def g(x):
    return f(x)+x

def error(old, new):
    return abs((old - new)/new) * 100

def get_xr(x_old):
    return g(x_old)


def main():
    xr = 0
    stringh = ("{:^7}\t"*3).format('xr_old', 'xr', 'error')
    print(stringh)
    
    for i in range(8):
        xr_old = xr
        xr = get_xr(xr_old)

        string = ("{:7.4f}\t"*3).format(xr_old, xr, error(xr_old, xr))
        print(string)

        
        
if __name__ == "__main__":
    main()