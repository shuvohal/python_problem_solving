#Nested Dictionary Update: Given a nested dictionary of employee details, write a Python program to update an employee’s salary based on their employee ID.
# Nested dictionary of employee details
employees = {
    "E101": {
        "name": "Alice",
        "salary": 50000,
        "department": "HR"
    },
    "E102": {
        "name": "Bob",
        "salary": 60000,
        "department": "IT"
    }
}

emp_id = input("Enter Employee ID: ")
new_salary = int(input("Enter New Salary: "))

if emp_id in employees:
    employees[emp_id]["salary"] = new_salary
    print("Salary updated successfully!")
else:
    print("Employee ID not found.")

print("\nUpdated Employee Data:")
for emp, details in employees.items():
    print(emp, ":", details)
