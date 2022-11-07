import sqlite3
import pwinput
conn = sqlite3.connect("./mainData.db")

def login(conn): # returns userID and artistID, at least one is not None
    c = conn.cursor()
    c.execute(' PRAGMA foreign_keys=ON; ')
    conn.commit()
    userID = None
    while userID == None: 
            #take ID and password
            
            ID = input("Enter username or input -1 to go back: ").lower()  # userID
            if ID.strip() == '-1':
                break
            pwd = pwinput.pwinput(prompt ="Enter your password: ", mask="*")
            
            # query all users matching ID and pwd
            c.execute('''
                SELECT u.uid 
                FROM users u
                WHERE lower(u.uid) = ? and u.pwd = ?;'''
                ,(ID,pwd))
            
            # check if valid user ID
            row = c.fetchone()
            if row is not None:
                userID = row[0]
            
            # if incorrect ID and pwd tell user and redo loop
            if userID == None:
                print("Not a valid username or password")
    return userID  # if both are none then user is backing out
