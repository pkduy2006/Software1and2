from flask import Flask, Response
import json
import math

app = Flask(__name__)
@app.route('/prime_number/<number>')
def is_prime(number):
    try:
        int_number = int(number)
        check = True
        for i in range(2, int(math.sqrt(int_number) + 1)):
            if int_number % i == 0:
                check = False
                break
        if int_number < 2:
            check = False
        response = {"Number": number}
        if check:
            response["isPrime"] = True
        else:
            response["isPrime"] = False
        return response
    except ValueError:
        response = {
            "message": "Invalid number as input",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status = 400, mimetype = "application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response = json_response, status = 404, mimetype = "application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader = True, host ="127.0.0.1", port = 5000)