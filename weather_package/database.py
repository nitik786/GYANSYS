import mysql.connector
import pandas as pd

class WeatherDatabase:
    def __init__(self, host, user, password, database):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Gaurighat@1',
            'database': 'weather',
        }

    def store_weather_data(self, city, weather, temperature):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            insert_query = "INSERT INTO weather_data (city, weather, temperature) VALUES (%s, %s, %s)"
            data = (city, weather, temperature)
            cursor.execute(insert_query, data)
            connection.commit()
        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            cursor.close()
            connection.close()

    def retrieve_weather_data(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            query = "SELECT city, weather, temperature FROM weather_data"
            df = pd.read_sql_query(query, connection)
            return df
        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            connection.close()

