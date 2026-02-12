#Temperature Converter: Write a Python function called `temperature_converter` that takes a temperature value and a string representing the scale (‘C’ for Celsius or ‘F’ for Fahrenheit) as input. The function should convert the temperature from one scale to the other using nested functions and return the converted value.
def temperature_converter(temp, scale):

    def celsius_to_fahrenheit():
        return (temp * 9/5) + 32

    def fahrenheit_to_celsius():
        return (temp - 32) * 5/9

    if scale.upper() == 'C':
        return celsius_to_fahrenheit()
    elif scale.upper() == 'F':
        return fahrenheit_to_celsius()
    else:
        return "Invalid scale (Use 'C' or 'F')"
# Test the temperature_converter function
print(temperature_converter(25, 'C'))  # Output: 77.0
print(temperature_converter(77, 'F'))  # Output: 25.0
print(temperature_converter(0, 'C'))   # Output: 32.0