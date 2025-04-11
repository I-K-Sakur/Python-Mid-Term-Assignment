class Student:
        def __init__(self,name,age,id):
            self.name = name
            self.age = age
            self.id = id

class StudentDatabase:
    student_list = []
    
    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)

student1 = Student("John Doe", 20, 12345)
student2 = Student("Jane Smith", 22, 67890)

StudentDatabase.add_student(student1)
StudentDatabase.add_student(student2)

for students in StudentDatabase.student_list:
    print(f"Name: {students.name}, Age: {students.age}, ID: {students.id}")