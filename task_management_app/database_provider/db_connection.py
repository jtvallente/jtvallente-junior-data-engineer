"""
database_provider/db_connection.py: connects to the MySQL database
"""

import mysql.connector
from configuration.db_configuration import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def connection_estab():
    """
    This functions creates a connection to the database and will return a MySQL DB Connection. This will use try-catch block mechanism
    """
    try: 
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    except mysql.connector.Error as e:
        print("There is an error connecting to the MySQL Database. Error: ", e)
        return None
