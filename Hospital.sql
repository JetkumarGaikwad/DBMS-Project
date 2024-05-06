-- Create database
CREATE DATABASE HospitalManagementSystem;

-- Use database
USE HospitalManagementSystem;

-- Create table for patients
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Address VARCHAR(255),
    Phone VARCHAR(15)
);

-- Insert sample data into Patients table
INSERT INTO Patients (Name, Age, Gender, Address, Phone)
VALUES 
    ('John Doe', 45, 'Male', '123 Main St, Anytown, USA', '+1234567890'),
    ('Jane Smith', 35, 'Female', '456 Elm St, Another Town, USA', '+1987654321');

-- Create table for medical staff
CREATE TABLE MedicalStaff (
    StaffID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Position VARCHAR(100),
    Department VARCHAR(100),
    Phone VARCHAR(15)
);

-- Insert sample data into MedicalStaff table
INSERT INTO MedicalStaff (Name, Age, Gender, Position, Department, Phone)
VALUES 
    ('Dr. David Johnson', 40, 'Male', 'Surgeon', 'Surgery', '+1122334455'),
    ('Dr. Sarah Williams', 35, 'Female', 'Physician', 'Internal Medicine', '+9988776655');

-- Create table for medical equipment
CREATE TABLE MedicalEquipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Type VARCHAR(100),
    Quantity INT
);

-- Insert sample data into MedicalEquipment table
INSERT INTO MedicalEquipment (Name, Type, Quantity)
VALUES 
    ('X-ray Machine', 'Diagnostic', 2),
    ('MRI Scanner', 'Imaging', 1);