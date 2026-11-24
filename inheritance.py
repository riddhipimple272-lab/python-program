class parent:
    def parent_massage(self):
        print("massage in parent")
class child(parent):
    def child_massage(self):
        print("massage for child")
a=child()
a.parent_massage()
a.child_massage()

class animal:
    def animal(self):
        print("animal")
class dog(animal):
    def dog(self):
     print("dog is animal")       
b=dog()
b.animal()
b.dog()

class  boy:
    def boy_details(self):
     print("my name is...!")
class  girl(boy):
    def girls_details(self):
      print("my age is..!")

obj=girl()
obj.boy_details()
obj.girls_details()

class math:
   def math(self):
      print("mathsub")
class english(math): 
   def english(self):
      print("englishsub")
sub=english()
sub.math()
sub.english()          

#multilevel
class person:
   def person_details(self):
      print("my name is = shweta")
class Teacher(person):
   def Teacher_details(self):
      print("subject = python")
class student(Teacher):
   def student_details(self):
     print( "rollno = 101")     
s=student()
s.person_details()
s.Teacher_details()
s.student_details()


class book: 
   def book_details(self):
         print("python book")
         print("html book")
class storybook(book):
   def storybook_details(self):
      print("english")
class  textbook(storybook):
    def textbook_details(self):
       print("css")

w=textbook()
w.textbook_details()
w.storybook_details()                    
w.book_details()   

class college:
     def college(self):
          self.name ="mgm college"
class department(college):
     def department(self):
          self.department = "Bsc"
class student(department):
      def student(self):
           self.studentname="siddhi"
           self.rollno=101
      def display(self):
           print("collage name:",self.name)
           print("department:",self.department)
           print("student:",self.studentname)
           print("roll number:",self.rollno)

obj=student()
obj.college()
obj.department()
obj.student()
obj.display() 



class grandfather:
   def grandfather_details(self):
      print("grandfather")
class father(grandfather):
   def father_details(self):
      print("father")
class daughter(father):
    def daughter_details(self):
       print("daughter")    
r=daughter()
r.grandfather_details()
r.father_details()  
r.daughter_details() 


class vechicle:
   def vechicle(self):
      print("vechicle")
class car(vechicle):
   def car(self):
      print("car")
class Electriccar(car):
   def Electriccar(self):
      print("electricar")
k=Electriccar()
k.vechicle()
k.car()
k.Electriccar()      

#Multiple
class mother():
   def mother(self):
      print("mother is great")
class father(mother):
   def father(self):
      print("father is super")
class child(father,mother):
   def child(self):
      print("child") 
get=child()
get.father()
get.mother()
get.child()       


class camera():
   def camera(self):
      print("click photo")
class phone(camera):
   def phone(self):
      print("use phone")
class smartphone(phone,camera):
    def  smartphone(self): 
       print("scrollreels")
yet=smartphone()
yet.phone()
yet.camera()
yet.smartphone()               

class writer:
   def writer(self):
      print("write the leter")
class editor(writer):
   def editor(self):
      print("edit the data")
class auother(editor,writer):
   def author(self):
      print("author")
veg=auother()
veg.writer()
veg.editor()
veg.author()

class laptop():
   def laptop(self):
      print("laptop")
class dell(laptop):
   def dell(self):
      print("dell")   
class hp(dell,laptop):
    def hp(self):
     print("hp")
gm=hp()
gm.laptop()
gm.dell()
gm.hp()     

class  google():
   def google(self):
      print("google")
class  youtube( google):
   def youtube(self):
      print("google create youtube")
class gmail(youtube,google):
   def gmail(self):
      print("google create gmail")
you=gmail()
you.google()
you.youtube()
you.gmail()


 #Hierarchical
class developer():
   def company(self):
      print("company:tcs")
class pythondeveloper(developer):
   def python(self):
      print("python")  
class javadeveloper(developer):
   def java(self):
      print("java")
obj=pythondeveloper()
obj.company()
obj.python()
obj=javadeveloper()
obj.company()
obj.java()

#hybried
class person():
   def display(self):
      print("person details")
class student(person):
   def study(self):
      print("student is studying") 
class teacher(person):
   def teach(self):
      print("teacher is teaching")
class assitstant(student,teacher):
   def   work(self):
         print("assistant is working")
obj=assitstant()
obj.display()
obj.study()
obj.teach ()
obj.work()
        
