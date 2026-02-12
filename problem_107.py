#Leap Year Checker: Write a Python function called `is_leap_year` that takes a year as input and returns `True` if it is a leap year and `False` otherwise. Test the function with different years.
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
# Test the is_leap_year function with different years
print(is_leap_year(2020))  # True
print(is_leap_year(2024))  # True
print(is_leap_year(2000))  # True
print(is_leap_year(2021))  # False
print(is_leap_year(2026))  # False
