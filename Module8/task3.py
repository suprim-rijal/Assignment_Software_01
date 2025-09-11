#Task3
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='suprim123',
         autocommit=True
         )

def get(code):
    sql = (f"select latitude_deg,longitude_deg from airport where ident='{code}'")
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        return result
    else:
        print("Invalid ICAO CODE or Results cannot be Found in Database!!!")

ICAO_Code1 = input("Enter ICAO code of the first airport:")
ICAO_Code2 = input("Enter ICAO code of the second airport:")

airport1 = get(ICAO_Code1)
airport2 = get(ICAO_Code2)

distace_between = distance.distance(airport1,airport2).km

print(f"The Distance between the airport is :{distace_between:.2f}")

