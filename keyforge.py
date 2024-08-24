import hashlib
import random


def user():
    print("........")
    print("let's Create Your new account!")
    user_name= input("enter a valid username: ")
    password= input("password: ")
    print("Creating Account....")
    with open('login_key.txt','a') as login:
        login.write(user_name + "|" + password + '\n')
    print(f'{user_name}, your account as been created!')
    print("........")
    with open("loginkey.txt","a") as login:
        login.write(user_name + "|" + password + "/n")
    

def user_login():
    print("........")
    print("login to your exisitng account")
    user_name= input("enter your username: ")
    password= input("Enter login password: ")
    with open("loginkey.txt","r") as login:
        for line in login.readlines():
            if password in line:
                print("loggin in")
            else:
                print("wrong password")


def password_genr():
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case= upper_case.lower()
    digits = "1234567890"
    symbols = ",./;'[]\?><}{|+=_-)(*&^%$#@!)}"
    total = ""
    lower, upper,num,sym = True,True,True,True
    if lower:
        total += lower_case
    if upper:
        total += upper_case
    if num:
        total += digits
    if sym:
        total += symbols
    length = 10
    password = "".join(random.sample(total,length))
    print(f'Generated password : {password}')


def add():
    acc_name = input("Enter the Account name/website : ")
    acc_password = input("Enter the password: ")
    hash_password = hashlib.sha256(input(acc_password).encode()).hexdigest()
    with open("ori_password.txt",'a') as ori:
        ori.write(acc_name+ "|"+ acc_password + "\n")
    with open("hashed_passwords.txt",'a') as output:
        output.write(acc_name + "|"+ hash_password + "\n")

def view():
    with open("hashed_passwords.txt",'r') as output:
        for line in output.readlines():
            print(line.rstrip())


print("........")
print("""Greetings! Welcome to KEYFORGE
Your one stop solution to generate and manage strong, unique passwords effortlessly.
Say goodbye to weak passwords and hello to seamless security!!!""")
next_step= input("Do you want to 'login to your exisitng account' or 'create a new account'? (create/login): ")
if 'create' in next_step:
    user()
elif 'login' in next_step:
    print("........")
    print("login to your exisitng account")
    user_name= input("enter your username: ")
    password= input("Enter login password: ")
    with open("loginkey.txt","r") as login:
        for line in login.readlines():
            if password in line:
                print("loggin in")
            else:
                print("wrong password")
                exit()

print("........")
print("""Welcome to KEYFORGE!!
You can perform the following tasks: 
a. ABOUT keyforge
b. GENERATE new passwords
c. ADD new password
d. VIEW saved passwords""")
print("........")

while True:
    command = input("Type in your command from the above list of tasks: ")
    if command == "about":
        print("""KeyForge is a powerful tool designed to generate and manage strong, unique passwords effortlessly. 
Built with a focus on security and ease of use, KeyForge ensures your digital accounts are protected with robust passwords while simplifying the process of managing them.
Whether you're creating new passwords or securely storing existing ones, KeyForge provides a seamless and secure experience.""")
    if command=="add":
        add()

    elif command=="view":
        view()
        security_check = input("If you want to see decyrpted passwords, login to your account for security purposes (login) : ")
        if security_check == "login":
            user_login()
            print("The decyrpted passwords are shown below : ")
            with open("ori_password.txt",'r') as ori:
                for line in ori.readlines():
                    print(line.rstrip())
        else:
            print("let's go back to the tasks list")


    elif command=="generate":
        password_genr()




