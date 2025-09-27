from .connection import get_connection

def insert_student(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO information 
        (department, course, year, semester, Student_ID, name, section, age, gender, Phone, email, bus) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", data)
    conn.commit()
    conn.close()

def fetch_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM information")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_student(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""UPDATE information 
        SET department=%s, course=%s, year=%s, semester=%s, name=%s, section=%s, age=%s, gender=%s, Phone=%s, email=%s, bus=%s 
        WHERE Student_ID=%s""", data)
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM information WHERE Student_ID=%s", (student_id,))
    conn.commit()
    conn.close()

def search_students(field, keyword):
    conn = get_connection()
    cur = conn.cursor()
    query = f"SELECT * FROM information WHERE {field} LIKE %s"
    cur.execute(query, ('%' + keyword + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows
