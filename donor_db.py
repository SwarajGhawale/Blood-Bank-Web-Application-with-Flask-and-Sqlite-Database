import sqlite3 as sql

#connect to SQLite
con = sql.connect('users.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ='''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 username TEXT NOT NULL,
                                 password TEXT NOT NULL)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()