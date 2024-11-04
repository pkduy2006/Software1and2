import requests

city_name = input("Enter the city name: ")
request = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=33dd23764fa14c0bd3a056f84cae3ea0&units=metric"
try:
    response = requests.get(request)
    if not response.ok:
        raise requests.exceptions.RequestsWarning()

    json_response = response.json()
    print(f"""Temperature in Celsius degree: {json_response['main']['temp']:.1f}
Weather description: {json_response['weather'][0]['description']}""")
except requests.exceptions.RequestException as error:
    print("Your request could not be completed.")
except requests.exceptions.RequestsWarning as error:
    print("Invalid request.")