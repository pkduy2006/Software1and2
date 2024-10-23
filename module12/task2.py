import requests

city_name = input("Enter the city name: ")
#country_code = input("Enter the country code: ")
#request1 = "http://api.openweathermap.org/geo/1.0/direct?q=" + city_name + "," + country_code + "&appid=33dd23764fa14c0bd3a056f84cae3ea0"
#response1 = requests.get(request1).json()
#latitude_deg = response1[0]["lat"]
#longitude_deg = response1[0]["lon"]
request = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=33dd23764fa14c0bd3a056f84cae3ea0&units=metric"
response = requests.get(request).json()
#print(json.dumps(response, indent = 2))
#print(response)
print(f"Temperature in Celsius degree: {response['main']['temp']:.1f}")
print(f"Weather description: {response['weather'][0]['description']}")
