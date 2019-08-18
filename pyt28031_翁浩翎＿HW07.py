
def Top(stus):
    average = 0
    top = 0
    for i in range (5):
        if stus[i].avg() > average:
            top = i
            average = stus[i].avg() 
    stus[top].show()




class student:
 
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grade = []
        
    def avg(self):
        result = sum(self.grade)/len(self.grade)
        return result
    def add(self,score):
        self.grade.append(score)
    def fcount(self):
        ct = 0
        for i in range (len(self.grade)):
            if self.grade[i] < 60:
                ct += 1
        return ct
    def show(self):
        #print("Data")
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Grades:",self.grade)
        print("Avg:",self.avg())
        print("Fail Number:", self.fcount())




s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
student_list=[s1,s2,s3,s4,s5]
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

for i in range(5):
    
    student_list[i].show()
    print('')

print('Top Student:')
Top(student_list)
print('')

