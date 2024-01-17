# Gradebook

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Task 1 & 2
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Task 3
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Task 4
print(gradebook)

# Task 5 & 6
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# print to check
# print(gradebook)

# Modifying The Gradebook
# Task 7, 8, & 9
gradebook[5][1] = 98
gradebook[2].remove(gradebook[2][1])
gradebook[2].append("Pass")

# print to check
# print(gradebook)

# One Big Gradebook!
# Task 10
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
