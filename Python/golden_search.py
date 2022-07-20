# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:06:18 2020

@author: shiha
"""

import math 


def f(x):
    #return 2.324815 * 10**(-14) * (-x**5 + 720000 * x**3 - 1.296 * 10**(11) * x)
    return 4 *x - 1.8 * x**2 + 1.2* x**3 - 0.3 * x**4


def error(xl, xu, xop):
    return abs(0.382 * (xu - xl)/xop) * 100


def get_xa(xl, xu):
    return xl + 0.618 * (xu - xl)


def get_xb(xl, xu):
    return xu - 0.618 * (xu - xl)


def main():
    xl = -2
    xu = 4
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
    