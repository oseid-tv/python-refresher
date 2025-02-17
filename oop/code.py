# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student['grades']))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (90, 90, 93, 78, 90))
student2 = Student("Rolf", (100, 95, 90, 75, 85))

print(student.average_grade())
print(student2.average_grade())