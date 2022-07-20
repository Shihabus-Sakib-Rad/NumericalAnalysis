# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:12:14 2021

@author: shiha
"""
import math

# put First derivative function here
def f1(x, y, z):
    return z

# put Second derivative function here
def f2(x, y, z):
    #return (11*(math.e)**(-x)-3*z-5*y)/2
    return 2*y + 8*x*(9-x)

def main():
    # Change initial values here
    x0 = 0
    y0 = 0
    z0 = 4
    h = 3
    
    stringh = ("{:^7}\t\t"*8).format('i','x', 'y', 'z', 'f1', 'f2', 'y1', 'z1')
    print(stringh)
#    print("{:8.0f}\t".format(0), end="")
#    string = ("{:8.3f}\t"*2).format(x0, y0, k1, k2)
#    print(string)
    
    for i in range(5):
        
        y1 = y0 + f1(x0, y0, z0)*h
        z1 = z0 + f2(x0, y0, z0)*h
        x1 = x0 + h
        
        print("{:8.0f}\t".format(i), end="")
        string = ("{:8.3f}\t"*7).format(x0, y0, z0, f1(x0, y0, z0), f2(x0, y0, z0), y1, z1)
        print(string)
        

        x0 = x1
        y0 = y1
        z0 = z1
        


if __name__ == "__main__":
    main()