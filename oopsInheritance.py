'''
class Student:
    def personalDetails(self):
        print("Name : Mounika")
        print("Phone : 9384542020")
    def courseDetails(self):
        print("Course : Python")
        print("Duration : 60hrs")
        
s = Student()
s.personalDetails()
s.courseDetails()

class Calculator:
    def addition(self,a,b):
        print(a+b)
    def subtraction(self,a,b):
        print(a-b)
    def multiplication(self,a,b):
        print(a*b)
    def division(self,a,b):
        print(a/b)

c = Calculator()
c.addition(10,20)
c.subtraction(20,10)
c.multiplication(2,6)
c.division(10,2)


c = Calculator()

ch = input("Enter the operation (+ , - , * , /) :")

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))

if ch=="+":
    c.addition(a,b)
elif ch=="-":
    c.subtraction(a,b)
elif ch=="*":
    c.multiplication(a,b)
elif ch=="/":
    c.division(a,b)
else:
    print("Invalid choice")

'''

#single inheritance
'''
class parent:
    def pbeh(self):
        print("multi-tasking")

class child(parent):
    def childbeh(self):
        print("scrolling")
       
p = parent()
p.pbeh()

c = child()
c.childbeh()
c.pbeh()
'''

#multiple inheritance
'''
class father:
    def fs(self):
        print("Driving")
class mother:
    def ms(self):
        print("Drawing")
class child(father,mother):
    def cs(self):
        print("Nothing")

c = child()
c.fs()
c.ms()
c.cs()
'''

#single inheritance

'''
class warehouse:
    def wp(self):
        wp = ["1.Laptop","2.Mobile","3.Pen","4.Mouse","5.Earbuds"]
        for i in wp:
            print(i)
class franchise(warehouse):
    def fp(self):
        fp = ["1.Jewels","2.Dress","3.Accessories"]
        for i in fp:
            print(i)
        
f = franchise()
f.wp()
f.fp()
'''
'''
#multiple inheritance

class resume1:
    def temp1(self):
        print("Name \nObjective \nSkills")

class resume2:
    def temp2(self):
        print("Education \nProjects \nInternship")

class resume3:
    def temp3(self):
        print("Extra curricular Activites \nCertifications")

class finalresume(resume1,resume2,resume3):
    def temp4(self):
        pass

f = finalresume()
f.temp1()
f.temp2()
f.temp3()

'''

#multi-level inheritance

'''
class briyani:
    def ing(self):
        print("common ingridients")

class vegbriyani(briyani):
    def ving(self):
        print("vegetables")

class additional(vegbriyani):
    def adding(self):
        print("curd / lemon")

b = briyani()
b.ing()

print()

v = vegbriyani()
v.ing()
v.ving()

print()

a = additional()
a.ing()
a.ving()
a.adding()
'''
