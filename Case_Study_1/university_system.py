import json
import csv


# BASE CLASS


class Person:
    def __init__(self, pid_value, pname_value, dept_value):
        self.id = pid_value
        self.name = pname_value
        self.department = dept_value

    def get_details(self):
        pass



# STUDENT CLASS


class Student(Person):
    def __init__(self, sid_value, sname_value, dept_value, sem_value, marks_value):
        super().__init__(sid_value, sname_value, dept_value)
        self.semester = sem_value
        self.marks = marks_value

    def fetch_performance(self):
        avg_score = sum(self.marks) / len(self.marks)

        if avg_score >= 80:
            grade_score = "A"
        elif avg_score >= 60:
            grade_score = "B"
        else:
            grade_score = "C"

        return avg_score, grade_score

    def __gt__(self, other_student_obj):
        return sum(self.marks) > sum(other_student_obj.marks)



# FACULTY CLASS


class Faculty(Person):
    def __init__(self, fid_value, fname_value, dept_value, salary_value):
        super().__init__(fid_value, fname_value, dept_value)
        self.salary = salary_value



# COURSE CLASS


class Course:
    def __init__(self, code_value, cname_value, credit_value, faculty_object):
        self.code = code_value
        self.name = cname_value
        self.credits = credit_value
        self.faculty = faculty_object

    def __add__(self, other_course_obj):
        return self.credits + other_course_obj.credits



# FILE LOADING FUNCTIONS


def load_students():
    with open("students.json", "r") as file_obj:
        raw_students = json.load(file_obj)

    student_map = {}

    for student_item in raw_students:
        student_map[student_item["id"]] = Student(
            student_item["id"],
            student_item["name"],
            student_item["department"],
            student_item["semester"],
            student_item["marks"]
        )

    return student_map


def load_faculty():
    with open("faculty.json", "r") as file_obj:
        raw_faculty = json.load(file_obj)

    faculty_map = {}

    for faculty_item in raw_faculty:
        faculty_map[faculty_item["id"]] = Faculty(
            faculty_item["id"],
            faculty_item["name"],
            faculty_item["department"],
            faculty_item["salary"]
        )

    return faculty_map


def load_courses(faculty_map_param):
    with open("courses.json", "r") as file_obj:
        raw_courses = json.load(file_obj)

    course_map = {}

    for course_item in raw_courses:
        course_map[course_item["code"]] = Course(
            course_item["code"],
            course_item["name"],
            course_item["credits"],
            faculty_map_param[course_item["faculty_id"]]
        )

    return course_map



# RANKING CORE LOGIC


def build_ranked_list(student_map_param):
    sorted_students = sorted(
        student_map_param.values(),
        key=lambda item_obj: sum(item_obj.marks),
        reverse=True
    )

    ranking_result = []

    for index_value, student_object in enumerate(sorted_students, start=1):
        perf_avg, perf_grade = student_object.fetch_performance()
        ranking_result.append(
            (index_value, student_object, perf_avg, perf_grade)
        )

    return ranking_result



# DISPLAY RANKING


def show_ranking(student_map_param):
    print("\nStudent Ranking")
    print("--------------------------------")

    ranking_data = build_ranked_list(student_map_param)

    for rank_no, ranked_student, rank_avg, rank_grade in ranking_data:
        print(
            f"Rank {rank_no} | {ranked_student.name} | "
            f"Average: {rank_avg:.2f} | Grade: {rank_grade}"
        )



# CSV REPORT


def generate_csv_report(student_map_param):
    ranking_data = build_ranked_list(student_map_param)

    with open("students_report.csv", "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(
            ["Rank", "ID", "Name", "Department", "Average", "Grade"]
        )

        for rank_no, ranked_student, rank_avg, rank_grade in ranking_data:
            writer.writerow(
                [
                    rank_no,
                    ranked_student.id,
                    ranked_student.name,
                    ranked_student.department,
                    round(rank_avg, 2),
                    rank_grade
                ]
            )

    print("CSV Report generated successfully")



# MAIN EXECUTION


student_data_map = load_students()
faculty_data_map = load_faculty()
course_data_map = load_courses(faculty_data_map)

print("Student Performance Report")
print("--------------------------------")

for perf_student in student_data_map.values():
    perf_avg_value, perf_grade_value = perf_student.fetch_performance()
    print(
        f"{perf_student.name} | "
        f"Average: {perf_avg_value:.2f} | Grade: {perf_grade_value}"
    )

show_ranking(student_data_map)

course_list_data = list(course_data_map.values())
if len(course_list_data) >= 2:
    print("\nTotal Credits After Merge :", course_list_data[0] + course_list_data[1])

generate_csv_report(student_data_map)

print("\nThank you for using Smart University Management System")
