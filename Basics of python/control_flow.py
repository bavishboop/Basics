"""
Control Flow Module
Covers conditional statements, loops, and error handling in Python
"""

class ControlFlowModule:
    def __init__(self):
        self.name = "Control Flow"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 CONTROL FLOW")
        print("="*60)
        
        print("\n🔹 CONDITIONAL STATEMENTS:")
        print("if statement: Executes code if condition is True")
        print("if-else statement: Executes one of two blocks")
        print("if-elif-else statement: Multiple conditions")
        print("Nested if statements: if inside another if")
        
        print("\n🔹 LOOPS:")
        print("for loop: Iterate over sequences (lists, strings, ranges)")
        print("while loop: Repeat while condition is True")
        print("Nested loops: Loop inside another loop")
        print("Loop control: break, continue, pass")
        
        print("\n🔹 LOOP CONTROL STATEMENTS:")
        print("break: Exit the loop immediately")
        print("continue: Skip to next iteration")
        print("pass: Do nothing (placeholder)")
        
        print("\n🔹 COMPREHENSIONS:")
        print("List comprehension: [expression for item in iterable]")
        print("Dictionary comprehension: {key: value for item in iterable}")
        print("Set comprehension: {expression for item in iterable}")
        
        print("\n🔹 EXCEPTION HANDLING:")
        print("try-except: Handle errors gracefully")
        print("try-except-else: Execute if no exception occurs")
        print("try-except-finally: Always execute cleanup code")
        print("raise: Manually raise exceptions")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 Conditional Statements:")
        print("""
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Nested conditions
grade = 85
if grade >= 60:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")  # This will execute
    else:
        print("C")
else:
    print("F")
        """)
        
        print("\n🔹 For Loops:")
        print("""
# Loop over range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Loop over list
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(f"I like {fruit}")

# Loop with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Loop over string
for char in "Python":
    print(char.upper())
        """)
        
        print("\n🔹 While Loops:")
        print("""
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You said: {user_input}")
        """)
        
        print("\n🔹 Loop Control:")
        print("""
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)  # 0, 1, 2, 4, 5, 6

# Pass statement
for i in range(3):
    pass  # Do nothing, placeholder
        """)
        
        print("\n🔹 Comprehensions:")
        print("""
# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ['hello', 'world', 'python']}

# Set comprehension
unique_chars = {char for char in 'hello world'}
        """)
        
        print("\n🔹 Exception Handling:")
        print("""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"10 divided by {num} is {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("Thank you for using this program!")
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nExercise 1: Find even numbers from 1 to 20")
        print("Write a program that prints all even numbers from 1 to 20")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
# Method 1: Using for loop with if
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Method 2: Using range with step
for num in range(2, 21, 2):
    print(num)

# Method 3: Using list comprehension
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)
        """)
        
        print("\nExercise 2: Guess the number game logic")
        print("Write the logic for a simple guess the number game")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
secret_number = 42
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    if attempts == max_attempts:
        print(f"Game over! The number was {secret_number}")
else:
    print("You ran out of attempts!")
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "How many times will this loop run: for i in range(3)?",
                "options": ["a) 2 times", "b) 3 times", "c) 4 times", "d) 0 times"],
                "answer": "b"
            },
            {
                "question": "What does the 'break' statement do in a loop?",
                "options": ["a) Skips current iteration", "b) Exits the loop", "c) Continues to next iteration", "d) Pauses the loop"],
                "answer": "b"
            },
            {
                "question": "Which is used to handle exceptions in Python?",
                "options": ["a) try-catch", "b) try-except", "c) try-handle", "d) try-error"],
                "answer": "b"
            },
            {
                "question": "What is the output of: [x*2 for x in range(3)]?",
                "options": ["a) [0, 2, 4]", "b) [2, 4, 6]", "c) [0, 1, 2]", "d) [1, 2, 3]"],
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
            print("🎉 Perfect score! You've mastered control flow!")
        else:
            print("Keep practicing! Review loops and conditionals.")
            
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
