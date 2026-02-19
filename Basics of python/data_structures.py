"""
Data Structures Module
Covers Python's built-in data structures: lists, tuples, dictionaries, and sets
"""

class DataStructuresModule:
    def __init__(self):
        self.name = "Data Structures"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 DATA STRUCTURES")
        print("="*60)
        
        print("\n🔹 LISTS:")
        print("• Ordered collection of items")
        print("• Mutable (can be modified)")
        print("• Allows duplicate elements")
        print("• Can contain different data types")
        print("• Created with square brackets []")
        
        print("\n🔹 TUPLES:")
        print("• Ordered collection of items")
        print("• Immutable (cannot be modified)")
        print("• Allows duplicate elements")
        print("• Can contain different data types")
        print("• Created with parentheses ()")
        
        print("\n🔹 DICTIONARIES:")
        print("• Collection of key-value pairs")
        print("• Mutable (can be modified)")
        print("• Keys must be unique and immutable")
        print("• Values can be any data type")
        print("• Created with curly braces {}")
        
        print("\n🔹 SETS:")
        print("• Unordered collection of unique items")
        print("• Mutable (can be modified)")
        print("• No duplicate elements allowed")
        print("• Elements must be immutable")
        print("• Created with set() or {} with single element")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 List Operations:")
        print("""
# Creating lists
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]

# Accessing elements
print(fruits[0])        # 'apple'
print(fruits[-1])       # 'orange' (last element)
print(fruits[1:3])      # ['banana', 'orange']

# Modifying lists
fruits.append('grape')  # Add to end
fruits.insert(1, 'kiwi') # Insert at index
fruits.remove('banana') # Remove specific item
popped = fruits.pop()    # Remove and return last item

# List methods
numbers.sort()          # Sort in place
numbers.reverse()       # Reverse in place
print(len(numbers))     # Get length
print(3 in numbers)     # Check membership
        """)
        
        print("\n🔹 Tuple Operations:")
        print("""
# Creating tuples
coordinates = (10, 20)
rgb = (255, 0, 0)
single = (42,)  # Note the comma for single element

# Accessing elements (same as lists)
print(coordinates[0])   # 10
print(coordinates[1:])  # (20,)

# Tuple methods
print(len(coordinates))  # 2
print(coordinates.count(10))  # 1
print(coordinates.index(20))  # 1

# Tuples are immutable
# coordinates[0] = 15  # This would cause an error!

# Tuple unpacking
x, y = coordinates
print(f"x: {x}, y: {y}")
        """)
        
        print("\n🔹 Dictionary Operations:")
        print("""
# Creating dictionaries
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
empty_dict = {}

# Accessing values
print(person['name'])        # 'John'
print(person.get('age'))     # 30
print(person.get('country', 'USA'))  # 'USA' (default)

# Modifying dictionaries
person['age'] = 31           # Update value
person['email'] = 'john@email.com'  # Add new key-value
del person['city']           # Remove key

# Dictionary methods
print(person.keys())         # dict_keys(['name', 'age', 'email'])
print(person.values())       # dict_values(['John', 31, 'john@email.com'])
print(person.items())        # dict_items([('name', 'John'), ...])
print('name' in person)      # True
        """)
        
        print("\n🔹 Set Operations:")
        print("""
# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set([1, 2, 2, 3])  # From list, removes duplicates

# Basic operations
set1.add(6)                 # Add element
set1.remove(1)              # Remove element
set1.discard(99)            # Remove if exists (no error)

# Set operations
print(set1 | set2)          # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1 & set2)          # Intersection: {4, 5, 6}
print(set1 - set2)          # Difference: {1, 2, 3}
print(set1 ^ set2)          # Symmetric difference: {1, 2, 3, 7, 8}

# Set methods
print(len(set1))            # 5
print(3 in set1)            # True
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nExercise 1: Student Grade Management")
        print("Create a system to manage student grades using appropriate data structures")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
# Using dictionary for student data
students = {
    'Alice': {'math': 90, 'science': 85, 'english': 92},
    'Bob': {'math': 78, 'science': 82, 'english': 88},
    'Charlie': {'math': 95, 'science': 89, 'english': 91}
}

# Calculate average grade for each student
for name, grades in students.items():
    average = sum(grades.values()) / len(grades)
    print(f"{name}'s average: {average:.2f}")

# Find class average for each subject
subjects = ['math', 'science', 'english']
for subject in subjects:
    subject_scores = [grades[subject] for grades in students.values()]
    class_avg = sum(subject_scores) / len(subject_scores)
    print(f"Class {subject} average: {class_avg:.2f}")
        """)
        
        print("\nExercise 2: Remove duplicates from a list")
        print("Given a list with duplicates, create a list with unique elements")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
# Method 1: Using set
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique_numbers = list(set(numbers))
print(unique_numbers)  # Order may vary

# Method 2: Preserving order
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

unique_ordered = remove_duplicates_preserve_order(numbers)
print(unique_ordered)  # [1, 2, 3, 4, 5]
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "Which data structure is immutable?",
                "options": ["a) list", "b) dictionary", "c) tuple", "d) set"],
                "answer": "c"
            },
            {
                "question": "How do you access the value for key 'name' in dictionary 'person'?",
                "options": ["a) person.name", "b) person['name']", "c) person.get('name')", "d) Both b and c"],
                "answer": "d"
            },
            {
                "question": "Which method adds an element to the end of a list?",
                "options": ["a) add()", "b) append()", "c) insert()", "d) extend()"],
                "answer": "b"
            },
            {
                "question": "What is the result of set([1, 2, 2, 3])?",
                "options": ["a) [1, 2, 2, 3]", "b) {1, 2, 3}", "c) {1, 2, 2, 3}", "d) Error"],
                "answer": "b"
            },
            {
                "question": "Which data structure stores key-value pairs?",
                "options": ["a) list", "b) tuple", "c) dictionary", "d) set"],
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
            print("🎉 Perfect score! You've mastered data structures!")
        else:
            print("Keep practicing! Review the properties of each data structure.")
            
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
