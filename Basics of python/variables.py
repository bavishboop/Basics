"""
Variables and Data Types Module
Covers Python variables, data types, type conversion, and basic operations
"""

class VariablesModule:
    def __init__(self):
        self.name = "Variables and Data Types"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 VARIABLES AND DATA TYPES")
        print("="*60)
        
        print("\n🔹 BASIC DATA TYPES:")
        print("1. Integer (int): Whole numbers")
        print("   Example: age = 25, count = -10")
        
        print("\n2. Float (float): Decimal numbers")
        print("   Example: price = 19.99, temperature = -5.5")
        
        print("\n3. String (str): Text data")
        print("   Example: name = 'Alice', message = \"Hello World\"")
        
        print("\n4. Boolean (bool): True or False")
        print("   Example: is_student = True, has_license = False")
        
        print("\n🔹 COLLECTION TYPES:")
        print("5. List: Ordered, mutable collection")
        print("   Example: fruits = ['apple', 'banana', 'orange']")
        
        print("\n6. Tuple: Ordered, immutable collection")
        print("   Example: coordinates = (10, 20)")
        
        print("\n7. Dictionary: Key-value pairs")
        print("   Example: person = {'name': 'John', 'age': 30}")
        
        print("\n8. Set: Unordered, unique elements")
        print("   Example: unique_numbers = {1, 2, 3, 4}")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 Variable Assignment and Type Checking:")
        print("""
# Variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True

# Check types
print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_student))  # <class 'bool'>
        """)
        
        print("\n🔹 Type Conversion:")
        print("""
# Converting between types
num_str = "42"
num_int = int(num_str)    # Convert string to integer
num_float = float(num_int) # Convert integer to float
back_to_str = str(num_float) # Convert back to string

print(num_int)      # 42
print(num_float)    # 42.0
print(back_to_str)  # "42.0"
        """)
        
        print("\n🔹 String Operations:")
        print("""
text = "Hello World"
print(text.upper())        # "HELLO WORLD"
print(text.lower())        # "hello world"
print(text.split())        # ['Hello', 'World']
print(len(text))           # 11
print(text.replace("World", "Python"))  # "Hello Python"
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nLet's practice! Try these operations:")
        print("1. Create a variable 'x' with value 10")
        print("2. Create a variable 'y' with value 3.14")
        print("3. Create a variable 'name' with your name")
        print("4. Convert x to float and y to integer")
        print("5. Find the length of your name")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
x = 10
y = 3.14
name = "Your Name"

x_float = float(x)    # 10.0
y_int = int(y)        # 3
name_length = len(name)  # length of your name

print(f"x as float: {x_float}")
print(f"y as integer: {y_int}")
print(f"Name length: {name_length}")
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "What data type would you use for a whole number?",
                "options": ["a) float", "b) int", "c) str", "d) bool"],
                "answer": "b"
            },
            {
                "question": "Which of these is immutable?",
                "options": ["a) list", "b) dict", "c) tuple", "d) set"],
                "answer": "c"
            },
            {
                "question": "How do you check the type of a variable?",
                "options": ["a) typeof()", "b) type()", "c) gettype()", "d) check_type()"],
                "answer": "b"
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
            print("🎉 Perfect score! You've mastered this topic!")
        else:
            print("Keep practicing! Review the concepts and try again.")
            
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
