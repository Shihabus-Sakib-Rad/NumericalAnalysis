# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 03:43:21 2020

@author: shiha
"""

def f(x):
    return x**3 - 2 * x - 5


def error(old, new):
    return abs((old - new)/new) * 100

def get_xr(xl, xu):
    fxl = f(xl)
    fxu = f(xu)
    
    xr = (xu*fxl - xl*fxu)/(fxl - fxu)

    return xr


def main():
    xl = 2
    xu = 3
    xr = get_xr(xl, xu)
    
    stringh = ("{:^7}\t"*7).format('xl', 'xu', 'xr', 'error', 'fxl', 'fxu', 'fxr')
    print(stringh)
    
    for i in range(7):
        xr_old = xr
        xr = get_xr(xl, xu)
        
        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)
        
        #print(xl, xu, xr, error(xr_old, xr), sep='\t')
        string = ("{:7.4f}\t"*7).format(xl, xu, xr, error(xr_old, xr), fxl, fxu, fxr)
        print(string)
        
        test = fxr * fxl
        
        if test < 0:
            xu = xr
        else:
            xl = xr
        
        
        
        
if __name__ == "__main__":
    main()