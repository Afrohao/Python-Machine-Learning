def avg(lst):
    return sum(lst)/len(lst)



score = [] 
for t in range(5): #could input 5 groups of scores
    a = input()
    a = a.split()
    for i in range(len(a)):
        a[i] = eval(a[i])
    score.append(a)
#print(score)

'''for m in score:
    print(*m)'''

total = 0
for m in range(len(score)):
    print("student", m+1)
    for j in range(len(score[m])):
        print(" %d: %d"%(j+1, score[m][j]))
    total += sum(score[m])
    print(" sum:", sum(score[m]))
    print(" avg: %.2f"%avg(score[m]))

total_avg = 0   
for r in range(len(score)):
    total_avg += avg(score[r])
total_avg2 = total_avg/len(score)
print("total: %d,"%(total),"avg: %.2f"%total_avg2)

y = avg(max(score))
q = score.index(max(score))
print("highest avg: student %d:"%(q+1),"%.2f"%(y))    



