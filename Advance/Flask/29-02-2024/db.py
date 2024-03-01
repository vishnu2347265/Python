import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')
#create a connection
cur = con.cursor()
#Drop users table if already exist.
cur.execute("Drop Table IF  EXISTS Users")
#Create the Users table with columns: ID, FirstName, LastName and Email.
sql = '''CREATE TABLE Users("UID" INTEGER PRIMARY KEY AUTOINCREMENT,"UNAME" TEXT NOT NULL,"CONTACT" TEXT )'''
cur.execute(sql)
#commit changes
con.commit()
#close the connection
con.close()
