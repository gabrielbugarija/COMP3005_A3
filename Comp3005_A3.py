import os # for environment variables
import psycopg2 # PostgreSQL adapter
from contextlib import contextmanager # for context manager

def get_conn():
    return psycopg2.connect(
        database=os.getenv("PGDATABASE", "COMP_3005_A3"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "sharkGym8888"),
        host=os.getenv("PGHOST", "127.0.0.1"),
        port=os.getenv("PGPORT", "5433"),
    )

@contextmanager
def cursor(commit=False):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            yield cur
            if commit:
                conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

# -------- CRUD wrappers that call the SQL functions --------

def getAllStudents():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_all_students();")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT add_student(%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_id

def updateStudentEmail(student_id, new_email):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT update_student_email(%s, %s);",
                (student_id, new_email))
    result = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return result

def deleteStudent(student_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT delete_student(%s);", (student_id,))
    result = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return result

# Demo
if __name__ == "__main__":
    print("== All students ==")
    for row in getAllStudents():
        print(row)

    print("\n== Add new student ==")
    new_id = addStudent("Z", "J", "ZJ@example.com", "2025-09-10")
    print("new id:", new_id)

    print("\n== Update email ==")
    print("rows updated:", updateStudentEmail(new_id, "ZCJ.X@example.com"))

    print("\n== After update, list ==")
    for row in getAllStudents():
        print(row)

    print("\n== Delete ==")
    print("rows deleted:", deleteStudent(new_id))

    print("\n== Final list ==")
    for row in getAllStudents():
        print(row)
