import json
import string
import random
from pathlib import Path
class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print(f"No such file found")        
    except Exception as err:
        print(f"An exception occurred as {err}")   
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))   
    @classmethod  
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3) 
        spchar=random.choices('!@#$%^&*',k=1)
        id=alpha+num+spchar 
        random.shuffle(id)
        return "".join(id)      
    def Createaccount(self):
        info={
            "name" : input("tell your name :"),
            "age" : int(input("tell your age: ")),
            "email" : input("tell your email: "),
            "pin" : int(input("tell your 4 digit pin: ")),
            "account" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age']<18 and len(str(info['pin']))!=4:
            print(f"Sorry you cannot create account")
        else:
            print(f"Account has been created successfully")  
        for i in info:
            print(f"{i} : {info[i]}")      
        print(f"Please note down your account")   
        Bank.data.append(info)
        Bank.__update() 

    def depositmoney(self):
        accnum=input("Enter your account number: ")
        pin=int(input("Enter your pin: ")) 
        userdata=[i for i  in Bank.data if i['account']==accnum and i['pin']==pin]
        if userdata==False:
            print(f"Sorry no data found")
        else:
            amount=int(input("How much money you want to deposit: "))
            if amount>10000 or amount<0:
                print(f"Sorry you can deposit money only above 0 or below 10000")
            else:
                print(userdata)
                userdata[0]['balance']+=amount
                Bank.__update()
                print(f"Amont deposited successfully")

    def withdrawmoney(self):
        accnum=input("Enter your account number: ")
        pin=int(input("Enter your pin: ")) 
        userdata=[i for i in Bank.data if i['account']==accnum and i['pin']==pin]
        if userdata==False:
            print(f"Sorry no data found")
        else:
            amount=int(input("How much money you want to wihdraw: "))
            if userdata[0]['balance']<amount:
                print(f"Sorry insufficient balance")
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print(f"Amont wihdrawn successfully")  

    def showdetails(self):
        accnum=input("Enter your account number: ")
        pin=int(input("Enter your pin: ")) 
        userdata=[i for i in Bank.data if i['account']==accnum and i['pin']==pin]
        if userdata==False:
            print(f"Sorry no data found")
        else:
            print(f"Your account information is :")    
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnum=input("Enter your account number: ")
        pin=int(input("Enter your pin: ")) 
        userdata=[i for i in Bank.data if i['account']==accnum and i['pin']==pin]
        if userdata==False:
            print(f"Sorry no data found")
        else:
            print(f"You cannot change your age,account number and balance.")
            print(f"Fill the details for change or press enter for no change.")
            newdata={
                "name":input("Enter your new name or press enter to skip: "),
            "email":input("Enter your new email or press enter to skip: "),
            "pin":input("Enter your new pin or press enter to skip: ")
            }
            if newdata['name']=="":
                newdata['name']=userdata[0]['name']
            if newdata['email']=="":
                newdata['email']=userdata[0]['email']
            if newdata['pin']=="":
                newdata['pin']=userdata[0]['pin']  
            newdata['age']=userdata[0]['age']
            newdata['account']=userdata[0]['account']
            newdata['balance']=userdata[0]['balance']
            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue 
                else:
                    userdata[0][i]=newdata[i]       
            Bank.__update()
            print(f"Bank details updated successfully")
    def delete(self):
        accnum=input("Enter your account number: ")
        pin=int(input("Enter your pin: ")) 
        userdata=[i for i in Bank.data if i['account']==accnum and i['pin']==pin]
        if userdata==False:
            print(f"Sorry no data found")
        else:
            check=input("press y to delete the account or press n: ")
            if check=='n' or check=='N':
                print("Bypassed")    
            else:
                index=Bank.data.index(userdata[0]) 
                Bank.data.pop(index)
                print("Account deleted successfully")   
                Bank.__update()

user=Bank()    
print("press 1 for creating an accout")
print("press 2 for depositing money in the bank")
print("press 3 for withdrawing money")
print("press 4 for showing the bank details")
print("press 5 for updating the bank details")
print("press 6 for deleting the account")
check=int(input("tell your response: "))
if check==1:
    user.Createaccount()
if check==2:
    user.depositmoney()  
if check==3:
    user.withdrawmoney()  
if check==4:
    user.showdetails()        
if check==5:
    user.updatedetails()   
if check==6:
    user.delete()        

