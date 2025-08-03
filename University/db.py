import sqlite3
from contextlib import closing

DB_NAME = 'university.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            family TEXT,
            phone TEXT,
            student_code TEXT UNIQUE,
            gender TEXT,
            age INTEGER,
            field TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            family TEXT,
            phone TEXT,
            gender TEXT,
            age INTEGER,
            edu TEXT,
            history TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            title TEXT,
            vahed INTEGER,
            dars_type TEXT,
            prerequisites TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS class_rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            capacity INTEGER
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS sections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER,
            teacher_id INTEGER,
            class_room_id INTEGER,
            time TEXT,
            FOREIGN KEY(course_id) REFERENCES courses(id),
            FOREIGN KEY(teacher_id) REFERENCES teachers(id),
            FOREIGN KEY(class_room_id) REFERENCES class_rooms(id)
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            section_id INTEGER,
            grade REAL,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(section_id) REFERENCES sections(id)
        )''')
        conn.commit()

def add_student(name, family, phone, student_code, gender, age, field):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO students (name, family, phone, student_code, gender, age, field)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (name, family, phone, student_code, gender, age, field))
        conn.commit()

def get_students():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM students')
        return c.fetchall()

def get_student_by_code(student_code):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM students WHERE student_code=?', (student_code,))
        return c.fetchone()

def get_student_by_id(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM students WHERE id=?', (id,))
        return c.fetchone()

def update_student(id, name, family, phone, student_code, gender, age, field):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''UPDATE students SET name=?, family=?, phone=?, student_code=?, gender=?, age=?, field=? WHERE id=?''',
                  (name, family, phone, student_code, gender, age, field, id))
        conn.commit()

def delete_student(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('DELETE FROM students WHERE id=?', (id,))
        conn.commit()

# استاد

def add_teacher(name, family, phone, gender, age, edu, history):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO teachers (name, family, phone, gender, age, edu, history)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (name, family, phone, gender, age, edu, history))
        conn.commit()

def get_teachers():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM teachers')
        return c.fetchall()

def get_teacher_by_id(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM teachers WHERE id=?', (id,))
        return c.fetchone()

def update_teacher(id, name, family, phone, gender, age, edu, history):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''UPDATE teachers SET name=?, family=?, phone=?, gender=?, age=?, edu=?, history=? WHERE id=?''',
                  (name, family, phone, gender, age, edu, history, id))
        conn.commit()

def delete_teacher(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('DELETE FROM teachers WHERE id=?', (id,))
        conn.commit()

# درس

def add_course(code, title, vahed, dars_type, prerequisites):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO courses (code, title, vahed, dars_type, prerequisites)
                     VALUES (?, ?, ?, ?, ?)''',
                  (code, title, vahed, dars_type, prerequisites))
        conn.commit()

def get_courses():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM courses')
        return c.fetchall()

def get_course_by_code(code):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM courses WHERE code=?', (code,))
        return c.fetchone()

def get_course_by_id(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM courses WHERE id=?', (id,))
        return c.fetchone()

def update_course(id, code, title, vahed, dars_type, prerequisites):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''UPDATE courses SET code=?, title=?, vahed=?, dars_type=?, prerequisites=? WHERE id=?''',
                  (code, title, vahed, dars_type, prerequisites, id))
        conn.commit()

def delete_course(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('DELETE FROM courses WHERE id=?', (id,))
        conn.commit()

# کلاس

def add_class_room(name, capacity):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO class_rooms (name, capacity) VALUES (?, ?)''', (name, capacity))
        conn.commit()

def get_class_rooms():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM class_rooms')
        return c.fetchall()

def get_class_room_by_name(name):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM class_rooms WHERE name=?', (name,))
        return c.fetchone()

def get_class_room_by_id(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM class_rooms WHERE id=?', (id,))
        return c.fetchone()

def update_class_room(id, name, capacity):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''UPDATE class_rooms SET name=?, capacity=? WHERE id=?''', (name, capacity, id))
        conn.commit()

def delete_class_room(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('DELETE FROM class_rooms WHERE id=?', (id,))
        conn.commit()

# سکشن

def add_section(course_id, teacher_id, class_room_id, time):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO sections (course_id, teacher_id, class_room_id, time)
                     VALUES (?, ?, ?, ?)''', (course_id, teacher_id, class_room_id, time))
        conn.commit()

def get_sections():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM sections')
        return c.fetchall()

def get_section_by_id(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM sections WHERE id=?', (id,))
        return c.fetchone()

def update_section(id, course_id, teacher_id, class_room_id, time):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''UPDATE sections SET course_id=?, teacher_id=?, class_room_id=?, time=? WHERE id=?''',
                  (course_id, teacher_id, class_room_id, time, id))
        conn.commit()

def delete_section(id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('DELETE FROM sections WHERE id=?', (id,))
        conn.commit()

# ثبت‌نام و نمره

def enroll_student(student_id, section_id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO enrollments (student_id, section_id, grade) VALUES (?, ?, NULL)''', (student_id, section_id))
        conn.commit()

def set_grade(student_id, section_id, grade):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''UPDATE enrollments SET grade=? WHERE student_id=? AND section_id=?''', (grade, student_id, section_id))
        conn.commit()

def get_enrollments():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM enrollments')
        return c.fetchall()

def get_student_grades(student_id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT section_id, grade FROM enrollments WHERE student_id=?', (student_id,))
        return c.fetchall()

def get_section_students(section_id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT student_id, grade FROM enrollments WHERE section_id=?', (section_id,))
        return c.fetchall()

# مقداردهی اولیه دیتابیس
if __name__ == '__main__':
    init_db() 