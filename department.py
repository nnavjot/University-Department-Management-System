"""
This module contains the Department class, which manages the collections
of students, professors, and courses, and handles automated CSV interactions.
"""

import csv
import os
from models import Student, Professor, Course


class Department:
    """Manages students, professors, and courses within a department."""

    def __init__(self, dept_name):
        """Initializes the department and automatically loads existing data."""
        self.dept_name = dept_name
        self.students = {}
        self.professors = {}
        self.courses = {}
        
        # Files for auto-saving
        self.students_file = "students.csv"
        self.professors_file = "professors.csv"
        self.courses_file = "courses.csv"
        
        # Load data on system start
        self.load_all_data()

    def add_student(self, student):
        """Adds a student and triggers auto-save."""
        self.students[student.student_id] = student
        self.save_all_data()

    def add_professor(self, professor):
        """Adds a professor and triggers auto-save."""
        self.professors[professor.prof_id] = professor
        self.save_all_data()

    def add_course(self, course):
        """Adds a course and triggers auto-save."""
        self.courses[course.course_code] = course
        self.save_all_data()

    def save_all_data(self):
        """Saves all records to CSV files automatically.
        
        Fulfills both Data Handling and Exception Handling requirements.
        """
        try:
            # Save Students (Grades saved as CS101:85|CS102:90)
            with open(self.students_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Name', 'Major', 'EnrolledCourses', 'Grades'])
                for s in self.students.values():
                    grades_str = "|".join([f"{c}:{g}" for c, g in s.grades.items()])
                    writer.writerow([s.student_id, s.name, s.major, ",".join(s.enrolled_courses), grades_str])

            # Save Professors
            with open(self.professors_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Name', 'Specialization', 'CoursesTaught'])
                for p in self.professors.values():
                    writer.writerow([p.prof_id, p.name, p.specialization, ",".join(p.courses_taught)])

            # Save Courses
            with open(self.courses_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Code', 'Title', 'Capacity', 'ProfID', 'Students'])
                for c in self.courses.values():
                    writer.writerow([c.course_code, c.title, c.capacity, c.professor_id, ",".join(c.enrolled_students)])

        except IOError as error:
            print(f"\n[System Error] Could not auto-save data: {error}")

    def load_all_data(self):
        """Loads all records from CSV files on startup if they exist."""
        try:
            # Load Courses first
            if os.path.exists(self.courses_file):
                with open(self.courses_file, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        course = Course(row.get('Code', ''), row.get('Title', ''), int(row.get('Capacity', 30)))
                        course.professor_id = row.get('ProfID', 'TBD')
                        students_data = row.get('Students', '')
                        if students_data:
                            course.enrolled_students = students_data.split(',')
                        self.courses[course.course_code] = course

            # Load Students
            if os.path.exists(self.students_file):
                with open(self.students_file, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        student = Student(row.get('ID', ''), row.get('Name', ''), row.get('Major', ''))
                        
                        courses_data = row.get('EnrolledCourses', '')
                        if courses_data:
                            student.enrolled_courses = courses_data.split(',')
                        
                        grades_data = row.get('Grades', '')
                        if grades_data:
                            for grade_pair in grades_data.split('|'):
                                if ':' in grade_pair:
                                    course_code, grade_val = grade_pair.split(':')
                                    student.grades[course_code] = float(grade_val)
                                    
                        self.students[student.student_id] = student

            # Load Professors
            if os.path.exists(self.professors_file):
                with open(self.professors_file, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        prof = Professor(row.get('ID', ''), row.get('Name', ''), row.get('Specialization', ''))
                        courses_taught = row.get('CoursesTaught', '')
                        if courses_taught:
                            prof.courses_taught = courses_taught.split(',')
                        self.professors[prof.prof_id] = prof

            print("\n[System] Existing database loaded successfully.")
            
        except IOError as error:
            print(f"\n[System Error] Could not load database files: {error}")

    def display_all_records(self):
        """Displays a comprehensive summary and detailed view of all records."""
        print("\n" + "=" * 50)
        print(f" {self.dept_name.upper()} DEPARTMENT DATABASE")
        print("=" * 50)
        
        print(f"Total Students:   {len(self.students)}")
        print(f"Total Faculty:    {len(self.professors)}")
        print(f"Total Courses:    {len(self.courses)}")
        print("=" * 50)
        
        # 1. Courses
        print("\n[ COURSES ]")
        if not self.courses:
            print("  No courses registered.")
        for course in self.courses.values():
            prof_name = "TBD"
            if course.professor_id in self.professors:
                prof_name = self.professors[course.professor_id].name
            
            print(f"  • {course.course_code}: {course.title}")
            print(f"    Instructor: {prof_name}")
            print(f"    Capacity:   {course.capacity}")
            print()

        # 2. Students
        print("[ STUDENTS ]")
        if not self.students:
            print("  No students registered.")
        for student in self.students.values():
            print(f"  • ID: {student.student_id} | Name: {student.name}")
            print(f"    Major:    {student.major}")
            if student.enrolled_courses:
                print(f"    Enrolled: {', '.join(student.enrolled_courses)}")
            if student.grades:
                grades_list = [f"{c}: {g}%" for c, g in student.grades.items()]
                print(f"    Grades:   {', '.join(grades_list)}")
                print(f"    Avg GPA:  {student.calculate_gpa():.1f}%")
            print()

        # 3. Professors
        print("[ PROFESSORS ]")
        if not self.professors:
            print("  No professors registered.")
        for prof in self.professors.values():
            print(f"  • ID: {prof.prof_id} | Name: {prof.name}")
            print(f"    Specialization: {prof.specialization}")
            if prof.courses_taught:
                print(f"    Teaching:       {', '.join(prof.courses_taught)}")
            print()
            
        print("=" * 50)