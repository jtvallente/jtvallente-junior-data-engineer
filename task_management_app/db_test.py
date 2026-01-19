"""
/db_test.py: a quick database connection test.
"""

from dotenv import load_dotenv
from database_provider.db_connection import connection_estab

load_dotenv()

conn = connection_estab()

if not conn:
    print("DB connection failed")
else:
    print("DB connected")
    cur = conn.cursor()
    cur.execute("SELECT DATABASE()")
    print("Using DB:", cur.fetchone()[0])
    cur.close()
    conn.close()
