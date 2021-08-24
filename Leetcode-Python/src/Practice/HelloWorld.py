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
   
class Duck:
    sound ='Quaack!'
    def quack(self):
        print(self.sound)
        
    def walk(self):
        print('walks')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
    
