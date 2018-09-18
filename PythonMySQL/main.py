import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="atul",database="COMPANY")

c = mydb.cursor()

data = [
("Mr. Bean", "Granny"),
("Ben10", "Omnitrix"),
("Phineas", "Mars"),
("Ferb", "Venus"),
("Doremon", "Drawer"),
]

sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
c.executemany(sql, data)

mydb.commit()#commit the action under execute 

print(c.rowcount, "record inserted.")
'''
# Python-MySQL
mysql connection in python
pip installs :-
1. sudo apt-get install python-dev libmysqlclient-dev
2. sudo pip install MySQL-python

#To check the database changes 
1. open another terminal 
2. run sudo mysql -u username -p
3. enter system password then sql password
4. run- show databases;
5. then - use database_name ;
6. shoe tables ;
7. select * from table_name
'''