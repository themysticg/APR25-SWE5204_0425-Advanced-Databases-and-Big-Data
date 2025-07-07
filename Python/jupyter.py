# Python Basics Tutorial

# 1. Printing to the Console
print("Hello, World!")

# 2. Variables and Data Types
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

print(name, age, height, is_student)

# 3. Conditional Statements
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 4. Loops
# For loop
for i in range(5):
    print(f"Iteration {i}")

# While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# 5. Functions
def greet(person_name):
    return f"Hello, {person_name}!"

print(greet("Bob"))

# 6. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)

# 7. Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])

# 8. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 25)
print(person1.introduce())

# 9. File Handling
with open("example.txt", "w") as file:
    file.write("This is a sample file.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 10. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")