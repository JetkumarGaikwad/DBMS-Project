import mysql.connector
import sys

# Connect to MySQL
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tejaswini@123",
            database="hospitalmanagementsystem"
        )
        print("Connected to MySQL database")
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None

# Create tables
def create_tables(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                gender VARCHAR(10),
                address VARCHAR(255)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                specialization VARCHAR(255)
            )
        """)
        print("Tables created successfully")
        conn.commit()
    except mysql.connector.Error as err:
        print("Error creating tables:", err)

# Insert data
def insert_patient(conn):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    address = input("Enter patient address: ")
    
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO patients (name, age, gender, address)
            VALUES (%s, %s, %s, %s)
        """, (name, age, gender, address))
        conn.commit()
        print("Patient inserted successfully")
    except mysql.connector.Error as err:
        print("Error inserting patient:", err)

def insert_doctor(conn):
    name = input("Enter doctor name: ")
    specialization = input("Enter doctor specialization: ")
    
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO doctors (name, specialization)
            VALUES (%s, %s)
        """, (name, specialization))
        conn.commit()
        print("Doctor inserted successfully")
    except mysql.connector.Error as err:
        print("Error inserting doctor:", err)

# Retrieve data
def get_patients(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        for patient in patients:
            print(patient)
    except mysql.connector.Error as err:
        print("Error fetching patients:", err)

def get_doctors(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM doctors")
        doctors = cursor.fetchall()
        for doctor in doctors:
            print(doctor)
    except mysql.connector.Error as err:
        print("Error fetching doctors:", err)

# Update data
def update_patient_address(conn):
    patient_id = int(input("Enter patient ID: "))
    new_address = input("Enter new address: ")
    
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE patients
            SET address = %s
            WHERE patient_id = %s
        """, (new_address, patient_id))
        conn.commit()
        print("Patient address updated successfully")
    except mysql.connector.Error as err:
        print("Error updating patient address:", err)

# Delete data
def delete_patient(conn):
    patient_id = int(input("Enter patient ID to delete: "))
    
    cursor = conn.cursor()
    try:
        cursor.execute("""
            DELETE FROM patients
            WHERE patient_id = %s
        """, (patient_id,))
        conn.commit()
        print("Patient deleted successfully")
    except mysql.connector.Error as err:
        print("Error deleting patient:", err)

# Main function
def main():
    conn = connect_to_mysql()
    if conn:
        create_tables(conn)

        while True:
            print("\n1. Insert Patient")
            print("2. Insert Doctor")
            print("3. Get Patients")
            print("4. Get Doctors")
            print("5. Update Patient Address")
            print("6. Delete Patient")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                insert_patient(conn)
            elif choice == '2':
                insert_doctor(conn)
            elif choice == '3':
                get_patients(conn)
            elif choice == '4':
                get_doctors(conn)
            elif choice == '5':
                update_patient_address(conn)
            elif choice == '6':
                delete_patient(conn)
            elif choice == '7':
                conn.close()
                sys.exit("Exiting program")
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
