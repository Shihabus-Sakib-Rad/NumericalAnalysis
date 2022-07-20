# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 03:43:21 2020

@author: shiha
"""
import math 

def f(x):
    return 54 * (1- (math.e)**(-0.18355 *x)) -30

def f_prime(x):
    return 9.9117 * (math.e)**(-0.18355 *x)


def error(old, new):
    return abs((old - new)/new) * 100

def get_xr(xr_old):
    return xr_old - f(xr_old)/f_prime(xr_old)


def main():
    xr = 5
    stringh = ("{:7}\t\t"*5).format('xr_old', 'xr', 'error', 'f', 'f_prime')
    print(stringh)
    for i in range(7):
        xr_old = xr
        xr = round(get_xr(xr_old), 6)

        string = ("{:8.6f}\t"*5).format(xr_old, xr, error(xr_old, xr), f(xr_old), f_prime(xr_old))
        print(string)

        
        
if __name__ == "__main__":
    main()