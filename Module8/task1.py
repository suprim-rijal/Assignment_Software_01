#Task1
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='suprim123',
         autocommit=True
         )

def get(code):
    sql = (f"select name,municipality from airport where ident='{code}'")
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        for items in result:
            print(f"The airport name is : {items[0]}\nThe Municipality name is : {items[1]}")
    else:
        print("Invalid ICAO CODE!!!")

    return
userInput = input("Enter ICAO code of the airport:")
get(userInput)