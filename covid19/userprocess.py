
import randam

def user():
    print("enter 1 or 2 or 3 \n 1->booking the appointment \n 2->update the details \n 3->view the detail")
    user_option=int(input("enter your option:"))
    if user_option==1:
        print("please fill below for appointment....")
        phone_no=int(input("enter your phone number:"))
        name=input("enter your name:")
        address=input("enter your address:")
        confirm=input(f"name:{name} and phone number:{phone_no} and address:{address},correct or not:")
        if confirm=="correct":
            print("your appointment is recieved")
        else:
            print("thanks for visiting")
    elif user_option==2:
        phone_no=int(input("enter your updated phone number:"))
        name=input("enter your updated name:")
        address=input("enter your updated address:")
        print(f"updated dtails:- name:{name} and phone number:{phone_no} and address:{address}")
        print("your details updated successfully...")
    elif user_option==3:
        name="priya"
        phone_no=123456789
        address="chennai"
        print(f"name:{name} and phone number:{phone_no} and address:{address}")
user()

    














        