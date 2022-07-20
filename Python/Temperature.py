# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 05:16:11 2020

@author: shiha
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 04:46:41 2020

@author: shiha
"""
    
def get_Ti(Ti, k, Ta, dt):
    return Ti - k * (Ti - Ta) * dt



def main():
    Ti = 37
    t = 0
    dt = 0.5
    k = 0.12
    Ta = 10
    
    stringh = ("{:^7}\t\t"*3).format('i','t', 'Ti')
    print(stringh)
    print("{:8.0f}\t".format(0), end="")
    string = ("{:8.4f}\t"*2).format(t, Ti)
    print(string)
    
    for i in range(10):
        Ti = round(get_Ti(Ti, k, Ta, dt), 4)
        t = t + dt
        
        print("{:8.0f}\t".format(i+1), end="")
        string = ("{:8.4f}\t"*2).format(t, Ti)
        print(string)



if __name__ == "__main__":
    main()