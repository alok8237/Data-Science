'''
a=10
b=20
print(a+b)  #imperative approach
#=======================================
def add(a,b):
    print(a+b)
add(20,30)   #functional approach 
#========================================

#Object oriented programming
class Factory:
    a=10 #attribute
    def hello(self):
        print(f"Hello i am alok")
    print(f"hello how are you")    
print(Factory().a)
Factory().hello()    

#=========================================
#Object creation
class Factory:
    a=10 #attribute
    def hello(self):
        print(f"Hello i am alok")   
obj=Factory() #object creation
print(obj.a)
obj.hello()  

#============================================
#Constructor
class Factory:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets
reebok=Factory("Leather",3,2)
Campus=Factory("Nylon",5,3)   
print(reebok.pockets)
print(Campus.zips)   #self stores address of reebok and Campus

#=======================================================
class Factory:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets
    def show(self):
        print(f"Your details are: {self.material},{self.zips},{self.pockets}")    
reebok=Factory("Leather",3,2)
Campus=Factory("Nylon",5,3)   
reebok.show()

#============================================
#types of attributes and methods
class Animal:
    a="Alok"  #class attributes
    def __init__(self,age): 
        self.age=age #instance attribute
    def show(self):  #instance method
        print(f"Your age is {self.age}")    
    @classmethod
    def hello(cls):  #cls tracks location of Animal(class)
        print(f"How are you?")    
    @staticmethod
    def static():
        print(f"Hello world") 
obj=Animal(50)
obj.show()
obj.hello()
obj.static()     

#===================================================
#Inheritance
class Factorymumbai: #Super class/parent class
    a="attribute mentioned inside factory"
    def hello(self):
        print(f"method mentioned inside factory")
class Factorypune(Factorymumbai): #subclass/child class
    pass
#obj=Factorymumbai()
obj2=Factorypune()
obj2.hello()

#=============================================================
#Inheritance using constructor
class Animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Hello your name is {self.name}")  
class Lion(Animal):
    pass
l=Lion("Akash")  
A=Animal("Aman") 
l.show()     
A.show()

#======================================================
#Single inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Hello your name is {self.name}")  
class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(f"Hello your name is {self.name} and age is {self.age}")  
h=Human("Alok",24)
h.show()
A=Animal("Anshu")
A.show()

#==========================================================
#Multiple inheritance
class Animal:
    name1="Aman"
class Human:
    name2="Rohan"
class Robots(Animal,Human):
    name3="Alok"
r=Robots()
print(r.name2)  

#=========================================================
#Multiple inheritance
class Animal:
    def __init__(self,name):
        pass
class Human:
    def __init__(self,name,age):
        pass
class Robots(Human,Animal): #if human is written first means human constructor is targeted
    name3="Alok"
r=Robots()

#=======================================================
#Multi level inheritance
class Factory:
    def __init__(self,name,material):
        self.name=name
        self.material=material
class Bhopalfactory(Factory):
    def __init__(self,name,material,zips):
        super().__init__(name,material)
        self.zips=zips
class Punefactory(Bhopalfactory):
    def __init__(self,name,material,zips,pockets):
        super().__init__(name,material,zips)
        self.pockets=pockets   
p=Punefactory("Adidas","Leather",4,5)
print(p.name,p.material,p.zips,p.pockets)   

#============================================================
#Polymorphism
#Method overriding
class Animal:
    def show(self):
        print("Tiger is national animal")
class Human:
    def show(self):
        print("Human is immortal")
obj=Human()
obj.show()

#===============================================
#Method overloading does not exist in python
class Animal:
    def show(self):
        print("Tiger is national animal")
    def show(self,name):
        pass    #method overloading
class Human:
    def show(self):
        print("Human is immortal")
obj=Human()
obj.show()  

#====================================================
#Duck typing
class Animal:
    def show(self):
        print("this is lion")
class Human:
    def show(self):
        print("this is human")        
obj=Animal()
obj2=Human()
obj.show()
obj2.show()        

#=========================================================
#Encapsulation
class Animal:
    _a="Tiger" #protected attribute
    def _hello(self):  #protected method
        print("Hello world")
class Human(Animal):
    def show(self):
        print(super()._a)            
obj=Human()
obj.show()  #but there is no difference between public and protected in python

#=======================================================
class Animal:
    __a="Tiger" #private attribute
    def __hello(self):  #private method
        print("Hello world")
class Human(Animal):
    def show(self):
        print(super().__a)            
obj=Human()
obj.show()        

#==================================================
class Animal:
    __a="Tiger" #private attribute
    def hello(self):  #private method
        print(Animal.__a)
a=Animal()
a.hello()  

#======================================================
class Animal:
    __a="Tiger" #private attribute
    def hello(self):  #private method
        print("Hello world")
A=Animal()
print(A.__a)        

#========================================================
class Demo:
    def __init__(self):
        self.name="Alok"
        self._age=24
        self.__salary=50000
    def show(self):
        print("Inside the class")
        print(f"Public: {self.name}")
        print(f"Protected: {self._age}")
        print(f"Private: {self.__salary}")  
d=Demo()
d.show()          
'''
#=====================================================
#Abstraction
from abc import ABC,abstractmethod
class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Square(abstract):
    def __init__(self,side):
        self.side=side 
    def perimeter(self):
        return 4*self.side
    def area(self):
        return self.side**2     
class Circle(abstract):
    def __init__(self,radius):
        self.radius=radius 
    def perimeter(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius*self.radius              
s=Square(5)
c=Circle(4)
print(f"Area of square is {s.area()} and perimeter is {s.perimeter()}")    
print(f"Area of circle is {c.area()} and perimeter is {c.perimeter()}") 