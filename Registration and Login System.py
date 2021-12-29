import pandas as pd
from openpyxl import load_workbook
import re

#Creating an excel file
df = pd.DataFrame(columns = ["username","password"])
writer = pd.ExcelWriter(r"D:\credentials.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1", index=False)
writer.save()

#Validating the Username   
def username_validation():
    print("Please enter your email id or username: \n")
    print("Please note that your email id is your username\n")
    username_validation.u = input()
    
    reg = re.compile(r'(\b[A-Za-z]{3,})([A-Za-z0-9._])*[A-Za-z0-9]+@[a-z-]{2,15}(\.[a-z]{2,})')
    
    if re.fullmatch(reg, username_validation.u):
        data1 = pd.read_excel(r"D:\credentials.xlsx")
        df2 = pd.DataFrame(data1)
        c = df2.loc[df2["username"] == username_validation.u]
        #Checking if the Username already exists
        if c.empty:
            print("Username accepted!\n")
            return username_validation.u
        else:
            print("Username taken. Please select a different Username\n")
            username_validation()
    else:
        print("Please provide a proper username\n")
        username_validation()

#Validating the password       
def Password_validation():
    Password_validation.p1 = input("Please enter a new password: \n")
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&_])[A-Za-z\d@$!#%*?&_]{5,16}')
    if re.fullmatch(regex, Password_validation.p1):
        print("Password accepted!")
        return Password_validation.p1
    else:
        print("Please provide a proper password.\n")
        print('''Make sure that your password has 5 to 16 characters and minimum one special character,
one lowercase,one uppercase and one digit \n''')
        Password_validation()

#Registration/Sigh Up
def Register(x,y):

    df1 = pd.DataFrame(data = [{"username" : x, "password" : y}], columns = ["username","password"])

    writer = pd.ExcelWriter(r"D:\credentials.xlsx", engine="openpyxl")
    writer.book = load_workbook(r"D:\credentials.xlsx")
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(r"D:\credentials.xlsx")
    df1.to_excel(writer,index=False,header=False,startrow=len(reader)+1)
    writer.save()
    writer.close()
    
    print("Registration successful\n")
        
#Login/Sign In      
def Login():
    user = input("Please enter your username: \n")
    pw = input("Please enter the password: \n")
    
    data = pd.read_excel (r"D:\credentials.xlsx") 
    df = pd.DataFrame(data)
	#Checking if the Username and password exists
    s = df.loc[(df["username"] == user) & (df["password"] == pw)]
    if s.empty:
		#Checking if the Username exists
        s1 = df.loc[(df["username"] == user) & (df["password"] != pw)]
        if s1.empty:
            print("Your account does not exist. Please Register\n")
            username_validation()
            Password_validation()
            Register(username_validation.u, Password_validation.p1)
        else:
            print("You have entered the wrong password.\n")
            print("Type 1 if you have forgotten your password and wish to retrive your password.\n")
            print("Type 2 if you wish to reset your password.\n")
            print("Type 3 if you wish to sign in again.\n")
            typ = int(input())
            l = s1.loc[:,"password"]
            if typ == 1:
                print("Your password is retreived. Your password is ",l.iloc[0])
                print("\n")
            elif typ == 2:
                Password_validation()
                df["password"] = df["password"].replace([l.iloc[0]],Password_validation.p1)
                writer = pd.ExcelWriter(r"D:\credentials.xlsx", engine="openpyxl")
                df.to_excel(writer, sheet_name="Sheet1", index=False)
                writer.save()
                writer.close()
            elif typ == 3:
                Login()
    else:
        print("Login Successful\n")
    
#Main    
a = 1
while(a):
    user_input = input("Are you a new user.[y/n]")
    if user_input == ("y" or "Y"):
        username_validation()
        Password_validation()
        Register(username_validation.u, Password_validation.p1)
    elif user_input == ("n" or "N"):
        Login()
    else:
        print("Please enter a valid option\n")