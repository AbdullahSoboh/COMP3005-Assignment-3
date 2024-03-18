import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def connect_db():
    #Connecting to the datebase
    try:
        conn = psycopg2.connect(
            dbname='school',
            user='postgres',
            password='abood',
            host='localhost' 
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def getAllStudents():
    # Connect to the PostgreSQL database
    conn = connect_db()
    cur = conn.cursor()
    try:
        # Execute the SQL query to select all records from the students table
        cur.execute("SELECT * FROM students;")
        # Fetch all rows from the query result and return as tuples stored in records
        records = cur.fetchall()
        # Iterate through each row and print
        for row in records:
            print(row)
    except Exception as e:
        # Print any error that occurs during the database operation
        print(f"Error fetching data: {e}")
    finally:
        # Close the cursor and connection to free resources
        cur.close()
        conn.close()


def addStudent(first_name, last_name, email, enrollment_date):
    # Connect to the PostgreSQL database
    conn = connect_db()
    cur = conn.cursor()
    try:
        # Execute the SQL command to insert a new record into the students table
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date)
        )
        # Inform the user that the student was added successfully
        print("Student added successfully.")
    except Exception as e:
        # Print any error that occurs during the database operation
        print(f"Error adding student: {e}")
    finally:
        # Close the cursor and connection to free resources
        cur.close()
        conn.close()


def updateStudentEmail(student_id, new_email):
    # Connect to the PostgreSQL database
    conn = connect_db()
    cur = conn.cursor()
    try:
        # Execute the SQL command to update the email of a specific student
        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id)
        )
        # Inform the user that the email was updated successfully
        print("Email updated successfully.")
    except Exception as e:
        # Print any error that occurs during the database operation
        print(f"Error updating email: {e}")
    finally:
        # Close the cursor and connection to free resources
        cur.close()
        conn.close()


def deleteStudent(student_id):
    # Connect to the PostgreSQL database
    conn = connect_db()
    cur = conn.cursor()
    try:
        # Execute the SQL command to delete a specific student record
        cur.execute(
            "DELETE FROM students WHERE student_id = %s;",
            (student_id,)
        )
        # Inform the user that the student was deleted successfully
        print("Student deleted successfully.")
    except Exception as e:
        # Print any error that occurs during the database operation
        print(f"Error deleting student: {e}")
    finally:
        # Close the cursor and connection to free resources
        cur.close()
        conn.close()


if __name__ == "__main__":
    # Test the functionality of CRUD operations
    getAllStudents()
    addStudent('Abdullah', 'Soboh', 'abood@carletoniscool.com', '1920-10-01')
    getAllStudents()
    updateStudentEmail(15, 'newabood@example.com')
    getAllStudents()
    deleteStudent(17)
    getAllStudents()
