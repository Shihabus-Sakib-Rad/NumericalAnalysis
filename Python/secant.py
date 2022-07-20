
"""
Created on Tue Nov  3 03:43:21 2020

@author: shiha
"""

def f(x):
    return x**3 - 2 * x - 5


def error(old, new):
    return abs((old - new)/new) * 100

def get_x1(x_old, x0):
    return x0 - (f(x0)*(x0 - x_old))/(f(x0) - f(x_old))


def main():
    x0 = 2.5
    x1 = 3
    stringh = ("{:^7}\t"*6).format('x_old', 'x0', 'x1', 'error', 'fx0', 'fx_old')
    print(stringh)
    
    for i in range(7):
        x_old = x0
        x0 = x1
        x1 = get_x1(x_old, x0)

        string = ("{:7.4f}\t"*6).format(x_old, x0, x1,  error(x0, x1), f(x0), f(x_old))
        print(string)

        
        
if __name__ == "__main__":
    main()