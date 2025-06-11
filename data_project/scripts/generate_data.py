import psycopg2
from faker import Faker

def connect_to_db():
   print("Connecting to PostgreSQL database...")
   try:
     conn = psycopg2.connect(
        host="postgres",
        dbname="hospital_db",
        user="postgres",
        password="postgres",
        port="5342",
        
     )
     return conn
   except:
     print("Error connecting to PostgreSQL database")
     return None