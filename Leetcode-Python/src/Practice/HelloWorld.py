'''
Created on 20 Aug 2021

@author: dankmint
'''
#Test 
print('Hello World')
x = 42
print('hello {}' .format(x))

y = 74
z = 71

if y > z:
    print('y < z: y is {} and z is {}'.format(y,z))
    
if x < y:
    print('x {} < y {}'.format(x,y))
elif x < z:
    print('x {} < z {}'.format(x,z))
else:
    print('oops')
    

n=0
words =['a','b','c','d','e']
for aa in words:
    print(aa)
    
def function(a):
    print(a)
    
function(10)
#while(n<5):
    #print(words[n])
   # n += 1
    
