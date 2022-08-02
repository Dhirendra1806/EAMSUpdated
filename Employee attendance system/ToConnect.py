'''pymysql module is use to connect to mysql database
1. import mysql module
2. get the database connection object pymysql.connect() get cusror() (is the  main objcet to perform sql query)
3. Exceute the sql command  by excecute function of cursor 
4. fetch the record by fetchall,fetchone function 
5. close the connection'''
import pymysql
db=pymysql.connect(host='localhost',user='root',password='root',database='company') 
cur=db.cursor()
sql="Select * from empdata"
cur.execute(sql)
data=cur.fetchall()
for x in data:
    
    print('Empno',x[0])
    print('Name',x[1])   
    print('City',x[2])
    print('ctc',x[3])
    
db.close()