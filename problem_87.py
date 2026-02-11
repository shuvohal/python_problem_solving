#Access Nested Dictionary: Given a nested dictionary containing student details, write a Python program to access and print specific information such as a student’s name, age, and address.
# Nested dictionary with student details
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "address": "Dhaka"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "address": "Chittagong"
    }
}

# Access specific information
print("Student1 Name:", students["student1"]["name"])
print("Student1 Age:", students["student1"]["age"])
print("Student2 Address:", students["student2"]["address"])
