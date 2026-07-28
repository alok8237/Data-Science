'''
#Dunder methods
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Hello how are you and lion's age is {self.age}"
a=Animal("Lion",12)
print(a)            

#==============================================================
#Addition using dunder
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Hello how are you and lion's age is {self.age}"
    def __add__(self, other):
        return f"Sum of ages of both animals are {self.age+other.age}"
a=Animal("Lion",12)
b=Animal("Tiger",15)
print(a+b) 

#===================================================
#three number addition
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Hello how are you and lion's age is {self.age}"
    def __add__(self, other):
        sum=0
        for i in other:
            sum+=i.age
        return f"Sum of ages of three animals are {self.age+sum}"
a=Animal("Lion",12)
b=Animal("Tiger",15)
c=Animal("Elephant",10)
print(a+(b,c)) 
'''
#=========================================================