'''
print("We are learning python")
#===================================================
#comment
""""This is a multi-line comment
doc string"""
#===================================================
#Variable
SheryiansSchool="students" #pascal case
sheryiansSchool="students" #camel case
sheryians_school="students" #snake case
#===================================================
#Data types
#1 Number
a = 10
b=2.5
c=12/4
d=2j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#2 String
name="Sheryians"
x='Alok'
print(type(name))
print(type(x))
#3 Boolean
is_student=True
print(type(is_student))
#===================================================
#Conversion of data types
z="A"
print(ord(z))
n=65
print(chr(n))
#====================================================
#String indexing
m="AlokYadav"
#positive indexing
print(m[1])
#negative indexing
print(m[-1])

#String slicing
print(m[1:4])
print(m[1:4:1])
print(m[3::1])
print(m[::2])
print(m[4::])
print(m[::])
#====================================================
#Type conversion
#Explicit conversion
x=10
p=str(x)
print(p)
print(type(p))
y=10.5
print(int(y))
z="10"
q=int(z)
print(q)
print(type(q))
a=10
print(bool(a))
b=0
print(bool(b))
#only seven values are considered false in python

#Implicit conversion
print(12/4) #output comes in float/computer automatically converts int to float
#====================================================
name="Alok"
b=100
print(name,b)
print("My name is",name,"and my age is",b)
print(f"My name is {name} and my age is {b}") #formatted string
#====================================================
#Input function
age=input("Enter your age: ") #Default data type of input is string
print("Your age is",age)
num=int(input("Enter a number: "))#convert string to int
print("Your number is",num)
#===================================================================
#Operators
#1 Arithmetic operators
a=5
b=20
print(a+b)
print(a-b)      
print(a*b)
print(a/b)
print(a//b) #floor division
print(a%b)  #modulus
print(a**b) #exponential
print(a+b/2) #operator precedence(BODMAS)
#2.Assignment operators
c=20
print(c)
#compound assignment operators
c+=20
c+=40
print(c)
c-=10
c*=2
c/=5
print(c)
#3.Comparison operators
x=10
y=20
print(x==y)
print(x!=y) 
print(x>y)
print(x<y)  
print(x>=y)
print(x<=y)
print(ord("A"))
print(ord("B"))
print("A">"B")
print("ABC">"ACD")
print("A">20) #comparison not possible between instances of 'str' and 'int'
#4.Logical operators (and, or, not)
print(24>23 and 23>22 and 22>21)
print(19>23 or 20>22 or 22>21)
print(not(20>22))
#===========================================================================
#If else statement
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")   

#if elif else statement
marks=int(input("Enter your marks: "))
if marks>=90:
    print("A grade")     
elif marks>=80:
    print("B grade")
else:
    print("C grade")

#Question 1
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))   
if a>b:
    print("Greatest number: ",a) 
else:
    print("Greatest number: ",b)  

#Question 2
a=input("Enter gender char: ")
if a=="M" or a=='m':
    print("Hello sir")
elif a=="F" or a=="f:
print("Hello mam)   
else:
    print("unidentified gender")   
        
#Question 3
x=int(input("Enter the number: "))  
if x%2==0:
    print(f"{x} is even")  
else:
    print(f"{x} is odd")    
 
#==========================================================
#Loops
#1. For loop
for i in range(1,11,1):
    print("Alok Yadav")

for j in range(5):
    print(j)    

n=int(input("Enter a number: "))
for k in range(n,(n*10)+1,n):
    print(k)    

#Loops in string
a="Good morning"
for i in range(len(a)):
    print(a[i])  

b="hello world"
for j in b:
    print(j)   

#==========================================================    
#Break,continue and else statement
for k in range(15):
    if k==12:
        break
    print(k)       

for l in range(15):
    if l==12:
        continue
    print(l)     

for i in range(5):
    if i==7:
       print("Break statement is executed")
       break
    print(i)    
else:
    print("Break statement is not executed")          
  
#Question 1:Reverse for loop.print n to 1
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    print(i)

#Question 2:Print sum of even and odd numbers in a range
n=int(input("Enter a number: "))
s=0
m=0
for i in range(0,n+1,1):
    if i%2==0:
        s+=i
    else:
        m+=i
print(f"Sum of even numbers is {s} and sum of odd numbers is {m}")   

#Question 3:Print all facors of a number
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i) 

#Question 4:Check whether a  umber is perfect or not
n=int(input("Enter a number: "))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i 
if s==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")   

#Question 5:Reverse a string
a=input("Enter the string: ")
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")  

#Question 6:Check pallindrome
b=input("Enter the string: ")
n=len(b)
for i in range(n//2):
    if b[i]!=b[n-i-1]:
        print(f"{b} is not a pallindrome")
        break
else:
    print(f"{b} is a pallindrome")

#Question 7:count all letters,digits and symbols from a given string  
#we can also use isdigit() and isalpha() function to check digit and alphabet
n=input("Enter the string: ")
c=0
d=0
s=0
for j in range(len(n)):
    if n[j]>='A' and n[j]<='Z' or n[j]>='a' and n[j]<='z':
        c+=1
    elif n[j]>='0' and  n[j]<='9':
        d+=1
    else:
        s+=1
print(f"Number of letters is {c} ,Numbers of digits is {d} and Numbers of symbols is {s}")       

#======================================================================================
#While loop
a=1
while a<=30:
    print(a)
    a+=1

#Question 1:seperate each digit of a number
n=int(input("Enter a number: ")) 
while n>0:
    a=n%10
    n//=10
    print(a)   

#Question 2:reverse the number
n=int(input("Enter a number: ")) 
while n>0:
    a=n%10
    n//=10
    print(a,end="")       

#Question 3:pallindrome number
n=int(input("Enter a number: ")) 
copy=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
if copy==rev:
    print("number is pallindrome")
else:
    print("number is not pallindrome")            

#==============================================================
#Question 4.Make a game of guessing random number between 1 to 50
import random
n=random.randint(1,50)
tries=0
while True:
    guess=int(input("Enter the number: "))
    if guess==n:
        tries+=1
        print(f"You guessed the right number and number of tries is {tries}")
        break
    elif guess<n:
        tries+=1
        print("Take a little higher number")   
    elif guess>n:
        tries+=1
        print("Take a little lower number") 
    else:
        print("Sorry you are wrong")    

#========================================================
#use of module
import mathsModule
print(mathsModule.addition(20,34))
'''
#============================================================
#use of packages
from Packages.package import subDivide
print(subDivide.divide(24,12))

from Packages import maths
print(maths.addition(24,12))


    