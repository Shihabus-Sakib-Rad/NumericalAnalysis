# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:12:14 2021

@author: shiha
"""
import math


# put first derivative function here
def f(x, y):
    #return 3* (math.e)**(-x) - 0.4*y
    return 37.5 - 3.5*y

def main():
    # Change initial values here
    x0 = 0
    y0 = 40
    h = 1.5
    
    stringh = ("{:^7}\t\t"*6).format('i','x', 'y', 'k1', 'k2', 'y1')
    print(stringh)
#    print("{:8.0f}\t".format(0), end="")
#    string = ("{:8.3f}\t"*2).format(x0, y0, k1, k2)
#    print(string)
    
    for i in range(5):
        k1 = f(x0, y0)
        k2 = f(x0+h, y0+k1*h)
        
        y1 = y0 + 0.5*(k1+k2)*h
        x1 = x0 + h
        
        print("{:8.0f}\t".format(i), end="")
        string = ("{:8.3f}\t"*5).format(x0, y0, k1, k2, y1)
        print(string)
        

        x0 = x1
        y0 = y1
        


if __name__ == "__main__":
    main()