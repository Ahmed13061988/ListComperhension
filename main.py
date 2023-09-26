import random
import pandas

# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# new_numbers = [number + 2 for number in numbers]
#
# print(new_numbers)
#
# name = "Ahmed"
#
# new_name = [n + "b" for n in name]
# print(new_name)
#
# range_1 = range(1,5)
#
# new_range = [n * 2 for n in range_1]
#
# print(new_range)
#
# con_new_numbers = [num * 2 for num in numbers if num > 3]
# print(con_new_numbers)

# names = ["Ahmed", "Ali", "Hussein", "Atyaf", "Salwa", "Rami"]
#
# # cap_case_names = [name.upper() for name in names if len(name) > 3]
# # print(cap_case_names)
# new_dict = {student: random.randint(1, 100) for student in names}
#
# passed_students = {student: score for (student, score) in new_dict.items() if score > 50}
# print(passed_students)

student_dict = {
    "student": ["Ahmed", "Rami", "Atyaf"],
    "score": [90, 100, 70]
}

for (key, value) in student_dict.items():
    for val in value:
        print()

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)
