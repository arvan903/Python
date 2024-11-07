class Student:
    def __init__(self,name,student_id,grade,is_complete=False):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.is_complete = is_complete

    def add_grade(self,grade):
        self.grade=grade

    def show_grade(self):
        print(f"Your Grade is {self.grade}")

    def get_grade_value(self):
        grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        return grade_mapping.get(self.grade, 0)

    def compelete_course(self):
        self.is_complete=True
        print(f"{self.name} Has Completed The Course.")

   
class Course:
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code
        self.students=[]

    def enroll_student(self,student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in {self.course_name}.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"{student.name} has been removed from {self.course_name}.")
                return
        print(f"Student with ID {student_id} is not found in {self.course_name}.")

    def show_students(self):
        print(f"\nStudents in {self.course_name}")
        if not self.students:
            print("no students enrolled")
        for student in self.students:
            print(f"Name: {student.name} ID: {student.student_id}, Grade: {student.grade}")
    
    def calculate_average_grade(self):
        if not self.students:
            print("No students enrolled to calculate the average grade.")
            return

        total_grade = sum(student.get_grade_value() for student in self.students)
        average_grade = total_grade / len(self.students)
        print(f"The average grade for {self.course_name} is: {average_grade:.2f}")

    def generate_report(self):
        print(f"\nReport for {self.course_name}")
        for student in self.students:
            compelete_status = "Completed" if student.is_complete else "in progress"
            print(f"Name: {student.name}, ID: {student.student_id}, Grade: {student.grade}, Status: {compelete_status} ")



student1 = Student("Rashid", 903, "A")
student2 = Student("Alice", 904, "B")
student3 = Student("John", 905, "C")


course1 = Course("Python Programming", "CS101")


course1.enroll_student(student1)
course1.enroll_student(student2)
course1.enroll_student(student3)


course1.show_students()
course1.calculate_average_grade()
course1.generate_report()

student1.compelete_course()
course1.generate_report()