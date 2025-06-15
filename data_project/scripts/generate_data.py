import psycopg2
from faker import Faker
import random

# Constants
DIAGNOSES = [
    "Hypertension", "Diabetes Mellitus", "Asthma", "Chronic Obstructive Pulmonary Disease (COPD)",
    "Pneumonia", "Tuberculosis", "Malaria", "Migraine", "Peptic Ulcer Disease",
    "Urinary Tract Infection (UTI)", "Anemia", "COVID-19", "HIV/AIDS",
    "Depression", "Anxiety Disorder"
]

DOCTOR_SPECIALIZATIONS = [
    "General Practitioner (GP)", "Cardiologist", "Dermatologist", "Endocrinologist",
    "Gastroenterologist", "Neurologist", "Nephrologist", "Oncologist", "Ophthalmologist",
    "Orthopedic Surgeon", "Otolaryngologist (ENT)", "Pediatrician", "Psychiatrist",
    "Pulmonologist", "Radiologist", "Rheumatologist", "Urologist",
    "Obstetrician/Gynecologist (OB/GYN)", "Anesthesiologist", "Pathologist",
    "Surgeon (General)", "Infectious Disease Specialist", "Hematologist",
    "Allergist/Immunologist", "Geriatrician", "Emergency Medicine Specialist",
    "Internal Medicine Specialist", "Family Medicine Physician", "Plastic Surgeon",
    "Sports Medicine Specialist"
]

fake = Faker()

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
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None


def generate_patient_data(num_records):
    conn = connect_to_db()
    if conn is None:
        return

    cursor = conn.cursor()

    for _ in range(num_records):
        gender_choice = ['Male', 'Female']
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth()
        gender = random.choice(gender_choice)
        age = fake.random_int(min=0, max=100)
        admission_date = fake.date_time_this_year()
        discharge_date = fake.date_time_this_year(after=admission_date)
        diagnosis = random.choice(DIAGNOSES)
        amount_paid = round(fake.random_number(digits=5), 2)

        try:
            cursor.execute("""
                INSERT INTO patients (
                    first_name, last_name, date_of_birth, gender, age,
                    admission_date, discharge_date, diagnosis, amount_paid
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                first_name, last_name, date_of_birth, gender, age,
                admission_date, discharge_date, diagnosis, amount_paid
            ))
        except Exception as e:
            print(f"Failed to insert patient: {e}")

    conn.commit()
    cursor.close()
    conn.close()


def generate_doctor_data(num_records):
    conn = connect_to_db()
    if conn is None:
        return

    cursor = conn.cursor()

    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        specialization = random.choice(DOCTOR_SPECIALIZATIONS)

        try:
            cursor.execute("""
                INSERT INTO doctors (first_name, last_name, specialization)
                VALUES (%s, %s, %s)
            """, (first_name, last_name, specialization))
        except Exception as e:
            print(f"Failed to insert doctor: {e}")

    conn.commit()
    cursor.close()
    conn.close()
