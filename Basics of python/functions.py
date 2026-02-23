"""
Functions and Modules Module
Covers function definition, parameters, return values, scope, and module organization
"""

class FunctionsModule:
    def __init__(self):
        self.name = "Functions and Modules"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 FUNCTIONS AND MODULES")
        print("="*60)
        
        print("\n🔹 FUNCTION BASICS:")
        print("• Reusable blocks of code that perform specific tasks")
        print("• Defined using 'def' keyword")
        print("• Can accept parameters (arguments)")
        print("• Can return values using 'return' statement")
        print("• Help organize code and avoid repetition")
        
        print("\n🔹 FUNCTION DEFINITION:")
        print("def function_name(parameter1, parameter2):")
        print("    # Function body")
        print("    return result")
        
        print("\n🔹 PARAMETERS AND ARGUMENTS:")
        print("• Positional arguments: passed by position")
        print("• Keyword arguments: passed by name")
        print("• Default parameters: have default values")
        print("• *args: variable number of positional arguments")
        print("• **kwargs: variable number of keyword arguments")
        
        print("\n🔹 RETURN VALUES:")
        print("• Functions can return single or multiple values")
        print("• Use 'return' statement to send back values")
        print("• If no return statement, returns None")
        print("• Can return tuples, lists, dictionaries")
        
        print("\n🔹 VARIABLE SCOPE:")
        print("• Local scope: variables inside function")
        print("• Global scope: variables outside all functions")
        print("• Built-in scope: Python built-in functions")
        print("• Use 'global' keyword to modify global variables")
        
        print("\n🔹 LAMBDA FUNCTIONS:")
        print("• Anonymous functions (single line)")
        print("• Syntax: lambda arguments: expression")
        print("• Used for short, simple operations")
        
        print("\n🔹 MODULES:")
        print("• Python files containing functions and variables")
        print("• Import using 'import module_name'")
        print("• Import specific items: 'from module import item'")
        print("• Create aliases: 'import module as alias'")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 Basic Function Definition:")
        print("""
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # "Hello, Alice!"
        """)
        
        print("\n🔹 Function with Multiple Parameters:")
        print("""
def calculate_area(length, width):
    return length * width

# Positional arguments
area1 = calculate_area(10, 5)
print(area1)  # 50

# Keyword arguments
area2 = calculate_area(width=8, length=3)
print(area2)  # 24
        """)
        
        print("\n🔹 Default Parameters:")
        print("""
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9 (3^2)
print(power(3, 3))   # 27 (3^3)
print(power(2, 5))   # 32 (2^5)
        """)
        
        print("\n🔹 Variable Arguments:")
        print("""
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC
        """)
        
        print("\n🔹 Multiple Return Values:")
        print("""
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

minimum, maximum, average = get_stats([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")
# Min: 1, Max: 9, Avg: 4.0
        """)
        
        print("\n🔹 Lambda Functions:")
        print("""
# Regular function
def square(x):
    return x * x

# Lambda equivalent
square_lambda = lambda x: x * x

print(square(5))           # 25
print(square_lambda(5))    # 25

# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 7))           # 10

# Lambda in built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
        """)
        
        print("\n🔹 Scope Examples:")
        print("""
global_var = 100

def scope_example():
    local_var = 50
    print(global_var)  # Can access global
    print(local_var)   # Can access local
    
    # To modify global
    global global_var
    global_var = 200

scope_example()
print(global_var)  # 200 (modified)
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nExercise 1: Create a calculator function")
        print("Write a function that performs basic arithmetic operations")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# Test the calculator
print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
        """)
        
        print("\nExercise 2: Create a function to find prime numbers")
        print("Write a function that checks if a number is prime")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

# Test the functions
print(is_prime(17))        # True
print(is_prime(15))        # False
print(find_primes(1, 20))  # [2, 3, 5, 7, 11, 13, 17, 19]
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "What keyword is used to define a function?",
                "options": ["a) function", "b) def", "c) func", "d) define"],
                "answer": "b"
            },
            {
                "question": "How do you specify a default parameter value?",
                "options": ["a) def func(param = value):", "b) def func(param: value):", "c) def func(param default value):", "d) def func(param -> value):"],
                "answer": "a"
            },
            {
                "question": "What does *args allow you to do?",
                "options": ["a) Pass keyword arguments", "b) Pass unlimited positional arguments", "c) Return multiple values", "d) Import modules"],
                "answer": "b"
            },
            {
                "question": "What is the return value of a function without return statement?",
                "options": ["a) 0", "b) False", "c) None", "d) Error"],
                "answer": "c"
            },
            {
                "question": "Which is correct lambda syntax?",
                "options": ["a) lambda x: return x*2", "b) lambda x = x*2", "c) lambda x: x*2", "d) lambda(x): x*2"],
                "answer": "c"
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
            print("🎉 Perfect score! You've mastered functions and modules!")
        else:
            print("Keep practicing! Review function syntax and parameters.")
            
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
