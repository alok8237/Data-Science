'''
#Decorator
class Demo:
    @property
    def show(self):
        print(f"Hello how are you")
obj=Demo()
obj.show       

#====================================================
def decorate(func):
    def wrapper():
        print(f"I will print before the function")
        func()
        print(f"I will print after the function")
    return wrapper
@decorate
def hello():
    print(f"Hello i am Alok")
hello()    

#=======================================================
def decorate(func):
    def wrapper(a,b):
        print(f"Hello how are you")
        func(a,b)
        print(f"Thank you")
    return wrapper
@decorate
def addition(a,b):
    print(f"sum is {a+b}")
addition(34,68)   

#==============================================
#args
#args is used to catch multiple arguments
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    print(f"Sum is {sum}")    
sum(11,1,14,55)   

#===================================================
#kwargs means keyword arguments
def data(**kwargs):
    print(kwargs)
data(a=10,b=20,c=30)  #convert values into keywords and arguments 

#===============================================================
def information(**kwargs):
    print(f"Your information is ")
    for i in kwargs:
       print(f"{i} : {kwargs[i]}")
information(name="Akash",Age=24,Designation="Data Science")       
'''
#===============================================================
#Use of args and kwargs in decorator
def decorate(func):
    def wrapper(*args,**kwargs):
        print(f"Hello how are you")
        func(*args,**kwargs)
        print(f"Thank you")
    return wrapper
@decorate
def addition(a,b):
    print(f"sum is {a+b}")
addition(34,68)  