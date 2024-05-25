import mysql.connector as mysql
from decouple import config

class DatabaseConnector:

    connection = None
    
    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host=config('DB_HOST'),
            port=int(config('DB_PORT')),
            database=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD')
        )
        cls.connection = db_connection

