import sqlite3
from sqlite3 import Error

def main():
    connection = connect_db("/Users/gabriel/Desktop/LyncUpDB")
    create_user_table(connection)
    username = input("What email would you like to be your username?: ")
    password = input("Please enter a password: ")
    insert_user(connection, username, password)
    associate_friends(connect_db("/Users/gabriel/Desktop/LyncUpDB"), "test", ['Gabe', 'Barney'])
    associate_calendar(connect_db("/Users/gabriel/Desktop/LyncUpDB"), "test", ['True', 'False', 'True', 'True'])
    fetch_users(connection)
    close_connection(connection)

def connect_db(database):
    connection = None
    try:
        connection = sqlite3.connect(database)
    except Error as error:
        print(error)
    finally:
        if connection:
            #print(sqlite3.version)
            return connection

def create_user_table(connection):
    connection.execute("CREATE TABLE IF NOT EXISTS userTable(Username, Password, Calendar, Friends)")
    connection.commit()

def insert_user(connection, username, password):
    connection.execute("INSERT INTO userTable Values (?, ?, ?, ?)", (username, password, None, None))
    connection.commit()

def fetch_users(connection):
    #maybe can do two None inputs initally into table, then can replace after when searching
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM userTable")
    logins = cursor.fetchall()
    connection.commit()
    for login in logins:
        print(login)
    return logins

def associate_friends(connection, username, friends):
    cursor = connection.cursor()
    cursor.execute("UPDATE userTable SET Friends = ? WHERE Username = ?", (str(friends), username))
    connection.commit()

def associate_calendar(connection, username, calendar):
    cursor = connection.cursor()
    cursor.execute("UPDATE userTable SET Calendar = ? WHERE Username = ?", (str(calendar), username))
    connection.commit()

def string_to_array(array_str):
    entry = ""
    new_array = []
    for i in array_str:
        if i.isalpha():
            entry += i
        elif i == ',' or i == ']':
            new_array.append(entry)
            entry = ""
    return new_array

def close_connection(connection):
    connection.close()

if __name__ == "__main__":
     main()
