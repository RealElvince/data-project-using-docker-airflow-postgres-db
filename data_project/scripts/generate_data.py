import psycopg2
from faker import Faker

import random

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
     print("Connection successful")
     return conn
   
      
   except:
     print("Error connecting to PostgreSQL database")
     return None


fake = Faker()
def generate_patient_data(num_records):

  conn = connect_to_db()

  for _ in range(num_records):
    gender = ['Male', 'Female']
    diagnoses = [
    "Hypertension","Diabetes Mellitus","Asthma","Chronic Obstructive Pulmonary Disease (COPD)", "Pneumonia","Tuberculosis","Malaria","Migraine","Peptic Ulcer Disease","Urinary Tract Infection (UTI)",
    "Anemia",
    "COVID-19",
    "HIV/AIDS",
    "Depression",
    "Anxiety Disorder"
]
    first_name = fake.first_name()
    last_name = fake.last_name()
    date_of_birth = fake.date_of_birth()
    gender = random.choice(gender)
    age = fake.random_int(min=0, max=100)
    admission_date = fake.date_time_this_year()
    discharge_date = fake.date_time_this_year(after=admission_date)
    diagnosis = random.choice(diagnoses)
    amount_paid = round(fake.random_number(digits=10), 2)

    # Insert the generated patient data into the database
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (first_name, last_name, date_of_birth, gender, age, admission_date, discharge_date, diagnosis, amount_paid)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (first_name, last_name, date_of_birth, gender, age, admission_date, discharge_date, diagnosis, amount_paid))
    conn.commit()
    cursor.close()


def generate_doctor_data(num_records):

  doctor_specializations = [
    "General Practitioner (GP)",
    "Cardiologist",
    "Dermatologist",
    "Endocrinologist",
    "Gastroenterologist",
    "Neurologist",
    "Nephrologist",
    "Oncologist",
    "Ophthalmologist",
    "Orthopedic Surgeon",
    "Otolaryngologist (ENT)",
    "Pediatrician",
    "Psychiatrist",
    "Pulmonologist",
    "Radiologist",
    "Rheumatologist",
    "Urologist",
    "Obstetrician/Gynecologist (OB/GYN)",
    "Anesthesiologist",
    "Pathologist",
    "Surgeon (General)",
    "Infectious Disease Specialist",
    "Hematologist",
    "Allergist/Immunologist",
    "Geriatrician",
    "Emergency Medicine Specialist",
    "Internal Medicine Specialist",
    "Family Medicine Physician",
    "Plastic Surgeon",
    "Sports Medicine Specialist"
]


  for _ in range(num_records):
    first_name = fake.first_name()
    last_name = fake.last_name()
    specialization = random.choice(doctor_specializations)
  

  # Insert the generated doctor data into the database
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO doctors (first_name, last_name, specialization)
        VALUES (%s, %s, %s)
    """, (first_name, last_name, specialization))
    conn.commit()
    cursor.close()
    conn.close()
