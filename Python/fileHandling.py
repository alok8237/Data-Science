'''
#File handling
p=open(r"D:\Java\AlokYadav.txt")
print(p.read())

#=============================================
r=open("Anshu.txt","w") #write overwrites or creates a new file
r.write("The monsoon is very good nowadays")
r.close()
'''
#==============================================
r=open("Anshu.txt","a") #append is used to add sentence in last
r.write("and the cold wind is blowing")
r.close()