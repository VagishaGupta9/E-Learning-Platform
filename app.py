# Import modules
from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import torch




# Create a Flask app
app = Flask(__name__)

# Dummy user 
dummy_user = {'username': 'admin', 'password': '123'}

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == dummy_user['username'] and password == dummy_user['password']:
          
            return redirect(url_for('dashboard', username=username))
        else:
            error = 'Invalid credentials. Please try again.'

    return render_template('login.html', error=error)

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username, user=dummy_user)

# Add a new route for the Python editor
@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/run', methods=['POST'])
@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']

    with open('temp_script.py', 'w') as file:
        file.write(code)

    try:
        result = subprocess.run(["C:\\Users\\vagu\\AppData\\Local\\Programs\\Python\\Python38\\python.exe", 'temp_script.py'], capture_output=True, text=True)
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)

    return {'output': output}


@app.route('/learning_python')
def learning_python():
    return render_template('learning_python.html')

@app.route('/ai_exps')
def ai_exps():
    return render_template('ai_exps.html')

@app.route('/ai_learning')
def ai_learning():
    return render_template('ai_learning.html')






# Run the app
if __name__ == '__main__':
    app.run(debug=True)
