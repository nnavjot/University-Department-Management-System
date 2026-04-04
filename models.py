"""
This module contains the basic model classes for the University Department System.
It defines Student, Professor, and Course entities.
"""

class Student:
    """Represents a student at the university."""

    def __init__(self, student_id, name, major):
        """Initializes a student with an ID, name, and major."""
        self.student_id = student_id
        self.name = name
        self.major = major
        self.enrolled_courses = []
        self.grades = {}  # Format: {'CS101': 85.0}

    def enroll(self, course_code):
        """Enrolls the student in a specific course."""
        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)
            return True
        return False

    def assign_grade(self, course_code, grade):
        """Assigns a numeric grade to the student for a course."""
        if course_code in self.enrolled_courses:
            self.grades[course_code] = float(grade)
            return True
        return False

    def calculate_gpa(self):
        """Calculates a simple numeric grade average."""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def get_student_info(self):
        """Returns a summarized string of student details."""
        return f"{self.name} ({self.student_id}) - Major: {self.major}"


class Professor:
    """Represents a faculty professor at the university."""

    def __init__(self, prof_id, name, specialization):
        """Initializes a professor with an ID, name, and specialization."""
        self.prof_id = prof_id
        self.name = name
        self.specialization = specialization
        self.courses_taught = []

    def assign_course(self, course_code):
        """Assigns a course to the professor's schedule."""
        if course_code not in self.courses_taught:
            self.courses_taught.append(course_code)
            return True
        return False

    def remove_course(self, course_code):
        """Removes a course from the professor's schedule."""
        if course_code in self.courses_taught:
            self.courses_taught.remove(course_code)
            return True
        return False

    def get_details(self):
        """Returns a formatted string containing the professor's details."""
        courses = ", ".join(self.courses_taught) if self.courses_taught else "None"
        return f"Prof. {self.name} ({self.specialization}) | Courses: {courses}"

    def has_specialization(self, spec):
        """Checks if the professor specializes in a specific area."""
        return self.specialization.lower() == spec.lower()


class Course:
    """Represents a course offered by the university."""

    def __init__(self, course_code, title, capacity=30):
        """Initializes a course with a code, title, and max capacity."""
        self.course_code = course_code
        self.title = title
        self.capacity = capacity
        self.professor_id = "TBD"
        self.enrolled_students = []

    def set_professor(self, prof_id):
        """Assigns a professor to the course by ID."""
        self.professor_id = prof_id

    def add_student(self, student_id):
        """Enrolls a student if there is capacity and they are not already in it."""
        if len(self.enrolled_students) < self.capacity:
            if student_id not in self.enrolled_students:
                self.enrolled_students.append(student_id)
                return True
        return False

    def remove_student(self, student_id):
        """Removes a student from the course by ID."""
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False

    def is_full(self):
        """Checks if the course has reached its full capacity."""
        return len(self.enrolled_students) >= self.capacity