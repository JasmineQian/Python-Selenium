def MaxNum(a,b):
    if a>b: return print(a)
    elif a<b:print(b)
    else: print("a is equal to b.")


def AAA(a,b):
    if a>b: return a
    else: return b

def BBB(a,b,c):
    if (AAA(a,b)>c):print(MaxNum(a,b))
    else:print(c)

###两个数的比较
MaxNum(11,12)
###三个数的比较
BBB(11,12,14)


text ='ice'+'cream'
print(text)

text ='---ice cream----   ' *3
print(text)



class CCC:
    name= "alibaba"
    department="test"
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def displayStudent(self):
        print("姓名  ",self.name, "  ,department is : "+self.department)
y=CCC("0000","1110")
y.displayStudent()