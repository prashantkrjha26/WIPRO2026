"""
SMART UNIVERSITY MANAGEMENT SYSTEM
=================================
Single-file Python project demonstrating:

- OOP (Inheritance, Abstraction, Polymorphism)
- Decorators
- Descriptors
- Operator Overloading
- Generators
- File Handling (JSON, CSV)
- Menu-driven application
"""

import json
import csv
import time
from abc import ABC, abstractmethod


# =====================================================
# GLOBAL STATE (LOGIN)
# =====================================================

CURRENT_USER_ROLE = None   # "admin" or "student"


def login():
    """
    Simple role-based login.
    """
    global CURRENT_USER_ROLE
    print("\nLogin")
    print("1. Admin")
    print("2. Student")
    choice = input("Select role: ")

    if choice == "1":
        CURRENT_USER_ROLE = "admin"
    elif choice == "2":
        CURRENT_USER_ROLE = "student"
    else:
        print("Invalid choice")
        login()


# =====================================================
# DECORATORS
# =====================================================

def log_execution(func):
    """
    Logs successful execution of a method.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} executed successfully")
        return result
    return wrapper


def performance_timer(func):
    """
    Measures execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper


def admin_only(func):
    """
    Restricts access to admin-only actions.
    """
    def wrapper(*args, **kwargs):
        if CURRENT_USER_ROLE != "admin":
            print("Access Denied: Admin only")
            return
        return func(*args, **kwargs)
    return wrapper


# =====================================================
# DESCRIPTORS
# =====================================================

class MarksDescriptor:
    """
    Validates marks (0–100).
    """
    def __get__(self, instance, owner):
        return instance.__dict__.get("marks", [])

    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks must be between 0 and 100")
        instance.__dict__["marks"] = value


class SalaryDescriptor:
    """
    Prevents salary from being read directly.
    """
    def __get__(self, instance, owner):
        print("Access Denied: Salary is confidential")
        return None

    def __set__(self, instance, value):
        instance.__dict__["_salary"] = value


# =====================================================
# ABSTRACT BASE CLASS
# =====================================================

class Person(ABC):
    """
    Base class for Student and Faculty.
    """

    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass


# =====================================================
# STUDENT CLASS
# =====================================================

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.attendance = 0

    def get_details(self):
        print("\nStudent Details")
        print("----------------------------")
        print("ID         :", self.id)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Semester   :", self.semester)

    def mark_attendance(self):
        self.attendance += 1
        print(f"Attendance marked for {self.name}")

    def calculate_gpa(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 85:
            return 4.0
        elif avg >= 70:
            return 3.0
        elif avg >= 55:
            return 2.0
        else:
            return 1.0

    @log_execution
    @performance_timer
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"

        print("\nPerformance Report")
        print("----------------------------")
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Average :", round(avg, 2))
        print("Grade   :", grade)
        print("GPA     :", self.calculate_gpa())

        return avg

    def __gt__(self, other):
        """
        Compare students using > operator.
        """
        return self.calculate_performance() > other.calculate_performance()


# =====================================================
# FACULTY CLASS
# =====================================================

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("\nFaculty Details")
        print("----------------------------")
        print("ID         :", self.id)
        print("Name       :", self.name)
        print("Department :", self.department)


# =====================================================
# COURSE CLASS
# =====================================================

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

    def __iter__(self):
        yield self.code
        yield self.name
        yield self.credits


# =====================================================
# UNIVERSITY DATA STORAGE
# =====================================================

class UniversityData:
    students = {}
    faculty = {}
    courses = {}
    enrollments = {}   # {student_id: [course_codes]}

    @staticmethod
    def student_generator():
        for s in UniversityData.students.values():
            yield f"{s.id} - {s.name}"


# =====================================================
# FILE HANDLING
# =====================================================

def save_students_json():
    data = []
    for s in UniversityData.students.values():
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })

    with open("students.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Student data saved to students.json")


def load_students_json():
    try:
        with open("students.json", "r") as f:
            data = json.load(f)

        for s in data:
            UniversityData.students[s["id"]] = Student(
                s["id"], s["name"], s["department"],
                s["semester"], s["marks"]
            )
        print("Student data loaded")
    except FileNotFoundError:
        pass


def generate_csv():
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "GPA"])

        for s in UniversityData.students.values():
            avg = sum(s.marks) / len(s.marks)
            writer.writerow([s.id, s.name, s.department, round(avg, 2), s.calculate_gpa()])

    print("CSV report generated")


# =====================================================
# TRANSCRIPT & SEARCH
# =====================================================

def generate_transcript(student):
    print("\nTranscript")
    print("----------------------------")
    print("Name       :", student.name)
    print("Department :", student.department)
    print("Semester   :", student.semester)
    print("Marks      :", student.marks)
    print("GPA        :", student.calculate_gpa())
    print("Courses    :", UniversityData.enrollments.get(student.id, []))


def search_student(name):
    for s in UniversityData.students.values():
        if name.lower() in s.name.lower():
            s.get_details()


# =====================================================
# MAIN MENU
# =====================================================

def main():
    login()
    load_students_json()

    while True:
        print("\nMENU")
        print("1 Add Student")
        print("2 Add Faculty")
        print("3 Add Course")
        print("4 Enroll Student")
        print("5 Calculate Performance")
        print("6 Compare Students")
        print("7 Generate Reports")
        print("8 Generate Transcript")
        print("9 Search Student")
        print("10 Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                sid = input("Student ID: ")
                name = input("Name: ")
                dept = input("Department: ")
                sem = int(input("Semester: "))
                marks = list(map(int, input("Marks: ").split()))
                UniversityData.students[sid] = Student(sid, name, dept, sem, marks)

            elif choice == "2":
                fid = input("Faculty ID: ")
                name = input("Name: ")
                dept = input("Department: ")
                sal = int(input("Salary: "))
                UniversityData.faculty[fid] = Faculty(fid, name, dept, sal)

            elif choice == "3":
                code = input("Course Code: ")
                cname = input("Course Name: ")
                credits = int(input("Credits: "))
                fid = input("Faculty ID: ")
                UniversityData.courses[code] = Course(
                    code, cname, credits, UniversityData.faculty[fid]
                )

            elif choice == "4":
                sid = input("Student ID: ")
                code = input("Course Code: ")
                UniversityData.enrollments.setdefault(sid, []).append(code)

            elif choice == "5":
                sid = input("Student ID: ")
                UniversityData.students[sid].calculate_performance()

            elif choice == "6":
                s1 = UniversityData.students[input("Student 1 ID: ")]
                s2 = UniversityData.students[input("Student 2 ID: ")]
                print("Result:", s1 > s2)

            elif choice == "7":
                generate_csv()
                save_students_json()
                for s in UniversityData.student_generator():
                    print(s)

            elif choice == "8":
                sid = input("Student ID: ")
                generate_transcript(UniversityData.students[sid])

            elif choice == "9":
                name = input("Enter name to search: ")
                search_student(name)

            elif choice == "10":
                save_students_json()
                print("Goodbye!")
                break

        except Exception as e:
            print("Error:", e)


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":
    main()
