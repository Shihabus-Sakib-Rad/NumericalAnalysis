# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:12:14 2021

@author: shiha
"""
import math


# put first derivative function here
def f(x, y):
    return 3* (math.e)**(-x) - 0.4*y

def main():
    # Change initial values here
    x0 = 0
    y0 = 5
    h = 1.5
    
    stringh = ("{:^7}\t\t"*5).format('i','x', 'y', 'f', 'y1')
    print(stringh)
#    print("{:8.0f}\t".format(0), end="")
#    string = ("{:8.3f}\t"*2).format(x0, y0, k1, k2)
#    print(string)
    
    for i in range(5):
        y1 = y0 + f(x0, y0)*h
        x1 = x0 + h
        
        print("{:8.0f}\t".format(i), end="")
        string = ("{:8.3f}\t"*4).format(x0, y0, f(x0, y0), y1)
        print(string)
        

        x0 = x1
        y0 = y1
        


if __name__ == "__main__":
    main()