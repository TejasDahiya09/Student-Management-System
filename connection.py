import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="sqluser",       # change if needed
        password="password",  # change if needed
        database="studentmanagementsystem"
    )
