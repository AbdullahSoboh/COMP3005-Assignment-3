# Student Management System

This application is designed to manage student records in a PostgreSQL database. It supports basic CRUD (Create, Read, Update, Delete) operations such as adding a new student, retrieving all student records, updating a student's email, and deleting a student record.

## Prerequisites

- Python 3.6 or higher
- PostgreSQL server running locally
- psycopg2 Python library (for PostgreSQL integration)

## Setup Instructions

1. **Database Setup:**
   - Make sure PostgreSQL is installed and running on your system.
   - Create a database named `school`. You can do this using pgAdmin or the PostgreSQL command line tool with the command: `CREATE DATABASE school;`.
   - Use the provided SQL script or pgAdmin to create the `students` table with the necessary schema.

2. **Environment Setup:**
   - Ensure Python 3.6 or higher is installed on your system.
   - Install psycopg2 library using pip:
     ```sh
     pip install psycopg2
     ```

## Running the Application

1. Open your terminal or command prompt.
2. Navigate to the directory containing the application files.
3. Run the application with the command:
   ```sh
   python Assignment3Question1.py

## Application Functions

- **`getAllStudents()`**: Retrieves and displays all student records from the database.
- **`addStudent(first_name, last_name, email, enrollment_date)`**: Inserts a new student record into the database. Requires the first name, last name, email, and enrollment date as parameters.
- **`updateStudentEmail(student_id, new_email)`**: Updates the email address for a student identified by `student_id` with `new_email`.
- **`deleteStudent(student_id)`**: Deletes the record of a student identified by `student_id`.

## Demonstration Video

A video demonstrating the setup of the database and the execution of each function in the application is available [here](https://youtu.be/1taQobn-kR4). This video shows how to perform INSERT, UPDATE, and DELETE operations and their effects on the database using pgAdmin.

## Additional Notes

- Ensure the PostgreSQL server is running before executing the application.
- Modify the database connection parameters in the `connect_db` function as necessary to match your PostgreSQL setup (e.g., database name, user, password).
