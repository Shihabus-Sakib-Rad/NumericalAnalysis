# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 03:19:28 2020

@author: shiha
"""
import math 


def f(x) -> float:
    return x**3 - 2 * x - 5
    #return (804.42/x)* (1 - (math.e)**(-2*x/41)) - 36
    # return 53.44 * (1 - (math.e)**(-0.18355 * x)) - 30


def error(old, new):
    return abs((old - new)/new) * 100

def get_xr(xl, xu):
    xr = (xl + xu)/2
    return xr

def main():
    xl = 1
    xu = 10
    xr = get_xr(xl, xu)
    
    stringh = ("{:^7}\t\t"*7).format('xl', 'xu', 'xr', 'error', 'fxl', 'fxu', 'fxr')
    print(stringh)
    
    for i in range(7):
        xr_old = xr
        xr = round(get_xr(xl, xu), 5)
        
        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)
        #print(xl, xu, xr, error(xr_old, xr), sep='\t')
        string = ("{:8.5f}\t"*7).format(xl, xu, xr, error(xr_old, xr), fxl, fxu, fxr)
        print(string)
        
        test = fxr * fxl
        
        if test < 0:
            # sign is not same as xl
            xu = xr
        else:
            xl = xr
        
        
        
        
if __name__ == "__main__":
    main()
    