#Task2
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
    sql = (f"select type,count(*) from airport where iso_country='{code}' group by type order by type;")
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        print(f"The airports located are:")
        for items in result:
            print(f"{items[0]}:{items[1]}")
    else:
        print("Invalid ICAO CODE!!!")
    return

userInput = input("Enter ID code of the country:")
get(userInput)