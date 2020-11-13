import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
#    passwd="root"
   passwd="root",
    database="testdatabase"
    )
    
mycursor = db.cursor()
    
#mycursor.execute("CREATE DATABASE testdatabase")

#mycursor.execute("CREATE TABLE People (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
   
mycursor.execute("INSERT INTO People (name, created, gender) VALUES (%s,%s,%s)", ("GERMAN",datetime.now(),"M"))

db.commit()
