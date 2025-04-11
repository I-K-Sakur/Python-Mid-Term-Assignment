class Student:
    __student_list = []

    def __init__(self, student_id, name, department, is_enrolled=True):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def is_enrolled(self):
        return self.__is_enrolled

    def drop_out(self):
        self.__is_enrolled = False

    def view_student_info(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}"

    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)

    @classmethod
    def get_all_students(cls):
        return cls.__student_list

    @classmethod
    def find_student_by_id(cls, student_id):
        for student in cls.__student_list:
            if student.get_id() == student_id:
                return student
        return None

    @classmethod
    def enroll_student(cls, student_id, name, department):
        existing = cls.find_student_by_id(student_id)
        if existing:
            if existing.is_enrolled():
                print("Student is already enrolled.")
            else:
                existing.__is_enrolled = True
                print("Student re-enrolled.")
        else:
            new_student = Student(student_id, name, department, True)
            cls.add_student(new_student)
            print("New student enrolled.")

    @classmethod
    def drop_student(cls, student_id):
        student = cls.find_student_by_id(student_id)
        if student:
            if not student.is_enrolled():
                print("Student already dropped.")
            else:
                student.drop_out()
                print(f"Student with ID {student_id} dropped.")
        else:
            print("Student ID not found.")
# Sample students
student1 = Student(1, "Sakur", "Computer Science", True)
student2 = Student(2, "Kabir", "Mathematics", False)
student3 = Student(3, "Iftakhar", "Physics", True)

Student.add_student(student1)
Student.add_student(student2)
Student.add_student(student3)

while True:
    print("\n--- Student Database Menu ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")   
        
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        print("\n--- All Students ---")
        for student in Student.get_all_students():
            print(student.view_student_info())
    elif choice =='2':
        try:
            student_id = int(input("Enter Student ID: "))
            if student_id < 0:
                raise ValueError("Student ID cannot be negative.")
            name = input("Enter Student Name: ")
            department = input("Enter Student Department: ")
            is_enrolled = input("Is the student enrolled? (True/False): ")
            Student.enroll_student(student_id, name, department)
            print("Student enrolled successfully!")
        except ValueError as ve:
            print("Invalid input:", ve)
    
    elif choice == '3':
        try:
            student_id = int(input("Enter Student ID: "))
            Student.drop_out(student_id)
        except ValueError as ve:
            print("Invalid input:", ve)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

    
    
