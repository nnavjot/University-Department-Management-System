# University Department Management System

## Purpose
This project is a Python-based management system designed to track students, professors, and courses within a university department. It demonstrates Object-Oriented Programming (OOP) principles, modular code structure, and persistent data storage using CSV files.

## Key Features
* **Student Registration:** Add new students with unique IDs and majors.
* **Faculty Management:** Register professors with specific areas of specialization.
* **Course Creation:** Create new courses with defined capacities.
* **Interactive Enrollment:** Enroll students and assign professors to courses using a dynamic menu system.
* **Data Persistence:** All data is automatically saved to and loaded from CSV files (`students.csv` and `courses.csv`).
* **Modular Architecture:** Separated logic for data models, department management, and user interface.

## Project Structure
* `main.py`: The entry point of the application containing the interactive CLI menu.
* `models.py`: Defines the `Student`, `Professor`, and `Course` classes.
* `department.py`: Manages the logic for data handling, saving, and loading.
* `students.csv`: Sample data file for student records.
* `courses.csv`: Sample data file for course and enrollment records.
* `professors.csv`: Sample data file for professor records.

## Installation and Execution
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/nnavjot/University-Department-Management-System.git](https://github.com/nnavjot/University-Department-Management-System.git)
cd University-Department-Management-System
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd University-Department-Management-System
    ```
3.  **Run the Application:**
    Ensure you have Python installed, then run:
    ```bash
    python main.py
    ```

## Example Usage
1.  **Start the program** and select `3` to create a course (e.g., "CS101").
2.  Select `1` to add a student. The system will prompt you for details and then show a list of available courses.
3.  **Choose the number** corresponding to "CS101" to enroll the student immediately.
4.  Select `4` to view the summary and verify the enrollment was successful.
5.  **Exit** the program. Your data is now saved in the `.csv` files and will reload automatically next time you run it.
