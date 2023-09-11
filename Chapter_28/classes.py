class Student:
    def __init__(self, name, major, cgpa, is_on_probation):
        self.student_name = name
        self.major = major
        self.cgpa = cgpa
        self.is_on_probation = is_on_probation

    def distinction(self):
        if self.cgpa > 7.5:
            return True
        else:
            return False


var_student1 = Student("Sayali", "Math", 7, "No")
var_student2 = Student("Pooja", "Science", 8, "No")


print(var_student1.student_name, var_student1.major)
print(var_student2.cgpa)
print(var_student1.is_on_probation)

print(var_student2.distinction())
