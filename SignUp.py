from getpass import getpass
import pwinput
import sqlite3

conn = sqlite3.connect("./mainData.db")
def signup(conn):
    c = conn.cursor()  # create cursor to connect to database
    uid,password, confirmPassword, name, age = "","","","",""  # initiate all the variables


    while uid == "" or password != confirmPassword or password == "": 
        uid = input("Input your username: ")
        while uid == "":
            uid = input("Input your username: ")
        # to check if uid in database
        c.execute('''
            SELECT u.uid
            FROM users u 
            WHERE lower(u.uid) = ?;'''
            ,(uid,))
        row = c.fetchone()

        # creates valid password
        password = pwinput.pwinput(prompt ="Enter your password: ", mask="*")
        while password == "": 
            password = input("Enter your password: ")
        confirmPassword = pwinput.pwinput(prompt ="Confirm your password: ", mask="*")

        name = input("Input your name: ")
        while(name == ""):
            try: 
                name = int(name)
                name = ""
                print("Username cannot be just numbers")
            except Exception as e: 
                print(e)
                # valid username
                

        # checks whatever can make it invalid
        if len(uid) > 15:  # username is too long
            print("Username is too long")
            uid = ""
        if len(uid) < 4:  # username is too short
            print("Username is too short")
            uid = ""
        elif row != None:  # username exists in database
            print("Username is not unique, try again")
            uid = ""
        elif len(password) < 5:  # password too short
            print("Password is too short, try again")
        elif password != confirmPassword:  # password and confirmPass don't match
            print("Passwords do not match, try again.")
        elif uid.lower() in password.lower():  # username inside password
            print("Weak password, try again")
            password,uid,confirmPassword = "", "",""

    c.execute('''INSERT INTO users VALUES (?,?,?,?)''')

signup(conn)