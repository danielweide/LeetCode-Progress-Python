'''
Created on 24 Aug 2021

@author: dankmint
'''

def main():
    print('test')
    
    hungry = False
    x = 'feed the bear now!' if hungry else 'Do not feed the bear'
    print(x)
    
    x = 0x0a
    y=0x02
    z = x >> y
    
    print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
    print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

if __name__ == '__main__':main()
