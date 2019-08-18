
n = eval(input())
import math
#m = int(math.sqrt(n))
#print(m)

if n ==2:
    print(n,'is prime')
elif n == 3:
    print(n-1,'is prime')
    print(n,'is prime')
else:
    print('2 is prime')
    print('3 is prime')

    for i in range(2,n+1):
        p = int(math.sqrt(i))+1
        # in case for 2
        for s in range(2,p):
            if(i % s == 0): # is i is not prime
                break
            elif(s==p-1):
                print(i,'is prime')
            
        
