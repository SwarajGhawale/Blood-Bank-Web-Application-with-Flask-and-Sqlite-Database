from flask import Flask, render_template, request
from flask import render_template
import sqlite3
# import requests
from flask import Flask
from flask import request,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import TextField
app = Flask(__name__)
app.secret_key = "ThisisSecretKey"

@app.route("/")
def home():
    conn = sqlite3.connect('users.db')
    return "<h1>Welcome Page</h1>"

@app.route("/greet")
def greet():
    value = request.args.get('name')
    return render_template('greet.html', name = value)
@app.route("/index")
def index():
    #value = request.args.get('name')
    return render_template('index.html')
        
@app.route('/login', methods=['GET', 'POST'])
def  login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Open database connection
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        #c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 #username TEXT NOT NULL,
                                 #password TEXT NOT NULL)''')
        # Check if username already exists
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        if result != None:
            return "Username already exists"
        else:
        # Insert new user into database
         c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
         conn.commit()

        # Close database connection
        conn.close()
        return redirect('/index')

    return render_template('login.html')

@app.route("/donor")
def donor():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    print("Opened database successfully")
    c.execute('''CREATE TABLE IF NOT EXISTS blood (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, donorname TEXT, donorsex TEXT, qty TEXT, dweight TEXT, donoruname TEXT, phone TEXT)''')
    print( "Table created successfully")
    conn.close()
    return render_template('donor.html')

@app.route('/add', methods =['POST','GET'])
def add():
    msg = ""
    if request.method == 'POST':
        try:
           type = request.form['blood_group']
           donorname = request.form['donorname']
           donorsex = request.form['gender']
           qty = request.form['qty']
           dweight = request.form['dweight']
           email = request.form['email']
           phone = request.form['phone']



           with sqlite3.connect("users.db") as conn:
              cur = conn.cursor()
              cur.execute("INSERT INTO blood (type,donorname,donorsex,qty,dweight,donoremail,phone) VALUES (?,?,?,?,?,?,?)",(type,donorname,donorsex,qty,dweight,email,phone) )
              conn.commit()
              msg = "Record successfully added"
        except:
           conn.rollback()
           msg = "error in insert operation"

        finally:
            flash("added new entry!")
            return redirect(url_for('index'))
        con.close()

    else:
        return render_template('index.html',msg=msg)

@app.route("/jsdemo")
def jsdemo():
    return render_template('jsdemo.html')

if __name__ == '__main__':
    app.run(debug=True)