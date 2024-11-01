import requests
import pandas as pd
from datetime import datetime

API_KEY = "444fd0a8dea1095c02b6f8666623949d"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # For temperature in Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        data = response.json()

        # Check if city is found
        if data.get("cod") != 200:
            print(f"City '{city_name}' not found.")
            return None

        # Extract required fields
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        return {
            "City": city_name,
            "Temperature (°C)": temperature,
            "Weather Description": weather_desc,
            "Humidity (%)": humidity,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_csv(data, filename="weather_data.csv"):
    df = pd.DataFrame([data])
    try:
        # Append to existing CSV or create a new one
        df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def main():
    while True:
        city_name = input("Enter city name (or 'exit' to quit): ")
        if city_name.lower() == 'exit':
            break

        weather_data = fetch_weather(city_name)
        if weather_data:
            print(weather_data)
            save_to_csv(weather_data)

if __name__ == "__main__":
    main()

