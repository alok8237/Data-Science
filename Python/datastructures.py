'''
#List
l=[1,2,3,4,5,"Alok",9.8]
print(l)
l.append(45) #insert in last
print(l)
l.remove(3)
print(l)
l.insert(2,3)
print(l)
l.pop() #delete from last
print(l)
l[0]=33
print(l)
#============================================
l1=[5,4,32,1,12]
for j in range(0,len(l1)):
    print(l1[j])
for k in l1:
    print(k)    

#============================================    
#Question 1:find negative and positive element in list
l=[1,2,3,4,-7,-8,45,-22,-90]
p=[]
n=[]
for i in range(0,len(l)):
    if l[i]>=0:
        p.append(l[i])
    else:
        n.append(l[i])
print(f"List of posive numbers is {p}")
print(f"List of negative numbers is {n}") 

#Question 2:mean of list
l=[1,2,3,4,5]
s=0
n=len(l)
for i in range(0,n):
    s+=l[i]
print(f"Mean of list is {s/n}")  

#Question 3:greatest elt and its index
l=[23,34,12,67,45,32]
n=len(l)
ind=0
max=float('-inf') #defining minus infinity
for i in range(0,n):
    if max<l[i]:
        max=l[i]
        idx=i
print(f"Max element is {max} and its index is {idx}")        

#Question 4:Check list is sorted or not
l=[1,54,11,23,44,34]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("list is not sorted")
        break
else:        
    print("List is sorted")    

#Question 5:second largest element
l=[12,23,1,2,56,43]
lar=l[0]
sec=l[0]
for i in range(len(l)):
    if lar<l[i]:
        sec=lar
        lar=l[i]
    elif sec<l[i]:
        sec=l[i] 
print(f"Second largest element is {sec}")            

#============================================== 
#Tuple
t=(1,2,3,4,4,5,5,6,7)
for i in range(len(t)):
    print(t[i],end=" ")
print()
print(t.count(4))
print(t.index(6))

#tuple unpacking
a,b,c,d=(1,2,3,4)
print(a)
print(b)
print(type(a))

#====================================================
#set (duplicates not allowed)
s={1,2,3,4,5} #unordered(cannot access by index) and immutable
print(s)
s1=hash((1,2,3,4,5))
print(s1)
print(s1)
s2={11,11,2,3,4,5,5}
print(s2)

#set traversing
s={1,2,3,"hello",8,9,4,5}
for a in s: #no other traversing work
    print(a)

#set methods
s={1,2,3,4,5,6}
s.remove(5) #occurs error if not found
print(s)    
s.add(5)
print(s)
s.discard(2) #no error if not found
print(s)
s.clear()
print(s)

#set operations
a={1,2,3,4}
b={3,4,5,6}
union=a|b
intersection=a&b
difference=a-b
symmetric_diff=a^b
print(f"Union:{union} Intersetion: {intersection} Difference: {difference} Symmetric difference: {symmetric_diff}")
#compund operation
b-=a
print(b)

#=========================================================================
#Dictionary
d={1:100,2:200,3:300,4:400}
print(d)
print(d[1])
d[1]=1000
print(d)
#in dictionary keys are unique and immutable but value are immutable

#dictionary create delete update operation
d1={1:10,2:20,3:30,4:40,5:50}
d1[6]=60 #create
print(d1)
d1[2]=200 #update
print(d1)
del d1[3] #delete
print(d1)
print(d1.clear()) #clear

#dictionary traversing
d={1:10,2:20,3:30,4:40,5:50}
for i in d:
    print(f"Key: {i} and Value: {d[i]}")
for j in d.values():
    print(j)     

d1={1:10,1:20} #print key's updated value
print(d1)

#dictionary deep copy
d={1:10,2:20,3:30,4:40,5:50}
print(d)
d1=d
d1[1]=100
print(d)

#dictionary shallow copy
d={1:10,2:20,3:30,4:40,5:50}
print(d)
d1=d.copy()
d1[1]=100
print(d)
print(d1)

#Question 1:merge two dictionaries
d1={1:10,2:20,3:30}
d2={3:40,4:50,5:50}
for i in d2:
    d1[i]=d2[i]
print(f"After merge: {d1}")    

#Question 2:sum keys and values of dictionary
d1={1:10,2:20,3:30}
s1=0
s2=0
for i in d1:
    s1+=i
    s2+=d1[i]
print(f"Sum of keys: {s1} and Sum of values: {s2}")

#Question 3:count frequency of each element in dictionary
l=[1,1,1,2,2,3,3,4,5,5,6,7]
d={} #empty dictionary
for a in l:
    if a in d.keys():
        d[a]+=1
    else: 
        d[a]=1
print(d)   
'''
#Question 4:write a python program to combine two dictionary by adding values for common keys
d1={1:10,2:20,3:30}
d2={3:40,4:50,5:50}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]    
print(d1)        
