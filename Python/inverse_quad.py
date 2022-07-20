# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 06:03:19 2020

@author: shiha
"""

def f(x):
    return x**3 - 2 * x - 5


def error(old, new):
    return abs((old - new)/new) * 100

def get_x3(x0, x1, x2, y0, y1, y2):
    lo = (y1 * y2) / ((y0 - y1) * (y0 - y2))
    l1 = (y0 * y2) / ((y1 - y0) * (y1 - y2))
    l2 = (y0 * y1) / ((y2 - y0) * (y2 - y1))
    
    return lo * x0 + l1 * x1 + l2 * x2


def main():
    x1 = 2.5
    x2 = 3
    x3 = 3.5
    stringh = ("{:^7}\t"*8).format('x0', 'x1', 'x2', 'x3', 'error', 'y0', 'y1', 'y2')
    print(stringh)
    
    for i in range(7):
        x0 = x1
        x1 = x2
        x2 = x3
        
        y0 = f(x0)
        y1 = f(x1)
        y2 = f(x2)
        
        x3 = get_x3(x0, x1, x2, y0, y1, y2)

        string = ("{:7.4f}\t"*8).format(x0, x1, x2, x3, error(x2, x3), y0, y1, y2)
        print(string)

        
        
if __name__ == "__main__":
    main()