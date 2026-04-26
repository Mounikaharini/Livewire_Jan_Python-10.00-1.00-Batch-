import pymysql as p

#CONNECT A DATABASE
db = p.connect(
    host="localhost",
    user="root",
    password="shiny",
    database="mounika")
c = db.cursor()

#CREATE TABLE
c.execute("CREATE TABLE LOGIN(USERNAME VARCHAR(20),PASSWORD INT(4))")
db.close()

#INSERTING A DATA

#MANUAL INPUT
'''query = "INSERT INTO LOGIN VALUES('MOUNIKA','1234')"'''

# INPUT GET FROM USER
u = input("Enter the username :")
p = int(input("Enter the password :"))

query = "INSERT INTO LOGIN VALUES('%s','%d')"%(u,p)
try:
    c.execute(query)
    db.commit()
    db.close()
except:
    db.rollback()
    db.close()
    
#DELETE
try:
    sql="DELETE FROM LOGIN WHERE USERNAME = 'MOUNIKA'"
    c.execute(sql)
    db.commit()
    print("Deleted")
except Exception as e:
    print("Not Deleted",e)
    db.rollback()
db.close()

# VIEW DATA
try:
    c.execute("SELECT * FROM LOGIN")
    data = c.fetchall()
    for i in data:
        username = data[0]
        password = data[1]
        print(username,password)
    print(data)
    db.close()
except:
    print("error")
    db.rollback()

#UPDATE QUERY
try:
    #c.execute("UPDATE LOGIN SET PASSWORD=9876")
    c.execute("UPDATE LOGIN SET PASSWORD=9876 WHERE USERNAME='JAYAKUMAR'")
    db.commit()
except:
    print("error")
db.close()
