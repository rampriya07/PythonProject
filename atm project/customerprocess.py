import time as t

#customer actually need to leave the site
def logout_and_exit():

    print("exiting....\n you have been logged out.\n Thank you for visiting our page")
    

#customer wants to view the balance amount
def view_account_balance():
    Pin_number=int(input("Please enter your 4-digit PIN:"))
    balance=20000
    if(Pin_number==1234):
        print("Account Authorized!")
        print(f"your current balance is:{balance}")
    else:
        print("enter the correct pin number")


#customer wants to withdraw cash
def withdraw():
    cash=int(input(f"enter the amount you wish to withdraw:"))
    balance=20000
    withdraw=balance-cash
    print(f"withdrawing Rs.{cash}")
    confirm=input(f"confirm? Yes/No:")
    if(confirm=="yes"):
        if(cash<20000):
            print(f"amount deposited->Rs.{cash}\n thankyou for visiting")
            print(f"your  updated balance amount is:{withdraw}")
        elif(cash>20000):
            print(f"your total amount is {balance}.rs so take less amount") 

    elif(confirm=="no"):
        print(f"withdraw cancelled...\n thankyou for visiting")

#deposit the cash
def deposit():
    deposit_amount=int(input("enter the amount you want to deposit:"))
    balance=20000
    total_amount=balance+deposit_amount
    print(f"{deposit_amount}.Rs  is credited to your account")
    print(f"your updated balance is{total_amount}")

#changing pin number
def pin_change():
    pin_number=int(input("please enter your pin number:"))
    if(pin_number==1234):
        print(f"Account Authorized...")
        new_pin_number=int(input("enter your new pin number:"))
        print(f"changing pin to {new_pin_number}")
        confirm=input(f"confirm? Yes/No:")
        if(confirm=="yes"):
            print("Pin changed successfully!")
        else:
            print("cancelling pin change...\n process cancelled!")

#returning a ATM card
def return_card():
    print("loading card return...\n card returned successfully!")

