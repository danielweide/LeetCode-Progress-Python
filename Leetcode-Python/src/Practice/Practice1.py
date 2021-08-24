'''
Created on 24 Aug 2021

@author: dankmint
'''

from decimal import *

def main():
    print("test")
    a = Decimal('.1')
    b = Decimal('.3')
    y = a + a + a -b
    x = 7//3
    print(x)
    print(y)
    
    z = None
    print(z)
    
    a = list(range(10))
    a[2]=33
    for i in a:
        print('i is {} aaa'.format(i))
    
    b = {'one':1,'two':2}
    b['two'] = 300
    for k,v in b.items():
        print('k: {}. v: {}'.format(k,v))
        
    c = (1,'two',3,[4, 'four'],5)
    d = (1,'two',3,[4, 'four'],5)
    print(type(c[3]))
    
    if c[1] == d[1]:
        print('yup')
    else:
        print('nope')
        
    if isinstance(c,tuple):
        print('yea')


if __name__ == '__main__':main()

