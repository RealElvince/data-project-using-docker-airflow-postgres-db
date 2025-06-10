import psycopg2
from faker import Faker

conn = psycopg2.connect(
    dbname="hospital_db",
    user="postgres",
    password="postgres",
    port="5342"
)

