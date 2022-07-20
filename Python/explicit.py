# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:32:16 2021

@author: shiha
"""

def main():
    x0 = 100
    xn = 44
    lamda = 0.020875
    t0 = [x0, 0, 0, 0, xn]
    
    
    T = [t0]
    ti =[]
    
    # index
    n = len(t0)-1
    for j in range(3):
        ti =[] 
        # flashing ti
        for i in range(len(t0)):
            if i==0:
                ti.append(x0)
            elif i > 0 and i < n:
                temp = T[j][i] + lamda * (T[j][i+1] - 2* T[j][i] + T[j][i-1])
                temp = round(temp, 3)
                ti.append(temp)
            elif i == n:
                ti.append(xn)
            
        #appending in j+1
        T.append(ti)
            
   
    for i in range(len(T)):
        print(T[i])
if __name__ == "__main__":
    main()