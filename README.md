COMP 3005 - Assignment 3

This project is a small Student Database demo that uses PostgreSQL and Python.

The program can:

Show all students

Add a student

Update a student’s email

Delete a student

The SQL functions are in A3.1.sql, and the Python code that calls them is in Comp3005_A3.py.

Setup

Make sure PostgreSQL is running.

Create or use a database (ex: COMP_3005_A3).

Run the SQL file:

psql -d COMP_3005_A3 -f A3.1.sql


Install Python dependency:

pip install psycopg2


Run the Python file:

python Comp3005_A3.py


