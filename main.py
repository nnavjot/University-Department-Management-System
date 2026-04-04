"""
This module provides the interactive terminal interface for the user
to interact with the University Department System.
"""

from models import Student, Professor, Course
from department import Department


def display_menu():
    """Displays the interactive menu choices."""
    print("\n" + "=" * 35)
    print(" UNIVERSITY DEPARTMENT SYSTEM")
    print("=" * 35)
    print("1. Add Student & Enroll")
    print("2. Add Professor & Assign Course")
    print("3. Create New Course")
    print("4. Record Student Grade")
    print("5. View All Records")
    print("6. Exit")
    print("=" * 35)


def select_course(dept):
    """Displays courses as a numbered menu and returns the selected course object."""
    if not dept.courses:
        print("\nNo courses are currently available in the system.")
        return None

    courses_list = list(dept.courses.values())
    
    print("\n--- Available Courses ---")
    for index, course in enumerate(courses_list, 1):
        print(f"{index}. {course.course_code}: {course.title}")
    print(f"{len(courses_list) + 1}. Skip / No Course")
    
    while True:
        choice = input(f"Choose an option (1-{len(courses_list) + 1}): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(courses_list):
                return courses_list[idx - 1]
            elif idx == len(courses_list) + 1:
                return None
        print("Invalid choice. Please pick a number from the list.")


def select_student(dept):
    """Displays students as a numbered menu and returns selected student object."""
    if not dept.students:
        print("\nNo students are currently available in the system.")
        return None

    students_list = list(dept.students.values())
    
    print("\n--- Select Student ---")
    for index, student in enumerate(students_list, 1):
        print(f"{index}. {student.name} ({student.student_id})")
    
    while True:
        choice = input(f"Choose a student (1-{len(students_list)}): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(students_list):
                return students_list[idx - 1]
        print("Invalid choice. Please pick a number from the list.")


def main():
    """Executes the main loop of the terminal application."""
    cs_dept = Department("Computer Science")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Register Student ---")
            id_num = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            major = input("Enter Student Major: ").strip()
            
            student = Student(id_num, name, major)
            
            print("\nWould you like to enroll this student in a course?")
            selected_course = select_course(cs_dept)
            
            if selected_course:
                if selected_course.add_student(student.student_id):
                    student.enroll(selected_course.course_code)
                    print(f"Enrolled in {selected_course.title}!")
                else:
                    print("Could not enroll. Course might be full.")
            
            cs_dept.add_student(student)
            print(f"Student {name} added to the system database.")
            
        elif choice == '2':
            print("\n--- Register Professor ---")
            id_num = input("Enter Professor ID: ").strip()
            name = input("Enter Professor Name: ").strip()
            spec = input("Enter Specialization: ").strip()
            
            prof = Professor(id_num, name, spec)
            
            print("\nWould you like to assign a course to this professor?")
            selected_course = select_course(cs_dept)
            
            if selected_course:
                prof.assign_course(selected_course.course_code)
                selected_course.set_professor(prof.prof_id)
                print(f"Assigned to teach {selected_course.title}!")
                
            cs_dept.add_professor(prof)
            print(f"Professor {name} added to the system database.")
            
        elif choice == '3':
            print("\n--- Create Course ---")
            code = input("Enter Course Code (e.g., CS101): ").strip()
            title = input("Enter Course Title: ").strip()
            cap = input("Enter Capacity (Press Enter for default 30): ").strip()
            
            if cap.isdigit():
                course = Course(code, title, int(cap))
            else:
                course = Course(code, title)
                
            cs_dept.add_course(course)
            print(f"Course '{title}' successfully created and saved.")
            
        elif choice == '4':
            print("\n--- Record Student Grade ---")
            student = select_student(cs_dept)
            if student:
                if not student.enrolled_courses:
                    print(f"{student.name} is not enrolled in any courses yet.")
                    continue
                
                print(f"\nSelect a course to grade for {student.name}:")
                for index, c_code in enumerate(student.enrolled_courses, 1):
                    print(f"{index}. {c_code}")
                
                while True:
                    idx_choice = input(f"Choose option (1-{len(student.enrolled_courses)}): ").strip()
                    if idx_choice.isdigit():
                        idx = int(idx_choice)
                        if 1 <= idx <= len(student.enrolled_courses):
                            selected_course_code = student.enrolled_courses[idx - 1]
                            break
                    print("Invalid option. Try again.")
                
                grade_input = input(f"Enter numeric grade for {selected_course_code} (0-100): ").strip()
                try:
                    grade_val = float(grade_input)
                    student.assign_grade(selected_course_code, grade_val)
                    # Trigger an auto-save because state changed!
                    cs_dept.save_all_data()
                    print(f"Grade of {grade_val}% recorded successfully for {student.name}!")
                except ValueError:
                    print("Invalid grade entered. Must be a number. Aborting grade entry.")
            
        elif choice == '5':
            cs_dept.display_all_records()
            
        elif choice == '6':
            print("Exiting system. All changes have been auto-saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()