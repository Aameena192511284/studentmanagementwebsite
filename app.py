from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "studentmanagement.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return """
    <h1>Student Management System</h1>

    <a href="/student">Student Management</a><br><br>
    <a href="/course">Course Management</a><br><br>
    <a href="/enrollment">Enrollment Management</a>
    """


@app.route("/student", methods=["GET", "POST"])
def student():

    conn = get_db()

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        email = request.form["email"]

        conn.execute(
            """
            INSERT INTO student
            (student_name, gender, age, phone, email)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, gender, age, phone, email)
        )

        conn.commit()

    students = conn.execute(
        "SELECT * FROM student"
    ).fetchall()

    conn.close()

    rows = ""

    for s in students:
        rows += f"""
        <tr>
        <td>{s['student_name']}</td>
        <td>{s['age']}</td>
        <td>{s['gender']}</td>
        <td>{s['phone']}</td>
        <td>{s['email']}</td>
        </tr>
        """

    return f"""
    <h1>Student Management</h1>

    <form method="POST">

    Name:
    <input name="name"><br><br>

    Age:
    <input name="age"><br><br>

    Gender:
    <input name="gender"><br><br>

    Phone:
    <input name="phone"><br><br>

    Email:
    <input name="email"><br><br>

    <button>Add Student</button>

    </form>

    <h2>Student Records</h2>

    <table border="1">
    <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Gender</th>
    <th>Phone</th>
    <th>Email</th>
    </tr>

    {rows}

    </table>

    <br>
    <a href="/">Home</a>
    """


@app.route("/course", methods=["GET", "POST"])
def course():

    conn = get_db()

    if request.method == "POST":

        course_name = request.form["course_name"]
        department = request.form["department"]

        conn.execute(
            """
            INSERT INTO course
            (course_name, department)
            VALUES (?, ?)
            """,
            (course_name, department)
        )

        conn.commit()

    courses = conn.execute(
        "SELECT * FROM course"
    ).fetchall()

    conn.close()

    rows = ""

    for c in courses:
        rows += f"""
        <tr>
        <td>{c['course_id']}</td>
        <td>{c['course_name']}</td>
        <td>{c['department']}</td>
        </tr>
        """

    return f"""
    <h1>Course Management</h1>

    <form method="POST">

    Course Name:
    <input name="course_name"><br><br>

    Department:
    <input name="department"><br><br>

    <button>Add Course</button>

    </form>

    <h2>Course Records</h2>

    <table border="1">

    <tr>
    <th>ID</th>
    <th>Course Name</th>
    <th>Department</th>
    </tr>

    {rows}

    </table>

    <br>
    <a href="/">Home</a>
    """

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():

    conn = get_db()

    if request.method == "POST":

        student_id = request.form["student_id"]
        course_id = request.form["course_id"]

        conn.execute(
            """
            INSERT INTO enrollement
            (student_id, course_id)
            VALUES (?, ?)
            """,
            (student_id, course_id)
        )

        conn.commit()

    enrollments = conn.execute(
        "SELECT * FROM enrollement"
    ).fetchall()

    conn.close()

    rows = ""

    for e in enrollments:
        rows += f"""
        <tr>
        <td>{e['enrollement_id']}</td>
        <td>{e['student_id']}</td>
        <td>{e['course_id']}</td>
        </tr>
        """

    return f"""
    <h1>Enrollment Management</h1>

    <form method="POST">

    Student ID:
    <input name="student_id"><br><br>

    Course ID:
    <input name="course_id"><br><br>

    <button>Enroll Student</button>

    </form>

    <h2>Enrollment Records</h2>

    <table border="1">

    <tr>
    <th>Enrollment ID</th>
    <th>Student ID</th>
    <th>Course ID</th>
    </tr>

    {rows}

    </table>

    <br>
    <a href="/">Home</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
