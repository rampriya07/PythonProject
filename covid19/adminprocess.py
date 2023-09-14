import random
import pandas as pd
import smtplib

data=pd.read_csv("covid-19")
df=pd.DataFrame(data)
print(df)

def admin():
    print("***********registration page**********")
    name=input("enter the name:")
    current_address=input("enter the address:")
    gender=input("enter your gender:")
    email=input("enter your mail id:")
    age=int(input("enter your age:"))
    print(f"admin details:\n name:{name} \n address:{current_address} \n gender:{gender}\n mailid:{email}")

    #sending mail
    print(f"{email}")
    for i in df[email]:
        print(i)
        s=smtplib.SMTP("smtp.gmail.com",123)
        s.starttls()

        #message
        message="your registration is done successfully!"
        s.sendmail(f"email:{email},{message}")
        #terminate
        s.quit()

admin()    
