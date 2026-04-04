class Student:

    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.enrolled_courses = []
        self.grades = {}

    def enroll(self, course_code):
        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)
            return True
        return False

    def assign_grade(self, course_code, grade):
        if course_code in self.enrolled_courses:
            self.grades[course_code] = float(grade)
            return True
        return False

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def get_student_info(self):
        return f"{self.name} ({self.student_id}) - Major: {self.major}"


class Professor:

    def __init__(self, prof_id, name, specialization):
        self.prof_id = prof_id
        self.name = name
        self.specialization = specialization
        self.courses_taught = []

    def assign_course(self, course_code):
        if course_code not in self.courses_taught:
            self.courses_taught.append(course_code)
            return True
        return False

    def remove_course(self, course_code):
        if course_code in self.courses_taught:
            self.courses_taught.remove(course_code)
            return True
        return False

    def get_details(self):
        courses = ", ".join(self.courses_taught) if self.courses_taught else "None"
        return f"Prof. {self.name} ({self.specialization}) | Courses: {courses}"

    def has_specialization(self, spec):
        return self.specialization.lower() == spec.lower()


class Course:

    def __init__(self, course_code, title, capacity=30):
        self.course_code = course_code
        self.title = title
        self.capacity = capacity
        self.professor_id = "TBD"
        self.enrolled_students = []

    def set_professor(self, prof_id):
        self.professor_id = prof_id

    def add_student(self, student_id):
        if len(self.enrolled_students) < self.capacity:
            if student_id not in self.enrolled_students:
                self.enrolled_students.append(student_id)
                return True
        return False

    def remove_student(self, student_id):
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False

    def is_full(self):
        return len(self.enrolled_students) >= self.capacity
