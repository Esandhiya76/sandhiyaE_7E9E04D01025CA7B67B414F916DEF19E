class student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  return sorted_students


# Example usage
students =[
  student("Sandhiya", "A123", 7.8),
  student("Janani", "A124", 8.9),
  student("Mohana", "A125", 9.1),
]

sort_students = sort_students(students)

# print the sorted list of students
for student in sort_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
  student.roll_number,     
                                                    student.cgpa))
