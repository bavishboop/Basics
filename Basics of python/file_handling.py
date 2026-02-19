"""
File Handling Module
Covers reading from and writing to files in Python
"""

class FileHandlingModule:
    def __init__(self):
        self.name = "File Handling"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 FILE HANDLING")
        print("="*60)
        
        print("\n🔹 FILE OPENING MODES:")
        print("'r' - Read: Open file for reading (default)")
        print("'w' - Write: Open file for writing (creates new or truncates existing)")
        print("'a' - Append: Open file for appending (creates new if doesn't exist)")
        print("'r+' - Read and Write: Open for both reading and writing")
        print("'x' - Exclusive Creation: Create new file, fail if exists")
        
        print("\n🔹 FILE TYPES:")
        print("Text files: Human-readable text with encoding")
        print("Binary files: Machine-readable data (images, executables)")
        
        print("\n🔹 CONTEXT MANAGERS:")
        print("with statement: Automatically handles file closing")
        print("Prevents resource leaks and errors")
        
        print("\n🔹 FILE OPERATIONS:")
        print("Reading: read(), readline(), readlines()")
        print("Writing: write(), writelines()")
        print("Seeking: seek(), tell()")
        print("File properties: name, mode, closed")
        
        print("\n🔹 ERROR HANDLING:")
        print("FileNotFoundError: File doesn't exist")
        print("PermissionError: No permission to access file")
        print("IsADirectoryError: Path is directory, not file")
        print("UnicodeDecodeError: Encoding issues")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 Basic File Operations:")
        print("""
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\\n')
    file.write('This is a test file.\\n')

# Reading entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Remove newline character

# Reading all lines into list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # ['Hello, World!\\n', 'This is a test file.\\n']
        """)
        
        print("\n🔹 Appending to Files:")
        print("""
# Appending to existing file
with open('example.txt', 'a') as file:
    file.write('This line is appended.\\n')

# Writing multiple lines
lines = ['Line 1\\n', 'Line 2\\n', 'Line 3\\n']
with open('multiline.txt', 'w') as file:
    file.writelines(lines)
        """)
        
        print("\n🔹 File Position Operations:")
        print("""
with open('example.txt', 'r') as file:
    print(f"Current position: {file.tell()}")  # 0
    
    # Read first 5 characters
    first_five = file.read(5)
    print(f"Read: '{first_five}'")
    print(f"Current position: {file.tell()}")  # 5
    
    # Go back to beginning
    file.seek(0)
    print(f"After seek(0): {file.tell()}")  # 0
    
    # Read first line
    first_line = file.readline()
    print(f"First line: {first_line.strip()}")
        """)
        
        print("\n🔹 Error Handling:")
        print("""
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File does not exist!")
except PermissionError:
    print("No permission to read this file!")
except Exception as e:
    print(f"An error occurred: {e}")

# Checking if file exists before opening
import os
if os.path.exists('example.txt'):
    with open('example.txt', 'r') as file:
        content = file.read()
else:
    print("File doesn't exist!")
        """)
        
        print("\n🔹 Working with CSV Files:")
        print("""
import csv

# Writing to CSV
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Alice', 20, 'A'])
    writer.writerow(['Bob', 21, 'B'])

# Reading from CSV
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Name', 'Age', 'Grade'], ['Alice', '20', 'A'], etc.
        """)
        
        print("\n🔹 Working with JSON Files:")
        print("""
import json

# Writing JSON data
data = {
    'name': 'John',
    'age': 30,
    'hobbies': ['reading', 'coding', 'gaming']
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

# Reading JSON data
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data['name'])  # John
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nExercise 1: Create a simple todo list manager")
        print("Write a program that can add tasks to a file and display all tasks")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def add_task(task):
    with open('todo.txt', 'a') as file:
        file.write(f"{task}\\n")

def show_tasks():
    try:
        with open('todo.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks yet!")
            else:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet!")

# Usage
add_task("Learn Python file handling")
add_task("Practice DSA problems")
show_tasks()
        """)
        
        print("\nExercise 2: Count words in a file")
        print("Write a program that counts words and lines in a text file")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def count_words_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = 0
            
            for line in lines:
                words = line.split()
                word_count += len(words)
                
            return line_count, word_count
    except FileNotFoundError:
        return 0, 0

lines, words = count_words_lines('example.txt')
print(f"Lines: {lines}, Words: {words}")
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "Which mode is used to append to a file?",
                "options": ["a) 'r'", "b) 'w'", "c) 'a'", "d) 'x'"],
                "answer": "c"
            },
            {
                "question": "What does the 'with' statement do in file handling?",
                "options": ["a) Opens file only", "b) Automatically closes file", "c) Creates file", "d) Deletes file"],
                "answer": "b"
            },
            {
                "question": "Which method reads a single line from a file?",
                "options": ["a) read()", "b) readline()", "c) readlines()", "d) line()"],
                "answer": "b"
            },
            {
                "question": "Which exception is raised when a file doesn't exist?",
                "options": ["a) ValueError", "b) TypeError", "c) FileNotFoundError", "d) IOError"],
                "answer": "c"
            },
            {
                "question": "What does file.tell() return?",
                "options": ["a) File size", "b) Current position", "c) File name", "d) File mode"],
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
            print("🎉 Perfect score! You've mastered file handling!")
        else:
            print("Keep practicing! Review file modes and error handling.")
            
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
