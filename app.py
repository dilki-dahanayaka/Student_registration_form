from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "student_secret"

# ---------- Database Setup ----------
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reg_no TEXT,
            date TEXT,
            full_name TEXT,
            dob TEXT,
            gender TEXT,
            class_name TEXT,
            religion TEXT,
            skills TEXT,
            father_name TEXT,
            father_occ TEXT,
            mother_name TEXT,
            mother_occ TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------- Routes ----------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    reg_no = request.form.get('reg_no')
    date = request.form.get('date')
    full_name = request.form.get('full_name')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    class_name = request.form.get('class_name')
    religion = request.form.get('religion')
    skills = request.form.get('skills')
    father_name = request.form.get('father_name')
    father_occ = request.form.get('father_occ')
    mother_name = request.form.get('mother_name')
    mother_occ = request.form.get('mother_occ')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (reg_no, date, full_name, dob, gender, class_name, religion, skills, father_name, father_occ, mother_name, mother_occ)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (reg_no, date, full_name, dob, gender, class_name, religion, skills, father_name, father_occ, mother_name, mother_occ))
    conn.commit()
    conn.close()

    flash("✅ Student registered successfully!")
    return redirect('/')

@app.route('/view')
def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('view.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
