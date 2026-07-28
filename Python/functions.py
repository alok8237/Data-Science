def sum(a,b): #here a and b are parameter
    print(f"Sum is {a+b}")
sum(10,20)   #here a and b are argument and argument is positional argument
#=================================================
def sum(a,b=45): #default argument
    print(f"Sum is {a+b}")
sum(34) 
sum(20,50)   
#===================================================
def info(name,age):
    print(f"Name is {name} and age is {age}")
info("Alok",24) 
info(age=25,name="Mohit")  #keyword argument