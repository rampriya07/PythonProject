import customerprocess

def transaction():
    print("*********Welcome to the ABC bank*********")

#customer account details
    name=input("enter your name:")
    user_name="kumar"

    account_number=int(input("enter your account number:"))
    user_account=123456789

    user_pin=1234

    if(name==user_name and account_number==user_account):
        print(f"===============Welcome to our bank acccount Ms./Mr.{name}==============")
        pin_number=int(input("insert your card and enter the 4 digit pin:"))
        if(pin_number==user_pin):
            #customer want to choose the process
            print("0-> for logout and exit the page \n 1-> for view the balance. \n 2-> for withdraw process. \n 3-> for changing pin number process.\n 4->for returning card. \n 5-> depositing purpose")
        process_number=int(input("enter the process number:"))
    
    #calling the  process 
        if(process_number==0):
            customerprocess.logout_and_exit()

        elif(process_number==1):
            customerprocess.view_account_balance()

        elif(process_number==2):
            customerprocess.withdraw()

        elif(process_number==3):
            customerprocess.pin_change()

        elif(process_number==4):
            customerprocess.return_card()

        elif(process_number==5):
            customerprocess.deposit()

        else:
            print("enter the valid number 0 to 5")


    else:
        print(f"{account_number} is not correct")

transaction()

   


    

