import random
import pandas as pd


print("*****************WELCOME TO OUR RPN HOSPITAL*******************")

data=pd.read_csv("covid-19")
data=pd.dataframe(data)

#admin login
your_name=input("enter your name:")
your_password=int(input("enter your password:"))

username="priya"
user_password=1234

if username==your_name and user_password==your_password:
    print(f"WELCOME {your_name.upper()}")
    process=int(input("enter 1 for user process OR enter 2 for admin process:"))

    import userprocess
    import adminprocess

    if process==1:
        userprocess.user()
    elif process==2:
        adminprocess.admin() 
    else:
        print("please enter 1 or 2")

        
else:
    print("enter the correct name and password")

