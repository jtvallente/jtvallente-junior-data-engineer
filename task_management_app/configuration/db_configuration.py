"""
configuration/db_configuration.py: Database configurations for MYSQL connection
Note: when running on a different device, update the values below. I recommend to use .env to not push the private credentials to the repository
"""

import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "task_manager")
DB_PORT = int(os.getenv("DB_PORT", 3306))