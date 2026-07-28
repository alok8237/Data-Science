'''
#Exception handling
n=int(input("Enter the number: "))
try:
    print(10/n)
except Exception as err :
    print(f"sorry there is an error as {err}")
print("Division has done")       

#=======================================================
n=int(input("Enter the number: "))
try:
    print(10/n)
except Exception as err :
    print(f"sorry there is an error as {err}")
else: #run only when there is no exception
    print("there is no exception")    
print("Division has done")  #always run  

#==========================================================
n=int(input("Enter the number: "))
try:
    print(10/n)
except Exception as err :
    print(f"sorry there is an error as {err}")
else: #run only when there is no exception
    print("there is no exception")    
finally: #always run
    print("i will always run no matter what")    
print("Division has done")  #always run  
'''
#========================================================
age=int(input("Enter the number: "))
try:
    if age<9 or age>18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("welcome to the club")
except Exception as err:
    print(f"an error occurred {err}")
print("club will start soon")            