# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:35:12 2020

@author: shiha
"""

import math 


def f(x):
    return 2*x / (4 + 0.8*x + x**2 + 0.2 * x**3)


def error(xl, xu, xop):
    return abs(0.382 * (xu - xl)/xop) * 100


def get_xa(xl, xu):
    return xl + 0.618 * (xu - xl)


def get_xb(xl, xu):
    return xu - 0.618 * (xu - xl)


def main():
    xl = 1
    xu = 3
    xop = (xl + xu)/2 ##dummy

    
    stringh = ("{:^7}\t\t"*8).format('xl', 'xu', 'xa','xb','xop' , 'error', 'fxa', 'fxb')
    print(stringh)
    
    for i in range(10):        
        xa = get_xa(xl, xu)
        xb = get_xb(xl, xu)
        
        fxa = f(xa)
        fxb = f(xb)
        
        #print(xl, xu, xr, error(xr_old, xr), sep='\t')
        string = ("{:8.5f}\t"*8).format(xl, xu, xa, xb, xop, error(xl, xu, xop), fxa, fxb)
        print(string)
        
        
        ## maximum deflection == more negative ..USE <<<<
        ## maximum value === default USE >>>>
        if fxa > fxb: ##change operator
            xl = xb
            xop = xa
        else:
            xu = xa
            xop = xb
        
        
        
        
if __name__ == "__main__":
    main()
    