# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 04:46:41 2020

@author: shiha
"""
def get_Ti(Ti, t, dt):
    return Ti + (9.81 - ((Ti)**2 )/320) * dt



def main():
    Ti = 40
    t = 0
    dt = 3
    
    stringh = ("{:^7}\t\t"*3).format('i','t', 'Ti')
    print(stringh)
    print("{:8.0f}\t".format(0), end="")
    string = ("{:8.4f}\t"*2).format(t, Ti)
    print(string)
    
    for i in range(20):
        Ti = round(get_Ti(Ti, t, dt), 4)
        t = t + dt
        
        print("{:8.0f}\t".format(i+1), end="")
        string = ("{:8.4f}\t"*2).format(t, Ti)
        print(string)



if __name__ == "__main__":
    main()