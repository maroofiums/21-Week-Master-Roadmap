class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
        
student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 22, 72)
student3 = Student("Charlie", 19, 55)

students = [student1, student2, student3]

for student in students:
    grade = student.calculate_grade()
    print(f"{student.name} (Age: {student.age}) - Marks: {student.marks}, Grade: {grade}")

class CollageStudent(Student):
    def __init__(self, name, age, marks, collage_name):
        super().__init__(name, age, marks)
        self.collage_name = collage_name


c_student1 = CollageStudent("David", 21, 88, "XYZ University")
print(f"{c_student1.name} (Age: {c_student1.age}) - Marks: {c_student1.marks}, Grade: {c_student1.calculate_grade()}, Collage: {c_student1.collage_name}")

