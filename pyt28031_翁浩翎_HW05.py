Math_pass={'柯南','灰原','步美','美環','光彦'}
Eng_pass={'柯南','灰原','丸尾','野口','步美'}

#math pass but not English
Mp1=Math_pass.union(Eng_pass)
Mp2=list(Mp1.difference(Eng_pass))
Mp2.sort()
print(Mp2)

#English pass but not math
Eg1=Math_pass.union(Eng_pass)
Eg2=list(Eg1.difference(Math_pass))
Eg2.sort()
print(Eg2)

#math and English all pass
EM=list(Math_pass.intersection(Eng_pass))
EM.sort()
print(EM)
