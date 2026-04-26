import pymysql as p

#CONNECT A DATABASE
db = p.connect(
    host="localhost",
    user="root",
    password="shiny",
    database="mounika")
c = db.cursor()
def mainmenu():
    print(" ~~~~~~~ Welcome TO Livewire Portal  ~~~~~~~")
    print("\t1.Register \n\t2.View All Data \n\t3.View One Data \n\t4.Update Data \n\t5.Delete Data \n\t6.Exit")
    choice = int(input("Enter the choice :"))
    if choice == 1:
        insertData()
    elif choice == 2:
        viewAllData()
    elif choice == 3:
        viewOneData()
    elif choice == 4:
        updateData()
    elif choice == 5:
        deleteData()
    elif choice == 6:
        print("Thank you !!")
        import sys
        sys.exit(0)
    else:
        print("Invalid Choice")
def createTable():
    #CREATE TABLE
    c.execute("CREATE TABLE REGISTER(USERNAME VARCHAR(20),PASSWORD INT(4))")
    db.close()
def alterTable():
    c.execute("ALTER TABLE REGISTER ADD COLUMN PHONE BIGINT(10)")
    db.commit()
    db.close()
def insertData():
    u = input("Enter the username :")
    p = int(input("Enter the password :"))
    ph = int(input("Enter the phone number :"))
    query = "INSERT INTO REGISTER VALUES('%s','%d','%d')"%(u,p,ph)
    try:
        c.execute(query)
        db.commit()
        db.close()
    except:
        db.rollback()
        db.close()
def viewAllData():
    query = "SELECT * FROM REGISTER"
    c.execute(query)
    data = c.fetchall()
    for i in data:
        un = i[0]
        pa = i[1]
        pho = i[2]
        print("Username :",un,end=" , ")
        print("Password :",pa,end=" , ")
        print("Phone Number :",pho)
def viewOneData():
    key = input("Enter the name :")
    query = "SELECT * FROM REGISTER WHERE USERNAME='%s'"%key
    c.execute(query)
    data = c.fetchall()
    for i in data:
        un = i[0]
        pa = i[1]
        pho = i[2]
        print("Username :",un,end=" , ")
        print("Password :",pa,end=" , ")
        print("Phone Number :",pho)
def updateData():
    name = input("Enter the name :")
    print("Choice 1: Update Username \nChoice 2: Update Password \nChoice 3:Update Phone Number")
    ch = int(input("Enter the choice (1/2/3):"))
    query=""
    if ch == 1:
        newname = input("Please Enter the name :")
        query="UPDATE REGISTER SET USERNAME='%s' WHERE USERNAME='%s'"%(newname,name)
    elif ch == 2:
        newpassword = int(input("Please Enter the password :"))
        query="UPDATE REGISTER SET PASSWORD='%d' WHERE USERNAME='%s'"%(newpassword,name)
    elif ch == 3:
        newphone = int(input("Please Enter the phone :"))
        query="UPDATE REGISTER SET PHONE='%d' WHERE USERNAME='%s'"%(newphone,name)
    else:
        print("Invalid Choice")
    try:
        c.execute(query)
        db.commit()
    except:
        print("error")
    db.close()
def deleteData():
    name = input("Enter the username to delete :")
    try:
        sql="DELETE FROM REGISTER WHERE USERNAME = '%s'"%(name)
        c.execute(sql)
        db.commit()
        print("Deleted")
    except Exception as e:
        print("Not Deleted",e)
        db.rollback()
    db.close()
while True:
    mainmenu()









    
