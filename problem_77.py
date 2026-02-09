#Dictionary Manipulation: Given a dictionary with student names as keys and their corresponding scores as values, write a Python program to add a new student to the dictionary and update the score of an existing student.
# Initial dictionary
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Add a new student
students["David"] = 88

# Update score of an existing student
students["Bob"] = 82

# Print updated dictionary
print("Updated student scores:")
for name, score in students.items():
    print(name, ":", score)
