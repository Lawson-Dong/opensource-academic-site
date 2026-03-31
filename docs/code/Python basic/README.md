# Python Classes Introduction 🐍

This document provides an introduction to classes in Python, including basic concepts, syntax, and best practices.

## What is a Class?

A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

## Basic Class Syntax

```python
class ClassName:
    # Class attributes
    class_variable = "value"
    
    # Constructor
    def __init__(self, parameter1, parameter2):
        # Instance attributes
        self.instance_variable = parameter1
        self.another_variable = parameter2
    
    # Method
    def method_name(self, parameter):
        # Method body
        return result
```

## Creating Objects

```python
# Create an instance of the class
object = ClassName("value1", "value2")

# Access attributes
print(object.instance_variable)

# Call methods
result = object.method_name("parameter")
```

## Example: A Simple Class

```python
class Person:
    """A class to represent a person"""
    
    # Class attribute
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Initialize a new Person instance"""
        self.name = name
        self.age = age
    
    def greet(self):
        """Return a greeting message"""
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def celebrate_birthday(self):
        """Increase age by 1"""
        self.age += 1
        return f"Happy birthday! I am now {self.age} years old."

# Create instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25
print(Person.species)  # Output: Homo sapiens

# Call methods
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person2.celebrate_birthday())  # Output: Happy birthday! I am now 26 years old.
```

## Class Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create instances
animal = Animal("Generic Animal")
dog = Dog("Rex")
cat = Cat("Whiskers")

print(animal.speak())  # Output: Some generic sound
print(dog.speak())     # Output: Woof!
print(cat.speak())     # Output: Meow!
```

## Special Methods

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    # Special method for string representation
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    # Special method for equality comparison
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
    
    # Special method for addition
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

# Create instances
rect1 = Rectangle(10, 5)
rect2 = Rectangle(10, 5)
rect3 = Rectangle(20, 10)

print(rect1)         # Output: Rectangle(width=10, height=5)
print(rect1.area())  # Output: 50
print(rect1 == rect2)  # Output: True
print(rect1 == rect3)  # Output: False

# Use the __add__ method
rect4 = rect1 + rect3
print(rect4)         # Output: Rectangle(width=30, height=15)
```

## Encapsulation

```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Invalid withdrawal amount."
    
    def get_balance(self):
        return f"Current balance: ${self.__balance}"

# Create instance
account = BankAccount("John Doe", 1000)

print(account.deposit(500))  # Output: Deposited $500. New balance: $1500
print(account.withdraw(200))  # Output: Withdrew $200. New balance: $1300
print(account.get_balance())  # Output: Current balance: $1300

# Trying to access private attribute directly (will not work)
# print(account.__balance)  # This will raise an AttributeError
```

## Class Methods and Static Methods

```python
class Math:
    # Class attribute
    pi = 3.14159
    
    @classmethod
    def circle_area(cls, radius):
        """Calculate the area of a circle"""
        return cls.pi * radius ** 2
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b

# Use class method
area = Math.circle_area(5)
print(f"Area of circle with radius 5: {area}")  # Output: Area of circle with radius 5: 78.53975

# Use static method
sum_result = Math.add(10, 20)
print(f"Sum of 10 and 20: {sum_result}")  # Output: Sum of 10 and 20: 30
```

## Python Functions

### What is a Function?

A function is a block of organized, reusable code that performs a specific task. Functions help break down complex problems into smaller, manageable parts and promote code reusability.

### Function Syntax

```python
def function_name(parameter1, parameter2, ...):
    """Docstring: describes what the function does"""
    # Function body
    # Perform operations
    return result  # Optional return statement
```

### Parameters vs. Arguments

- **Parameters**: Variables defined in the function signature (e.g., `parameter1` in `def function_name(parameter1):`)
- **Arguments**: Actual values passed to the function when it's called (e.g., `5` in `function_name(5)`)

### Types of Parameters

#### 1. Positional Parameters

Positional parameters are the most basic type of parameters. They are passed to the function in the order they are defined.

```python
def add(a, b):
    """Add two numbers"""
    return a + b

# Calling with positional arguments
result = add(5, 3)  # a=5, b=3
print(result)  # Output: 8
```

#### 2. Default Parameters

Default parameters have a predefined value that is used if no argument is provided. They must come after positional parameters.

```python
def greet(name, greeting="Hello"):
    """Greet a person with a customizable greeting"""
    return f"{greeting}, {name}!"

# Using default value for greeting
print(greet("Alice"))  # Output: Hello, Alice!

# Overriding the default value
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
```

#### 3. Keyword Arguments

Keyword arguments allow you to pass arguments by name, regardless of order. This improves code readability.

```python
def describe_person(name, age, city):
    """Describe a person"""
    return f"{name} is {age} years old and lives in {city}."

# Using keyword arguments
print(describe_person(name="Alice", age=30, city="New York"))
# Output: Alice is 30 years old and lives in New York.

# Order doesn't matter with keyword arguments
print(describe_person(city="London", name="Bob", age=25))
# Output: Bob is 25 years old and lives in London.
```

#### 4. Variable-Length Parameters

Variable-length parameters allow functions to accept an arbitrary number of arguments.

##### *args (Arbitrary Positional Arguments)

`*args` collects extra positional arguments into a tuple.

```python
def sum_numbers(*args):
    """Sum any number of positional arguments"""
    return sum(args)

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(10, 20, 30, 40))  # Output: 100
```

##### **kwargs (Arbitrary Keyword Arguments)

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def print_info(**kwargs):
    """Print keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```

#### 5. Mixing Parameter Types

You can combine different parameter types, but they must follow this order:
1. Positional parameters
2. Default parameters
3. *args
4. **kwargs

```python
def mixed_params(a, b, c=10, *args, **kwargs):
    """Demonstrate mixed parameter types"""
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed_params(1, 2, 3, 4, 5, 6, x=10, y=20)
# Output:
# a: 1, b: 2, c: 3
# args: (4, 5, 6)
# kwargs: {'x': 10, 'y': 20}
```

#### 6. Parameter Unpacking

You can unpack sequences and dictionaries when passing arguments to functions.

```python
# Unpacking a list/tuple as positional arguments
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # Output: 6

# Unpacking a dictionary as keyword arguments
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

person_info = {"name": "Alice", "age": 30, "city": "New York"}
print(describe_person(**person_info))
# Output: Alice is 30 years old and lives in New York.
```

#### 7. Type Hints

Python 3.5+ supports type hints, which make code more readable and help with static analysis.

```python
def greet(name: str, age: int) -> str:
    """Greet a person with their name and age"""
    return f"Hello, {name}! You are {age} years old."

print(greet("Alice", 30))  # Output: Hello, Alice! You are 30 years old.

# Type hints for collections from typing module
from typing import List, Dict, Optional

def process_numbers(numbers: List[int]) -> List[int]:
    """Process a list of numbers"""
    return [num * 2 for num in numbers]

def get_person_info(name: str) -> Optional[Dict[str, str]]:
    """Get person information or None if not found"""
    if name == "Alice":
        return {"city": "New York", "country": "USA"}
    return None
```

### Return Statement

The `return` statement is used to exit a function and optionally return a value to the caller:

```python
def calculate_area(length, width):
    area = length * width
    return area  # Return the calculated area

# Function without return statement (returns None implicitly)
def print_greeting(name):
    print(f"Hello, {name}!")

# Returning multiple values (as a tuple)
def get_min_max(numbers):
    return min(numbers), max(numbers)
```

### Function Examples

```python
# Basic function
def square(n):
    """Calculate the square of a number"""
    return n * n

# Function with default parameter
def power(base, exponent=2):
    """Calculate base raised to the given exponent"""
    return base ** exponent

# Function with keyword arguments
def create_user(name, email, age=18):
    """Create a user dictionary"""
    return {
        "name": name,
        "email": email,
        "age": age
    }

# Using the functions
print(square(5))  # Output: 25
print(power(2, 3))  # Output: 8
print(power(3))  # Output: 9 (uses default exponent=2)

user = create_user(name="Alice", email="alice@example.com")
print(user)  # Output: {'name': 'Alice', 'email': 'alice@example.com', 'age': 18}

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {min_val}, Max: {max_val}")  # Output: Min: 1, Max: 9
```

### Best Practices for Functions

1. **Use meaningful function names** (snake_case)
2. **Use docstrings** to document what the function does
3. **Keep functions focused** on a single task
4. **Use appropriate parameter types** and defaults
5. **Return meaningful values** (avoid side effects when possible)
6. **Handle edge cases** and invalid inputs
7. **Keep functions short** and readable

## Function Nesting

Function nesting refers to two related concepts: **nested calling** (calling one function inside another) and **nested definition** (defining a function inside another function).

### 1. Nested Calling (Function Composition)

Nested calling is when one function is called inside another function call. This is also known as function composition.

#### Basic Nested Calling

```python
def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

# Nested calling: multiply is called with the result of add
result = multiply(add(2, 3), 4)
print(result)  # Output: 20 (equivalent to (2+3)*4)

# More complex nesting
result = add(multiply(2, 3), multiply(4, 5))
print(result)  # Output: 26 (equivalent to (2*3)+(4*5))
```

#### Practical Examples of Nested Calling

```python
# Example 1: String manipulation
message = "Hello, World!".upper().replace("WORLD", "Python").strip()
print(message)  # Output: HELLO, PYTHON!

# Example 2: Math operations
import math
result = math.sqrt(math.pow(3, 2) + math.pow(4, 2))
print(result)  # Output: 5.0 (Pythagorean theorem: sqrt(3² + 4²))

# Example 3: List operations
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum([x**2 for x in numbers if x % 2 == 0])
print(sum_of_squares)  # Output: 20 (2² + 4²)
```

### 2. Nested Definition (Inner Functions)

Nested definition is when a function is defined inside another function. These inner functions have access to variables from the outer function's scope (closure).

#### Basic Nested Definition

```python
def outer_function(x):
    """Outer function that defines an inner function"""
    def inner_function(y):
        """Inner function that uses variable from outer scope"""
        return x + y  # Inner function can access x from outer scope
    
    return inner_function  # Return the inner function

# Create a closure
add_five = outer_function(5)

# Use the closure
print(add_five(3))  # Output: 8
print(add_five(10))  # Output: 15
```

#### Practical Example: Counter

```python
def create_counter():
    """Create a counter function that maintains state"""
    count = 0  # This variable is in the outer function's scope
    
    def counter():
        nonlocal count  # Declare that we want to modify the outer variable
        count += 1
        return count
    
    return counter

# Create a counter instance
my_counter = create_counter()

# Use the counter
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3

# Create another counter instance (maintains its own state)
another_counter = create_counter()
print(another_counter())  # Output: 1
```

#### More Nested Definition Examples

##### Example 1: Factory Function

```python
def create_multiplier(factor):
    """Create a function that multiplies by a given factor"""
    def multiplier(number):
        return number * factor
    return multiplier

# Create multiplier functions
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

##### Example 2: Decorator Pattern

```python
def log_function(func):
    """Decorator that logs function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

@log_function
def greet(name):
    return f"Hello, {name}!"

# Test the decorated functions
print(add(5, 3))  # Will print logging information
print(greet("Alice"))  # Will print logging information
```

##### Example 3: Data Validation

```python
def create_validator(min_value, max_value):
    """Create a validator function for a specific range"""
    def validate(value):
        if value < min_value:
            return f"Value {value} is below minimum {min_value}"
        elif value > max_value:
            return f"Value {value} is above maximum {max_value}"
        else:
            return f"Value {value} is valid"
    return validate

# Create validators
validate_age = create_validator(0, 120)
validate_score = create_validator(0, 100)

print(validate_age(25))  # Output: Value 25 is valid
print(validate_age(150))  # Output: Value 150 is above maximum 120
print(validate_score(95))  # Output: Value 95 is valid
```

## Python Data Structures

### Lists

A list is a mutable sequence of elements. It is defined using square brackets `[]` and is one of the most commonly used data structures in Python.

#### List Creation and Access

```python
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access elements by index
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

# Access a range of elements (slicing)
print(fruits[0:2])  # Output: ['apple', 'banana']
print(fruits[1:])  # Output: ['banana', 'cherry']
print(fruits[:2])  # Output: ['apple', 'banana']

# List unpacking
a, b, c = fruits
print(a, b, c)  # Output: apple banana cherry
```

#### List Operations

```python
# Create lists
numbers = [1, 2, 3, 4, 5]
more_numbers = [6, 7, 8, 9, 10]

# Concatenation
combined = numbers + more_numbers
print(combined)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Repetition
repeated = ["Hello"] * 3
print(repeated)  # Output: ['Hello', 'Hello', 'Hello']

# Membership check
print(3 in numbers)  # Output: True
print(10 in numbers)  # Output: False

# Length
print(len(numbers))  # Output: 5

# Maximum and minimum
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1

# Sum
print(sum(numbers))  # Output: 15
```

#### List Methods

```python
# Create a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Append an element
numbers.append(7)
print(numbers)  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 7]

# Insert an element at a specific position
numbers.insert(0, 0)
print(numbers)  # Output: [0, 3, 1, 4, 1, 5, 9, 2, 6, 7]

# Remove an element by value
numbers.remove(1)  # Removes the first occurrence of 1
print(numbers)  # Output: [0, 3, 4, 1, 5, 9, 2, 6, 7]

# Pop an element (default: last)
popped = numbers.pop()
print(f"Popped: {popped}, List: {numbers}")  # Output: Popped: 7, List: [0, 3, 4, 1, 5, 9, 2, 6]

# Pop from a specific index
popped_at_2 = numbers.pop(2)
print(f"Popped at index 2: {popped_at_2}, List: {numbers}")  # Output: Popped at index 2: 4, List: [0, 3, 1, 5, 9, 2, 6]

# Clear the list
numbers.clear()
print(numbers)  # Output: []

# Recreate the list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Count occurrences
print(numbers.count(1))  # Output: 2

# Find index of an element
print(numbers.index(5))  # Output: 4

# Sort the list
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse the list
numbers.reverse()
print(numbers)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# Create a copy
numbers_copy = numbers.copy()
print(numbers_copy)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]
```

#### List Comprehensions

List comprehensions provide a concise way to create lists.

```python
# Basic list comprehension: squares of numbers 0-9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension with condition: even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# Nested list comprehension: matrix transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# List comprehension with transformation
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']
```

### Tuples

A tuple is an immutable sequence of elements. It is defined using parentheses `()`. Once created, tuples cannot be modified.

#### Tuple Creation and Access

```python
# Create a tuple
fruits = ("apple", "banana", "cherry")

# Access elements by index
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

# Tuple unpacking
a, b, c = fruits
print(a, b, c)  # Output: apple banana cherry

# Single element tuple (note the comma)
single_element = (42,)
print(type(single_element))  # Output: <class 'tuple'>

# Tuple operations
combined = fruits + ("date", "elderberry")
print(combined)  # Output: ('apple', 'banana', 'cherry', 'date', 'elderberry')

repeated = fruits * 2
print(repeated)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Tuple methods
print(fruits.count("apple"))  # Output: 1
print(fruits.index("banana"))  # Output: 1
```

### Dictionaries

A dictionary is a collection of key-value pairs. It is defined using curly braces `{}` and is mutable.

#### Dictionary Creation and Access

```python
# Create a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access values by key
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 30

# Use get() to handle missing keys
print(person.get("country", "Unknown"))  # Output: Unknown

# Add or update key-value pairs
person["country"] = "USA"
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Remove items
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

# Dictionary methods
print(person.keys())  # Output: dict_keys(['name', 'age', 'country'])
print(person.values())  # Output: dict_values(['Alice', 31, 'USA'])
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('country', 'USA')])
```

#### Dictionary Comprehensions

```python
# Create a dictionary from a list
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter items
even_squares = {num: num**2 for num, square in squares.items() if num % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16}
```

## Best Practices for Classes

1. **Use meaningful class names** (CamelCase)
2. **Use docstrings** to document classes and methods
3. **Keep classes focused** on a single responsibility
4. **Use private attributes** for internal state
5. **Follow the DRY principle** (Don't Repeat Yourself)
6. **Use inheritance appropriately**
7. **Implement special methods** for better usability
8. **Test your classes** thoroughly

## Advanced Concepts

- **Abstract Base Classes (ABCs)**
- **Multiple Inheritance**
- **Method Resolution Order (MRO)**
- **Property Decorators**
- **Descriptors**
- **Metaclasses**

## Further Reading

- [Python Official Documentation on Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python Wiki: Python Style Guide](https://wiki.python.org/moin/StyleGuide)

---

*Mastering classes is essential for writing clean, organized, and reusable Python code!* 🚀