


#ans = int(input())
print('1 < ? < 100')
n = int(input())

import random
ans = random.randint50(1,100)

Max_num = 100
Min_num = 1

while n != ans:
   
    if n>ans:
            Max_num = n
            #print(Max_num)
            print('wrong answer, guess smaller')
            print(Min_num,'< ? <', Max_num)
 
    elif n<ans:
            Min_num = n
            #print(Min_num)
            print('wrong answer, guess larger')
            print(Min_num,'< ? <', Max_num)

    n = int(input())
else:
    print('bingo answer is', ans)
    
