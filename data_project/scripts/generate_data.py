import psycopg2
from faker import Faker
from datetime import timedelta
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


def generate_patient_data(num_records):
    print("Connecting to PostgreSQL database...")
    try:
        with psycopg2.connect(
            host="postgres",
            dbname="hospital_db",
            user="postgres",
            password="postgres",
            port="5432"
        ) as conn:
            print("Connection successful")
            with conn.cursor() as cursor:
                for _ in range(num_records):
                    gender = random.choice(['Male', 'Female'])
                    first_name = fake.first_name()
                    last_name = fake.last_name()
                    date_of_birth = fake.date_of_birth()
                    age = fake.random_int(min=0, max=100)
                    admission_date = fake.date_time_this_year()
                    discharge_date = admission_date + timedelta(days=random.randint(1, 10))
                    diagnosis = random.choice(DIAGNOSES)
                    amount_paid = round(fake.random_number(digits=5), 2)

                    try:
                        cursor.execute("""
                            INSERT INTO hospital.patients (
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
            print(f"{num_records} patient records inserted successfully.")
    except Exception as e:
        print(f"Error connecting to database: {e}")


def generate_doctor_data(num_records):
    print("Connecting to PostgreSQL database...")
    try:
        with psycopg2.connect(
            host="postgres",
            dbname="hospital_db",
            user="postgres",
            password="postgres",
            port="5432"
        ) as conn:
            print("Connection successful")
            with conn.cursor() as cursor:
                for _ in range(num_records):
                    first_name = fake.first_name()
                    last_name = fake.last_name()
                    specialization = random.choice(DOCTOR_SPECIALIZATIONS)

                    try:
                        cursor.execute("""
                            INSERT INTO hospital.doctors (first_name, last_name, specialization)
                            VALUES (%s, %s, %s)
                        """, (first_name, last_name, specialization))
                    except Exception as e:
                        print(f"Failed to insert doctor: {e}")

            conn.commit()
            print(f"{num_records} doctor records inserted successfully.")
    except Exception as e:
        print(f"Error connecting to database: {e}")