-- schema.sql
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS studentmanagementsystem;

-- Use the newly created or existing database
USE studentmanagementsystem;

-- Create the 'information' table if it doesn't exist
CREATE TABLE IF NOT EXISTS information (
    department VARCHAR(255),
    course VARCHAR(255),
    year VARCHAR(255),
    semester VARCHAR(255),
    Student_ID VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    section VARCHAR(255),
    age INT,
    gender VARCHAR(50),
    Phone VARCHAR(20),
    email VARCHAR(255),
    bus VARCHAR(50)
);