-- hospital_db/init.sql
CREATE TABLE IF NOT EXISTS patients(
    patient_id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    diagnosis VARCHAR(255) NOT NULL,
    admission_date DATE NOT NULL,
    amount_paid DECIMAL(10, 2) NOT NULL

);