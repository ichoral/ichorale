
import re
print("WELCOME TO BRIGHTON UNIVERSITY, LOGIN WITH YOUR DETAILS")
userName=input()
password=input()
while len(userName)==0 or len(password)==0:
    print("Error: Please ensure both Username and Password string are being entered")
    userName=input()
    password=input()
while len(userName)<12 or len(password)<12:
    print("Username or Password is incorrect: please re-login")
    userName=input()
    password=input()
if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password):
    print("Password is strong")
else:
    print("Username must contain uppercase, lowercase and digit")
    password=input()
password2=input("confirm password:  ")
while password2!=password:
    print("input type error!")
    password2=input("confirm password:  ")
print("CONGRATULATIONS! YOU CAN ACCESS BRIGHTON MATERIALS")
    
        