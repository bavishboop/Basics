"""
Advanced Python Concepts Module
Covers advanced topics essential for DSA and professional development
"""

class AdvancedPythonModule:
    def __init__(self):
        self.name = "Advanced Python Concepts"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 ADVANCED PYTHON CONCEPTS")
        print("="*60)
        
        print("\n🔹 LIST COMPREHENSIONS & GENERATORS:")
        print("• List comprehensions: Concise list creation")
        print("• Generator expressions: Memory-efficient iteration")
        print("• Generator functions: Yield values lazily")
        print("• Decorators: Modify function behavior")
        
        print("\n🔹 FUNCTIONAL PROGRAMMING:")
        print("• map(): Apply function to all elements")
        print("• filter(): Filter elements based on condition")
        print("• reduce(): Apply function cumulatively")
        print("• Lambda functions: Anonymous functions")
        print("• Higher-order functions: Functions as arguments")
        
        print("\n🔹 ERROR HANDLING & EXCEPTIONS:")
        print("• try-except blocks: Handle exceptions")
        print("• Custom exceptions: Create your own errors")
        print("• finally block: Cleanup code")
        print("• raise statement: Trigger exceptions")
        print("• Context managers: with statements")
        
        print("\n🔹 FILE I/O OPERATIONS:")
        print("• Reading files: read(), readline(), readlines()")
        print("• Writing files: write(), writelines()")
        print("• File modes: 'r', 'w', 'a', 'b', '+'")
        print("• Context managers: with open()")
        print("• CSV, JSON handling")
        
        print("\n🔹 WORKING WITH MODULES:")
        print("• Import statements: import, from...import")
        print("• Standard library: os, sys, math, random")
        print("• Third-party packages: pip install")
        print("• Virtual environments: venv")
        print("• Package structure: __init__.py")
        
        print("\n🔹 DEBUGGING & TESTING:")
        print("• print() debugging: Simple but effective")
        print("• assert statements: Check conditions")
        print("• pdb module: Python debugger")
        print("• Unit testing: unittest, pytest")
        print("• Code profiling: time, timeit")
        
        print("\n🔹 MEMORY MANAGEMENT:")
        print("• Garbage collection: Automatic memory management")
        print("• Reference counting: Object lifecycle")
        print("• Memory profiling: tracemalloc")
        print("• Efficient data structures: generators vs lists")
        
        print("\n🔹 MULTITHREADING & CONCURRENCY:")
        print("• threading module: Basic threading")
        print("• Concurrent execution: Multiple tasks")
        print("• Synchronization: Locks, semaphores")
        print("• Global Interpreter Lock (GIL)")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 List Comprehensions:")
        print("""
# Basic list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
        """)
        
        print("\n🔹 Generator Functions:")
        print("""
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using generator
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34

# Generator expression
squares_gen = (x**2 for x in range(5))
print(list(squares_gen))  # [0, 1, 4, 9, 16]
        """)
        
        print("\n🔹 Decorators:")
        print("""
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

# Using decorated function
result = slow_function()  # Prints execution time
        """)
        
        print("\n🔹 Functional Programming:")
        print("""
numbers = [1, 2, 3, 4, 5]

# map: Apply function to all elements
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter: Filter elements
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]

# reduce: Cumulative operation
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# List comprehension alternative
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
        """)
        
        print("\n🔹 Exception Handling:")
        print("""
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Both arguments must be numbers!")
        return None
    finally:
        print("Division attempt completed")

# Custom exception
class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number")
    return x ** 0.5

# Test exception handling
print(divide_numbers(10, 2))   # 5.0
print(divide_numbers(10, 0))   # None with error message

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print(f"Error: {e}")
        """)
        
        print("\n🔹 File Operations:")
        print("""
# Reading files
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Writing files
with open('output.txt', 'w') as file:
    file.write("Hello, World!\\n")
    file.write("This is a test file.\\n")

# Appending to files
with open('output.txt', 'a') as file:
    file.write("This line is appended.\\n")

# Working with JSON
import json

data = {
    "name": "John",
    "age": 30,
    "courses": ["Math", "Science", "English"]
}

# Write JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

# Read JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)
        """)
        
        print("\n🔹 Working with Modules:")
        print("""
# Importing modules
import math
import random
from datetime import datetime, timedelta

# Using math module
print(math.pi)           # 3.14159...
print(math.sqrt(16))      # 4.0
print(math.factorial(5))  # 120

# Using random module
print(random.randint(1, 10))     # Random integer 1-10
print(random.choice(['a', 'b', 'c']))  # Random choice
print(random.shuffle([1, 2, 3, 4]))  # Shuffle list

# Using datetime
now = datetime.now()
print(f"Current time: {now}")
future = now + timedelta(days=7)
print(f"One week later: {future}")
        """)
        
        print("\n🔹 Context Managers:")
        print("""
class Timer:
    def __init__(self):
        self.start_time = None
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start_time
        print(f"Elapsed time: {elapsed:.4f} seconds")

# Using custom context manager
with Timer():
    # Some operation
    import time
    time.sleep(0.5)
# Prints elapsed time
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nExercise 1: Create a data processing pipeline")
        print("Use functional programming to process a list of numbers")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def process_numbers(numbers):
    # Filter out negative numbers
    positive = filter(lambda x: x > 0, numbers)
    
    # Square each number
    squared = map(lambda x: x**2, positive)
    
    # Keep only squares less than 100
    filtered = filter(lambda x: x < 100, squared)
    
    # Convert to list and sort
    result = sorted(list(filtered))
    
    return result

# Alternative using list comprehensions
def process_numbers_comprehension(numbers):
    return sorted([x**2 for x in numbers if x > 0 and x**2 < 100])

# Test
numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 10, 11]
print(process_numbers(numbers))              # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(process_numbers_comprehension(numbers)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]
        """)
        
        print("\nExercise 2: Create a file processor with error handling")
        print("Write a function to read, process, and write files safely")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def process_file(input_file, output_file):
    try:
        # Read input file
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Process lines (remove empty lines and strip whitespace)
        processed_lines = [line.strip() for line in lines if line.strip()]
        
        # Add line numbers
        numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(processed_lines)]
        
        # Write to output file
        with open(output_file, 'w') as f:
            f.write('\\n'.join(numbered_lines))
        
        print(f"Processed {len(processed_lines)} lines")
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        return False
    except PermissionError:
        print(f"Error: Permission denied")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Test the function (assuming you have a file to test with)
# success = process_file('input.txt', 'output.txt')
        """)
        
        print("\nExercise 3: Create a caching decorator")
        print("Write a decorator that caches function results")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def cache_decorator(func):
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print("Returning cached result")
            return cache[key]
        
        # Compute and cache result
        result = func(*args, **kwargs)
        cache[key] = result
        print("Computed and cached result")
        return result
    
    return wrapper

@cache_decorator
def expensive_function(n):
    print(f"Computing expensive operation for {n}")
    import time
    time.sleep(1)  # Simulate expensive operation
    return n * n

# Test the decorator
print(expensive_function(5))  # Computes and caches
print(expensive_function(5))  # Returns cached result
print(expensive_function(10)) # Computes and caches
print(expensive_function(10)) # Returns cached result
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "What is the main advantage of generators over lists?",
                "options": ["a) They are faster", "b) They use less memory", "c) They are easier to read", "d) They support more operations"],
                "answer": "b"
            },
            {
                "question": "Which statement is used to trigger an exception?",
                "options": ["a) throw", "b) raise", "c) except", "d) error"],
                "answer": "b"
            },
            {
                "question": "What does the map() function do?",
                "options": ["a) Filters elements", "b) Applies function to all elements", "c) Reduces to single value", "d) Sorts elements"],
                "answer": "b"
            },
            {
                "question": "Which is the correct way to open a file safely?",
                "options": ["a) file = open('file.txt')", "b) with open('file.txt') as file:", "c) file = open('file.txt', 'r')", "d) open_file('file.txt')"],
                "answer": "b"
            },
            {
                "question": "What is a decorator?",
                "options": ["a) A function that modifies another function", "b) A design pattern", "c) A type of class", "d) A data structure"],
                "answer": "a"
            }
        ]
        
        score = 0
        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for option in q['options']:
                print(f"  {option}")
            
            answer = input("Your answer (a/b/c/d): ").lower().strip()
            if answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is {q['answer']}")
        
        print(f"\n📊 Quiz Score: {score}/{len(questions)}")
        if score == len(questions):
            print("🎉 Perfect score! You've mastered advanced Python concepts!")
        else:
            print("Keep practicing! Review generators, decorators, and file handling.")
            
    def run(self):
        while True:
            print(f"\n📖 {self.name} Module")
            print("1. Learn Concepts")
            print("2. See Examples")
            print("3. Interactive Exercise")
            print("4. Quick Quiz")
            print("5. Back to Main Menu")
            
            choice = input("Choose an option (1-5): ").strip()
            
            if choice == '1':
                self.display_content()
            elif choice == '2':
                self.show_examples()
            elif choice == '3':
                self.interactive_exercise()
            elif choice == '4':
                self.run_quiz()
            elif choice == '5':
                break
            else:
                print("❌ Invalid choice. Please try again.")
                
            input("\nPress Enter to continue...")
