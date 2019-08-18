guess = eval(input());

#guess = eval(input());

import random
ans = random.randint(1,5)

if ans == guess:
    print('你猜對了 答案正是', guess)
else:
    print('猜錯了了喔 其實是', ans)

# should use random to be ans
