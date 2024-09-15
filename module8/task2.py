import mysql.connector

def get_airports(code):
    sql = f"SELECT name, type FROM airport WHERE iso_country = %s ORDER BY type, name"
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql, (code,))
    result = cursor.fetchall()
    return result

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '16102006',
    autocommit = True,
)

area_code = input("Enter the code of the area: ")
airports = get_airports(area_code)
if len(airports) == 0:
    print("Error. No airport found.")
else:
    cnt = 1
    for each_airport in airports:
        print(f"{cnt}. {each_airport['name']}: {each_airport['type']}")
        cnt += 1

