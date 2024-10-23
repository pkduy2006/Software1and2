from flask import Flask, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '16102006',
    autocommit = True
)

app = Flask(__name__)
@app.route('/airport/<icao>')
def get_airport(icao):
    try:
        sql = """SELECT name, municipality FROM airport WHERE ident = %s;"""
        cursor = connection.cursor(dictionary = True)
        cursor.execute(sql, (icao,))
        result = cursor.fetchone()
        response = {
            "ICAO": icao,
            "Name": result["name"],
            "Location": result["municipality"]
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid ICAO code.",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status = 400, mimetype = "application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint.",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response = json_response, status = 404, mimetype = "application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port = 5000)