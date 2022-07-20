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
    return (11*(math.e)**(-x)-3*z-5*y)/2

def main():
    # Change initial values here
    x0 = 0
    y0 = 7
    z0 = 13
    h = 0.25
    
    stringh = ("{:^7}\t\t"*10).format('i','x', 'y', 'z', 'k1y', 'k1z', 'k2y', 'k2z', 'y1', 'z1')
    print(stringh)
#    print("{:8.0f}\t".format(0), end="")
#    string = ("{:8.3f}\t"*2).format(x0, y0, k1, k2)
#    print(string)
    
    for i in range(5):
        k1y = f1(x0, y0, z0)
        k1z = f2(x0, y0, z0)
        
        k2y = f1(x0+h, y0+k1y*h, z0 + k1z*h)
        k2z = f2(x0+h, y0+k1y*h, z0 + k1z*h)
        
        y1 = y0 + 0.5*(k1y+k2y)*h
        z1 = z0 + 0.5*(k1z+k2z)*h
        x1 = x0 + h
        
        print("{:8.0f}\t".format(i), end="")
        string = ("{:8.3f}\t"*9).format(x0, y0, z0, k1y, k1z, k2y, k2z, y1, z1)
        print(string)
        

        x0 = x1
        y0 = y1
        z0 = z1
        


if __name__ == "__main__":
    main()