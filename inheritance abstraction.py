from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    @abstractmethod
    def calculate_final_score(self):
        pass

    def show_details(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")

class AcademicStudent(Student):
    def __init__(self, student_id, name, exam_marks):
        super().__init__(student_id, name)
        self.exam_marks = exam_marks

    def calculate_final_score(self):
        return sum(self.exam_marks) / len(self.exam_marks)
    
class SportsStudent(Student):
    def __init__(self, student_id, name, exam_marks, sports_score):
        super().__init__(student_id, name)
        self.exam_marks = exam_marks
        self.sport_score = sports_score

    def calculate_final_score(self):
        return sum(self.exam_marks) / len(self.exam_marks)
        return academic_average + self.sports_score
    
class ScholarshipStudent(Student):
    def __init__(self, student_id, name, exam_marks, scholarship_bonus):
        super().__init__(student_id, name)
        self.exam_marks = exam_marks
        self.scholarship_bonus = scholarship_bonus

    def calculate_final_score(self):
        return sum(self.exam_marks) / len(self.exam_marks)
        return academic_average + self.scholarship_bonus
    
students = [
    AcademicStudent(101, "Lisi Twist", [28, 92, 98]),
    AcademicStudent(102, "Jonas Temple", [40, 64, 70]),
    SportsStudent(103, "Ines Woods", [70, 64, 92], 7),
    SportsStudent(104, "Jason White", [90, 51, 49], 8),
    ScholarshipStudent(105, "Emmie Parson", [90, 84, 92], 9),
    ScholarshipStudent(106, "Ollie Taylor", [65, 78, 98], 8),

]

def display_all(student_list):
    print("STUDENT PROGRESS REPORT")
    print("- - - - - - - - - - - - - - - ")
    print("- - - - - - - - - - - - - - - ")
    for student in student_list:
        student.show_details()
        print("FINAL SCORE:", round(student.calculate_final_score(), 2))
        print("- - - - - - - - - - - - - - - ")
        
display_all(students)