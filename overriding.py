class database():
    def connect(self):
        print("connect data")
class mysql(database):
    def connect(self):
        print("connect mysql")
obj=mysql()
obj.connect()

class software():
    def testing(self):
        print("softwer testing")
class automation_testing(software):
    def testing(self):
        print("automation testing")
k=automation_testing()
k.testing() 
q=software()
q.testing()       


class teacher():
    def teach(self):
        print("teacher")
class math(teacher):
    def teach(self):
        print("teaching math") 
class english(teacher):
    def teach(self):
        print("teaching english")        
obj1=math()
obj1.teach()
obj=english()
obj.teach()             

class restorent():
    def food(self):
      print("provide normal food")
class pizza(restorent):
    def food(self):
        print("provide pizza")
o=pizza()
k=restorent()
o.food()
k.food()

class manager():
    def salary(self):
        print("manager")
class employee(manager):
    def salary(self):
        print("employee")
caul=employee()
caul.salary()

class frontend():
    def developer(self):
        print("frontend develpoer")
class backend (frontend):
    def developer(self):
        print("backend developer")
obj=backend()
obj.developer()

class html():
    def coding(self):
        print("write html code")
class python(html):
    def coding(self):
        print("write python code")
obj1=python()
obj1.coding()     


class college():
    def deparment(self):
        print("college name")
class mgm(college):
    def deparment(self):
        return super().deparment()
print("deparment name")
obj=mgm()
obj.deparment()

class bank():
    def interest(self):
        print("bank name")
class hdfc(bank):
    def interest(self):
        print("hdfc bank")
show=hdfc()
show.interest()     


class shooping():
    def payment(self):
        print(" payment done")
class onlineshooping():
    def payment(self):
        print("payment")
shop=onlineshooping()
shop.payment()        


class hospital():
    def treatment(self):
        print("hospital  treatment")
class childhospital():
    def treatment(self): 
        print("child treatment")
h=childhospital()
h.treatment() 


class school():
    def eduction(self):
        print("school")
class onlineschool(school):
    def eduction(self):
        print("onlineschool")
show=onlineschool()
show1=school()
show.eduction()
show1.eduction()                

class pen():
    def write(self):
        print("writing with a pen")
class pencile():
    def write(self):
        print("writing with a pencile")
obj=pencile()
obj.write()

class visualcode():
    def typing_code(self):
        print("typing code on visualcode")
class notepad():
    def typing_code(self):
        print("typing code on notepad")
h=notepad()
h.typing_code()      

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()


class mother():
    def cooking(self):
        print("cooking food")
class daughter(mother):
    def cooking(self):
        print("extra food cooking")
show=daughter()
show.cooking()
show1=mother()
show1.cooking()


class watch():
    def show_time(self):
        print("show time")
class smartwatch(watch):
    def show_time(self):
        print("smart watch show time")
r=smartwatch()
r.show_time()

class gmail():
     def google(self):
         print("google creat gmail ")
class youtube():
    def google(self):
        print("gooogle creat youtube")
obj=youtube()
obj.google()        


