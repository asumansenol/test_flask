from flask import current_app, g
import mysql.connector

# get the environment variables
db_user = 'test'
db_password = 'asutest'
db_name = 'asu_interview'
db_connection_name = '34.71.66.174'

def getdb():
    if 'db' not in g or not g.db.is_connected():
        g.db = mysql.connector.connect(
            host=db_connection_name,
            user=db_user,
            password=db_password,
            database=db_name
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None and db.is_connected():
        db.close()

def check_user_exist(name, email):
    conn = getdb()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Users;')
    users = cursor.fetchall()
    #check user exist
    for user in users:
        if user['Email'] == email and user['Name'] == name:
            conn.close()
            return user
    cursor.close()
    return False

def update_user_status(user_id, status):
    conn = getdb()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('UPDATE Users SET status = %s WHERE id = %s', (status, user_id))
    conn.commit()
    cursor.close()

def add_user(user):
    user_id = None
    conn = getdb()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('INSERT INTO Users (name, email, status) VALUES(%s, %s, %s)', (user["name"], user["email"], user["status"]))
    #return the user id
    user_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    return user_id
