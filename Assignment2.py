import requests
from datetime import datetime

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def apidata():
    response = requests.get(url)
    data = response.json()
    return data

def get_temperature(data, date):
    for item in data['list']:
        timestamp = item['dt']
        date_time = datetime.utcfromtimestamp(timestamp)
        if date_time.strftime('%Y-%m-%d %H:%M:%S') == date:
            return item['main']['temp']
    return None

def get_wind_speed(data, date):
    for item in data['list']:
        timestamp = item['dt']
        date_time = datetime.utcfromtimestamp(timestamp)
        if date_time.strftime('%Y-%m-%d %H:%M:%S') == date:
            return item['wind']['speed']
    return None

def get_pressure(data, date):
    for item in data['list']:
        timestamp = item['dt']
        date_time = datetime.utcfromtimestamp(timestamp)
        if date_time.strftime('%Y-%m-%d %H:%M:%S') == date:
            return item['main']['pressure']
    return None


data = apidata()

while True:
    print("\n1. Get Temperature\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
    choice = input("Enter your choice: ")

    if choice == '0':
        print("Exiting program.")
        break
    elif choice == '1':
        date = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
        temperature = get_temperature(data, date)
        if temperature is not None:
            print(f"Temperature at {date}: {temperature}°C")
        else:
            print("Data not available for the given date and time.")
    elif choice == '2':
        date = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
        wind_speed = get_wind_speed(data, date)
        if wind_speed is not None:
            print(f"Wind Speed at {date}: {wind_speed} m/s")
        else:
            print("Data not available for the given date and time.")
    elif choice == '3':
        date = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
        pressure = get_pressure(data, date)
        if pressure is not None:
            print(f"Pressure at {date}: {pressure} ")
        else:
            print("No Data for the given date and time.")
    else:
        print("Invalid choice.")


