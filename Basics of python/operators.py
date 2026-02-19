"""
Operators Module
Covers arithmetic, comparison, logical, and assignment operators in Python
"""

class OperatorsModule:
    def __init__(self):
        self.name = "Operators"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 OPERATORS")
        print("="*60)
        
        print("\n🔹 ARITHMETIC OPERATORS:")
        print("+ Addition: x + y")
        print("- Subtraction: x - y")
        print("* Multiplication: x * y")
        print("/ Division: x / y (float result)")
        print("// Floor Division: x // y (integer result)")
        print("% Modulus: x % y (remainder)")
        print("** Exponentiation: x ** y (power)")
        
        print("\n🔹 COMPARISON OPERATORS:")
        print("== Equal to: x == y")
        print("!= Not equal to: x != y")
        print("> Greater than: x > y")
        print("< Less than: x < y")
        print(">= Greater than or equal: x >= y")
        print("<= Less than or equal: x <= y")
        
        print("\n🔹 LOGICAL OPERATORS:")
        print("and: True if both conditions are True")
        print("or: True if at least one condition is True")
        print("not: Reverses the boolean value")
        
        print("\n🔹 ASSIGNMENT OPERATORS:")
        print("=: Simple assignment")
        print("+=: Add and assign")
        print("-=: Subtract and assign")
        print("*=: Multiply and assign")
        print("/=: Divide and assign")
        print("%=: Modulus and assign")
        print("**=: Exponent and assign")
        print("//=: Floor divide and assign")
        
        print("\n🔹 MEMBERSHIP OPERATORS:")
        print("in: Checks if value is in sequence")
        print("not in: Checks if value is not in sequence")
        
        print("\n🔹 IDENTITY OPERATORS:")
        print("is: Checks if two variables refer to same object")
        print("is not: Checks if two variables refer to different objects")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 Arithmetic Operations:")
        print("""
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3 (floor division)
print(a % b)    # 1 (remainder)
print(a ** b)   # 1000 (10 to the power of 3)
        """)
        
        print("\n🔹 Comparison Operations:")
        print("""
x = 10
y = 5

print(x > y)     # True
print(x < y)     # False
print(x == y)    # False
print(x != y)    # True
print(x >= 10)   # True
print(y <= 5)    # True
        """)
        
        print("\n🔹 Logical Operations:")
        print("""
age = 25
has_license = True

print(age >= 18 and has_license)  # True
print(age >= 18 or has_license)   # True
print(not has_license)            # False
        """)
        
        print("\n🔹 Assignment Operations:")
        print("""
count = 10
count += 5    # count = count + 5 (15)
count *= 2    # count = count * 2 (30)
count -= 10   # count = count - 10 (20)
count //= 3   # count = count // 3 (6)
        """)
        
        print("\n🔹 Membership and Identity:")
        print("""
fruits = ['apple', 'banana', 'orange']
print('apple' in fruits)        # True
print('grape' not in fruits)    # True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True (same content)
print(list1 is list2)  # False (different objects)
print(list1 is list3)  # True (same object)
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nLet's practice operator precedence and combinations!")
        print("Calculate the result of: 10 + 2 * 3 - 4 // 2")
        print("Remember: PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
# Step by step evaluation:
result = 10 + 2 * 3 - 4 // 2

# 1. Multiplication: 2 * 3 = 6
# 2. Floor division: 4 // 2 = 2
# 3. Addition: 10 + 6 = 16
# 4. Subtraction: 16 - 2 = 14

print(result)  # 14
        """)
        
        print("\nNow try this logical expression:")
        print("not (True and False) or (True or False)")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
# Step by step evaluation:
result = not (True and False) or (True or False)

# 1. First parentheses: True and False = False
# 2. Second parentheses: True or False = True
# 3. not False = True
# 4. True or True = True

print(result)  # True
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "What is the result of 10 // 3?",
                "options": ["a) 3.33", "b) 3", "c) 1", "d) 0"],
                "answer": "b"
            },
            {
                "question": "Which operator has higher precedence: * or +?",
                "options": ["a) +", "b) *", "c) They have equal precedence", "d) It depends"],
                "answer": "b"
            },
            {
                "question": "What does 'is' operator check?",
                "options": ["a) Value equality", "b) Type equality", "c) Object identity", "d) String equality"],
                "answer": "c"
            },
            {
                "question": "What is the result of not (True or False)?",
                "options": ["a) True", "b) False", "c) Error", "d) None"],
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
            print("🎉 Perfect score! You've mastered operators!")
        else:
            print("Keep practicing! Review operator precedence and types.")
            
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
