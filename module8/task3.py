import mysql.connector
from geopy import distance

def get_cord_and_name(icao):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '16102006',
    autocommit = True,
)

code1 = input("Enter the icao code of the first airport: ")
code2 = input("Enter the icao code of the second airport: ")

st_airport = get_cord_and_name(code1)
nd_airport = get_cord_and_name(code2)

if st_airport is None and nd_airport is None:
    print("Error. Unable to find the airports.")
elif st_airport is None:
    print("Error. Unable to find the first airport.")
elif nd_airport is None:
    print("Error. Unable to find the second airport.")
else:
    st_airport_cord = (st_airport["latitude_deg"], st_airport["longitude_deg"])
    nd_airport_cord = (nd_airport["latitude_deg"], nd_airport["longitude_deg"])
    print(f"The distance from {st_airport['name']} to {nd_airport['name']} is {distance.distance(st_airport_cord, nd_airport_cord).km:<.1f} km.")

