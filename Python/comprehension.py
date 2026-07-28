'''
#Question 1:make a list of even number from 1 to 20
l=[]
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l)   

#Question 1 using list comprehension
l=[i for i in range(1,21) if i%2==0]
print(l)
'''
#=====================================================
#Dictionary comprehension
d={i:i**2 for i in range(1,10)}
print(d)
