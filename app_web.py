from flask import Flask, render_template, request, redirect, url_for, session
import connection as db
from dotenv import load_dotenv
import os

load_dotenv('.env')
KEY = os.getenv('KEY')

app = Flask(__name__)
app.secret_key = KEY

@app.route("/", methods=['GET','POST'])
def home(user=None,passw=None,check=None):
    if 'username' in session:
        login = db.select_usuario()
        return render_template("homepage.html",user=login)
    return render_template("homepage.html",user=None)

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route("/cadastro", methods=['GET','POST'])
def cadastro():
    if request.method =='POST':
        #fazer o insert daqui
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        session['username'] = username
        session['email'] = email
        session['password'] = password
        return render_template('login.html')
    return render_template('cadastro.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
    
#rum
if __name__ == "__main__":
    app.run(debug=True)