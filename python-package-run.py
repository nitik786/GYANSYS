from weather_package.api import WeatherAPI
from weather_package.database import WeatherDatabase

api_key = '30d4741c779ba94c470ca1f63045390a'
db_host = 'localhost'
db_user = 'root'
db_password = 'Gaurighat@1'
db_database = 'weather'


weather_api = WeatherAPI(api_key)
weather_db = WeatherDatabase(db_host, db_user, db_password, db_database)


city = 'muzaffarpur'  # Replace with the city for which you want to fetch weather data
weather_data = weather_api.get_weather(city)

if weather_data:

    weather = weather_data['weather'][0]['main']
    temperature = round(weather_data['main']['temp'])


    weather_db.store_weather_data(city, weather, temperature)


    df = weather_db.retrieve_weather_data()
    print("Weather Data:")
    print(df)
else:
    print("No data available for the city.")

