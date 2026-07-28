from pathlib import Path
import os
def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")
def createfile():
    try: 
        readfileandfolder()
        name=input("Enter the file name: ")
        p=Path(name)
        if not p.exists() and p.is_file():
           with open(p,"w") as fs:
               data=input("What do you want to write in file: ")
               fs.write(data)
           print(f"File created successfully")    
        else:
            print(f"File already exist")   
    except Exception as err:
        print(f"An error occurred as {err}")    
def readfile():
    try:
        readfileandfolder()
        name=input("Which file do you want to read: ")
        p=Path(name)
        if p.exists() and p.is_file():
           with open(p,'r') as fs:
              data=fs.read()
              print(data)
           print(f"Data readed successfully")   
        else:
            print(f"File does not exist")   
    except Exception as err:
        print(f"An error occurred as {err}")    
def updatefile():
    try:
        name=input("Enter the file name you want to update: ")
        p=Path(name)
        print(f"press 1 for changing the name of your file: ")
        print(f"press 2 for overriting the data in the file: ")
        print(f"press 3 for appending some content in the file: ")
        res=int(input("Enter the choice: "))
        if res==1:
           name2=input("Enter the new name of the file: ")
           p2=Path(name2)
           p.rename(p2)
        if res==2:
           with open(p,'w') as fs:
              data=input("tell us what you want to overwrite in the file: ")
              fs.write(data)
        if res==3:
           with open(p,'a') as fs:
              data=input("tell us what you want to overwrite in the file: ")
              fs.write(" "+data)
    except Exception as err:
        print(f"An error occurred as {err}")          
def deletefile():
    try:
       name=input("Enter the name of file you wnat to delete: ")
       p=Path(name)
       if p.exists() and p.is_file():
          os.remove(p)
          print(f"File removed successfully")
       else:
          print(f"No such file exist")    
    except Exception as err:
        print(f"An error occurred as {err}")                    
print("Press 1 for crerating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")
check=int(input("Enter the choice: "))
if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatefile()
if check==4:
    deletefile()        
