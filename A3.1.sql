--Gabriel Bugarija 
--101262776

-- Return full list
CREATE OR REPLACE FUNCTION get_all_students()
RETURNS SETOF students
LANGUAGE sql AS $$
  SELECT * FROM students ORDER BY student_id;
$$;


-- Insert
CREATE OR REPLACE FUNCTION add_student(
  new_first_name TEXT,
  new_last_name TEXT,
  new_email TEXT,
  new_enrollment_date DATE
)
RETURNS students
LANGUAGE sql AS $$
  INSERT INTO students (first_name, last_name, email, enrollment_date)
  VALUES (new_first_name, new_last_name, new_email, new_enrollment_date)
  RETURNING *;
$$;


-- Update
CREATE OR REPLACE FUNCTION update_student_email(
  p_student_id BIGINT,
  p_new_email  TEXT
)
RETURNS students
LANGUAGE sql AS $$
  UPDATE students
     SET email = p_new_email
   WHERE student_id = p_student_id
   RETURNING *;
$$;


-- Delete
CREATE OR REPLACE FUNCTION delete_student(
  p_student_id BIGINT
)
RETURNS students
LANGUAGE sql AS $$
  DELETE FROM students
   WHERE student_id = p_student_id
   RETURNING *;
$$;
