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