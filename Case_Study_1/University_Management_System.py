# ============================================================
# University Management System
# Developed & Commented by: Prashant Kumar Jha
# ============================================================

import csv
import json

# ============================================================
# In-Memory Database
# ============================================================

students = {}     # student_id -> student details
faculty = {}      # faculty_id -> faculty details
courses = {}      # course_id -> course details
complaints = []   # complaints from students and faculty


# ============================================================
# AUTHENTICATION FUNCTIONS
# ============================================================

def admin_auth():
    print("\n--- ADMIN LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # admin<number>@gmail.com | abc@<number>
    if username.startswith("admin") and username.endswith("@gmail.com"):
        num = username.replace("admin", "").replace("@gmail.com", "")
        if num.isdigit() and password == f"abc@{num}":
            print("Admin login successful")
            return True

    print("ERROR: Invalid admin credentials")
    return False


def faculty_auth():
    print("\n--- FACULTY LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # faculty_id@gmail.com | abc@faculty_id
    if username.endswith("@gmail.com"):
        fid = username.replace("@gmail.com", "")
        if fid in faculty and password == f"abc@{fid}":
            print("Faculty login successful")
            return fid

    print("ERROR: Invalid faculty credentials")
    return None


def student_auth():
    print("\n--- STUDENT LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # student_id@gmail.com | abc@student_id
    if username.endswith("@gmail.com"):
        sid = username.replace("@gmail.com", "")
        if sid in students and password == f"abc@{sid}":
            print("Student login successful")
            return sid

    print("ERROR: Invalid student credentials")
    return None


# ============================================================
# ADMIN FUNCTIONS
# ============================================================

def add_course():
    print("\n--- ADD COURSE ---")
    cid = input("Course ID: ").strip()
    name = input("Course Name: ").strip()
    credits = int(input("Course Credits: ").strip())

    courses[cid] = {
        "name": name,
        "credits": credits,
        "faculty": None,
        "students": []
    }
    print("Course added successfully")


def add_faculty():
    print("\n--- ADD FACULTY ---")
    fid = input("Faculty ID: ").strip()
    name = input("Faculty Name: ").strip()
    dept = input("Department: ").strip()
    salary = input("Salary: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()

    faculty[fid] = {
        "name": name,
        "department": dept,
        "salary": salary,
        "email": email,
        "phone": phone,
        "courses": []
    }

    print("Faculty added successfully")
    print("Faculty Login Password:", f"abc@{fid}")


def assign_faculty():
    print("\n--- ASSIGN FACULTY TO COURSE ---")
    cid = input("Course ID: ").strip()
    fid = input("Faculty ID: ").strip()

    if cid in courses and fid in faculty:
        courses[cid]["faculty"] = fid
        faculty[fid]["courses"].append(cid)
        print("Faculty assigned successfully")
    else:
        print("Invalid course or faculty")


def enroll_student():
    print("\n--- ENROLL STUDENT (MULTIPLE COURSES) ---")

    if not courses:
        print("No courses available")
        return

    sid = input("Student ID: ").strip()
    name = input("Student Name: ").strip()
    dept = input("Department: ").strip()
    sem = input("Semester: ").strip()

    print("\nAvailable Courses:")
    for cid, c in courses.items():
        print(f"{cid} - {c['name']}")

    course_input = input(
        "Enter Course IDs to enroll (comma separated): "
    ).strip()

    selected_courses = [c.strip() for c in course_input.split(",")]

    valid_courses = []
    for cid in selected_courses:
        if cid in courses:
            valid_courses.append(cid)
        else:
            print(f"Invalid course skipped: {cid}")

    if not valid_courses:
        print("No valid courses selected")
        return

    # Create student if new
    if sid not in students:
        students[sid] = {
            "name": name,
            "department": dept,
            "semester": sem,
            "courses": {}   # course_id -> marks
        }
        print("Student created")
        print("Student Login Password:", f"abc@{sid}")

    # Enroll student in selected courses
    for cid in valid_courses:
        students[sid]["courses"][cid] = None
        courses[cid]["students"].append(sid)

    print("Student enrolled successfully in courses:", valid_courses)


def view_all_students():
    print("\n--- ALL STUDENTS ---")
    for sid, s in students.items():
        print(sid, s)


def view_all_courses():
    print("\n--- ALL COURSES ---")
    for cid, c in courses.items():
        print(cid, c)


def view_all_faculty():
    print("\n--- ALL FACULTY ---")
    for fid, f in faculty.items():
        print(fid, f)


def generate_csv():
    with open("university_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Student ID", "Name", "Department", "Semester", "Courses"])

        for sid, s in students.items():
            writer.writerow([
                sid,
                s["name"],
                s["department"],
                s["semester"],
                s["courses"]
            ])

    print("CSV file generated successfully")


def generate_json():
    with open("university_data.json", "w") as f:
        json.dump({
            "students": students,
            "faculty": faculty,
            "courses": courses,
            "complaints": complaints
        }, f, indent=2)

    print("JSON file generated successfully")


def compare_students():
    print("\n--- STUDENT PERFORMANCE COMPARISON ---")
    for sid, s in students.items():
        marks = [m for m in s["courses"].values() if m is not None]
        avg = sum(marks) / len(marks) if marks else 0
        print(f"{sid} -> Average Marks: {avg}")


def view_complaints():
    print("\n--- COMPLAINTS ---")
    for c in complaints:
        print(c)


# ============================================================
# FACULTY MENU
# ============================================================

def faculty_menu(fid):
    while True:
        print("""
FACULTY MENU
1 View My Details
2 View Salary
3 Assign Marks
4 Send Complaint
5 Back to Main Menu
""")
        ch = input("Choice: ").strip()

        if ch == "1":
            print(faculty[fid])

        elif ch == "2":
            print("Salary:", faculty[fid]["salary"])

        elif ch == "3":
            for cid in faculty[fid]["courses"]:
                print(f"\nAssigning marks for course: {cid}")
                for sid in courses[cid]["students"]:
                    marks = int(input(f"Enter marks for {sid}: "))
                    students[sid]["courses"][cid] = marks
            print("Marks updated successfully")

        elif ch == "4":
            msg = input("Enter complaint: ")
            complaints.append(f"Faculty {fid}: {msg}")
            print("Complaint sent")

        elif ch == "5":
            break


# ============================================================
# STUDENT MENU
# ============================================================

def student_menu(sid):
    while True:
        print("""
STUDENT MENU
1 View My Details
2 View My Marks
3 Try Restricted Feature
4 Send Complaint
5 Back to Main Menu
""")
        ch = input("Choice: ").strip()

        if ch == "1":
            print(students[sid])

        elif ch == "2":
            print("Marks:", students[sid]["courses"])

        elif ch == "3":
            print(
                "WARNING: You are not authorised as a student. "
                "Please contact admin."
            )

        elif ch == "4":
            msg = input("Enter complaint: ")
            complaints.append(f"Student {sid}: {msg}")
            print("Complaint sent")

        elif ch == "5":
            break


# ============================================================
# MAIN MENU
# ============================================================

def main():
    print("Welcome to University Management System")

    while True:
        print("""
MAIN MENU
1 Admin
2 Faculty
3 Student
4 Exit
""")
        choice = input("Choice: ").strip()

        if choice == "1":
            if admin_auth():
                while True:
                    print("""
ADMIN MENU
1 Add Course
2 Add Faculty
3 Assign Faculty to Course
4 Enroll Student (Multiple Courses)
5 View All Students
6 View All Courses
7 View All Faculty
8 Generate CSV
9 Generate JSON
10 Compare Students
11 View Complaints
12 Back to Main Menu
""")
                    c = input("Choice: ").strip()

                    if c == "1": add_course()
                    elif c == "2": add_faculty()
                    elif c == "3": assign_faculty()
                    elif c == "4": enroll_student()
                    elif c == "5": view_all_students()
                    elif c == "6": view_all_courses()
                    elif c == "7": view_all_faculty()
                    elif c == "8": generate_csv()
                    elif c == "9": generate_json()
                    elif c == "10": compare_students()
                    elif c == "11": view_complaints()
                    elif c == "12": break

        elif choice == "2":
            fid = faculty_auth()
            if fid:
                faculty_menu(fid)

        elif choice == "3":
            sid = student_auth()
            if sid:
                student_menu(sid)

        elif choice == "4":
            print("\nThank you for using University Management System")
            print("\nFor more suggestions or complaints,")
            print("please contact original admin:")
            print("Name  : Prashant Kumar Jha")
            print("Email : prashantkumarjha100@gmail.com")
            break


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()






# ============================================================
# LOGIN CREDENTIAL FORMAT (IMPORTANT – FOR FUTURE REFERENCE)
# ------------------------------------------------------------
# ADMIN LOGIN:
# Username : admin<number>@gmail.com
# Password : abc@<number>
# Example  :
# Username : admin1@gmail.com
# Password : abc@1
#
# FACULTY LOGIN:
# Username : <faculty_id>@gmail.com
# Password : abc@<faculty_id>
# Example  :
# Username : F101@gmail.com
# Password : abc@F101
#
# STUDENT LOGIN:
# Username : <student_id>@gmail.com
# Password : abc@<student_id>
# Example  :
# Username : S001@gmail.com
# Password : abc@S001
#
# NOTE:
# - These formats are mandatory
# - Any mismatch will result in authentication failure
#
# Written & maintained by: Prashant Kumar Jha
# ============================================================
