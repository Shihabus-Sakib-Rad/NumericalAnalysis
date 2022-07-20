# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 07:00:00 2020

@author: shiha
"""
import math 


def get_xy(x, y):
#    x_new = x + (0.13 - 0.1*x -0.007*y) * 0.4
#    y_new = y + (0.21 - 0.032*y - 0.007*x) *0.4
    x_new = x + (-10*x + 5*y + 1) * 0.4
    y_new = y + ( 5*x -5*y + 1.5) * 0.4
    return x_new , y_new

def main():
    x , y = 2, 2
    
    stringh = ("{:^7}\t\t"*2).format('x', 'y')
    print(stringh)
    string = ("{:8.5f}\t"*2).format(x,y)
    print(string)
    
    for i in range(7):
        x , y = round(x, 5) , round(y, 5)
        x , y = get_xy(x, y)

        #print(xl, xu, xr, error(xr_old, xr), sep='\t')
        string = ("{:8.5f}\t"*2).format(x,y)
        print(string)
        
        
        
if __name__ == "__main__":
    main()
    