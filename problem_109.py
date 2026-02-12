#Greeting Generator: Write a Python function called `greeting_generator` that takes a name as input and returns a greeting message using nested functions. The greeting message should be customizable (e.g., “Hello, {name}! How are you today?”).
def greeting_generator(name):

    def create_message():
        return f"Hello, {name}! How are you today?"

    return create_message()
# Test the greeting_generator function
print(greeting_generator("Shuvo"))
print(greeting_generator("Wife"))

#another way to do it
def greeting_generator(name):

    def create_message():
        return f"Hello, {name}! How are you today?"

    def reply_message():
        return "I am doing well."

    return create_message() + "\n" + reply_message()
# Test the greeting_generator function
print(greeting_generator("Shuvo"))
print(greeting_generator("Wife"))

