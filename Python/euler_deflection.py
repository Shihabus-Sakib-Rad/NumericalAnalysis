# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:15:51 2020

@author: shiha
"""

def get_Ti(Ti, t, dt):
    return Ti + (1/156000) *(4 * t**3 - 48 * t**2 + 192 * t)* dt



def main():
    Ti = 0
    t = 0
    dt = 0.4
    
    stringh = ("{:^7}\t\t"*3).format('i','t', 'Ti 10^(-4)')
    print(stringh)
    print("{:8.0f}\t".format(0), end="")
    string = ("{:8.4f}\t"*2).format(t, Ti)
    print(string)
    
    for i in range(20):
        
#        Ti = round(get_Ti(Ti,t, dt), 6)
        Ti = get_Ti(Ti,t, dt)
        t = t + dt
        
        
        print("{:8.0f}\t".format(i+1), end="")
        string = ("{:8.6f}\t"*2).format(t, Ti * 10**4)
        print(string)



if __name__ == "__main__":
    main()