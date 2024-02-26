import pickle
import os
import sqlite3
import subprocess

# Vulnerable code
def load_data_from_file(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

# Vulnerable code
def calculate_expression(expression):
    return eval(expression)

# Vulnerable code
def run_command(command):
    os.system(command)

# Vulnerable code
def run_command(command):
    subprocess.call(command, shell=True)

# Vulnerable code
def greet_user(username):
    message = f"Hello, {username}!"
    print(message)

# Vulnerable code
def get_user_data(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    user_data = cursor.fetchone()
    conn.close()
    return user_data
