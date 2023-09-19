numbers = [1, 2, 3, 4, 5, 6, 7]

new_numbers = [number + 2 for number in numbers]

print(new_numbers)

name = "Ahmed"

new_name = [n + "b" for n in name]
print(new_name)

range_1 = range(1,5)

new_range = [n * 2 for n in range_1]

print(new_range)

con_new_numbers = [num * 2 for num in numbers if num > 3]
print(con_new_numbers)
