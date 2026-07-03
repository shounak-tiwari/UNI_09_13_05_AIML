from mysql.connector import connect

try:
    connect = connect(
    host = "localhost",
    user= "root",
    password = "root",
    database = "anydb",
    port = 3306
    )

except:
    print("oops some error or some run time errors ")


# if connect.is_connected():/
#     print("Heyy It get connected ")

# else:
#     print("Ooops its not ")