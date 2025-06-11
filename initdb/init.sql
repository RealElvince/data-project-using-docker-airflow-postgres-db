-- create schema
CREATE SCHEMA IF NOT EXISTS hospital;

-- patients table
 CREATE  TABLE IF NOT EXISTS hospital.patients (
    patient_id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    admission_date DATE NOT NULL,
    discharge_date DATE,
    diagnosis VARCHAR(255) NOT NULL,
    amount_paid DECIMAL(10, 2) NOT NULL
);


-- doctors table
CREATE TABLE IF NOT EXISTS hospital.doctors (
    doctor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL
);


