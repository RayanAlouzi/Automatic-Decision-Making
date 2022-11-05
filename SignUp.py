from getpass import getpass
import pwinput
import sqlite3

conn = sqlite3.connect("./mainDatabase.db")
def signup(conn):
    uid = None
    password = None
    confirmPassword = 0
    while uid == None: 
        uid = input("Input your username: ")
        if len(uid) > 10:
            print("Username is too long")
            uid = None
        elif  len(uid) == 0:
            uid = None
    while(password != confirmPassword):  # creates valid password
        password = pwinput.pwinput(prompt ="Enter your password: ", mask="*")
        confirmPassword = pwinput.pwinput(prompt ="Confirm your password: ", mask="*")
        if password != confirmPassword:
            print("Passwords do not match, try again.")

    print("Your password is:", password)    

signup(conn)