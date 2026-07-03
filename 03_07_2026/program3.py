# connect mysql workbanch from python code

try:
    import mysql.connector
    from mysql.connector import Error

except ModuleNotFoundError as e:
    print(e)

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'UniDb'
    )

    if connection.is_connected():
        print("data base successfully connected to mysql server ")

except Error as e:
    print(f"Error while connecting to mysql : ",e)
finally:
    print("finally block")