import mysql.connector

def get_name_and_town(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
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
         autocommit = True
         )

code = input("Enter the ICAO code of an airport: ")
airport = get_name_and_town(code)
if airport is not None:
    print(f"{airport['name']} is located in {airport['municipality']}.")
else:
     print("Error. Unable to find the airport.")