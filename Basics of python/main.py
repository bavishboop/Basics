"""
Python Mastery App - Complete Learning Platform
Comprehensive Python concepts application for DSA preparation
"""

import sys
import os

# Import all modules
from variables import VariablesModule
from operators import OperatorsModule
from control_flow import ControlFlowModule
from data_structures import DataStructuresModule
from functions import FunctionsModule
from oop import OOPModule
from algorithms import AlgorithmsModule
from advanced_python import AdvancedPythonModule
from file_handling import FileHandlingModule
from quiz_system import QuizSystem

class PythonMasteryApp:
    def __init__(self):
        self.app_name = "🐍 Python Mastery for DSA"
        self.modules = {
            '1': VariablesModule(),
            '2': OperatorsModule(),
            '3': ControlFlowModule(),
            '4': DataStructuresModule(),
            '5': FunctionsModule(),
            '6': OOPModule(),
            '7': AlgorithmsModule(),
            '8': AdvancedPythonModule(),
            '9': FileHandlingModule(),
            '10': QuizSystem()
        }
        
    def display_welcome(self):
        print("\n" + "="*80)
        print("🎓 " + self.app_name)
        print("="*80)
        print("\n📚 Welcome to your comprehensive Python learning platform!")
        print("This application covers all essential Python concepts needed")
        print("for advanced Data Structures and Algorithms preparation.")
        print("\n🎯 Learning Path:")
        print("   1. Variables & Data Types → 2. Operators → 3. Control Flow")
        print("   4. Data Structures → 5. Functions → 6. Object-Oriented Programming")
        print("   7. Algorithms → 8. Advanced Concepts → 9. File Handling")
        print("   10. Comprehensive Quiz System")
        print("\n💡 Each module includes:")
        print("   • Concept explanations with examples")
        print("   • Interactive coding exercises")
        print("   • Practice quizzes with instant feedback")
        print("   • Real-world problem-solving scenarios")
        
    def display_menu(self):
        print("\n" + "="*60)
        print("📖 MAIN MENU - Choose Your Learning Module")
        print("="*60)
        print("\n🔹 FUNDAMENTALS:")
        print("1. Variables and Data Types")
        print("2. Operators")
        print("3. Control Flow")
        print("\n🔹 CORE CONCEPTS:")
        print("4. Data Structures")
        print("5. Functions and Modules")
        print("6. Object-Oriented Programming")
        print("\n🔹 ADVANCED TOPICS:")
        print("7. Algorithms and Problem Solving")
        print("8. Advanced Python Concepts")
        print("9. File Handling and I/O Operations")
        print("\n🔹 PRACTICE & ASSESSMENT:")
        print("10. Comprehensive Quiz System")
        print("\n0. Exit Application")
        
    def display_learning_path(self):
        print("\n" + "="*60)
        print("🗺️ RECOMMENDED LEARNING PATH")
        print("="*60)
        
        path = [
            ("Variables & Data Types", "Foundation of programming"),
            ("Operators", "Mathematical and logical operations"),
            ("Control Flow", "Decision making and loops"),
            ("Data Structures", "Organizing and storing data"),
            ("Functions", "Reusable code blocks"),
            ("OOP", "Object-oriented design principles"),
            ("Algorithms", "Problem-solving strategies"),
            ("Advanced Concepts", "Professional Python features"),
            ("File Handling", "Working with external data"),
            ("Quiz System", "Test your knowledge")
        ]
        
        for i, (topic, description) in enumerate(path, 1):
            print(f"{i:2d}. {topic:<25} - {description}")
        
        print("\n💡 Tips:")
        print("• Complete modules in order for best results")
        print("• Each module builds on previous concepts")
        print("• Practice exercises are crucial for mastery")
        print("• Take quizzes to test your understanding")
        print("• Review concepts you find challenging")
        
    def show_progress_tracker(self):
        print("\n" + "="*60)
        print("📊 PROGRESS TRACKER")
        print("="*60)
        
        print("\n🎯 Your Learning Journey:")
        print("□ Module 1: Variables and Data Types")
        print("□ Module 2: Operators")
        print("□ Module 3: Control Flow")
        print("□ Module 4: Data Structures")
        print("□ Module 5: Functions and Modules")
        print("□ Module 6: Object-Oriented Programming")
        print("□ Module 7: Algorithms and Problem Solving")
        print("□ Module 8: Advanced Python Concepts")
        print("□ Module 9: File Handling and I/O Operations")
        print("□ Module 10: Comprehensive Quiz System")
        
        print("\n📈 Progress: 0/10 modules completed")
        print("🎯 Next Step: Start with Module 1 - Variables and Data Types")
        
    def show_study_tips(self):
        print("\n" + "="*60)
        print("💡 STUDY TIPS FOR DSA SUCCESS")
        print("="*60)
        
        tips = [
            "🔹 Practice coding daily - consistency is key",
            "🔹 Understand concepts before memorizing syntax",
            "🔹 Solve problems without looking at solutions first",
            "🔹 Review and refactor your code for better solutions",
            "🔹 Join coding communities and discuss problems",
            "🔹 Build projects to apply what you've learned",
            "🔹 Read other people's code to learn new patterns",
            "🔹 Focus on problem-solving approach, not just code",
            "🔹 Time yourself to improve speed and efficiency",
            "🔹 Teach others to solidify your understanding"
        ]
        
        for tip in tips:
            print(tip)
        
        print("\n🎯 DSA Preparation Strategy:")
        print("1. Master Python fundamentals (this app!)")
        print("2. Learn basic data structures (arrays, linked lists, stacks, queues)")
        print("3. Study algorithms (sorting, searching, recursion)")
        print("4. Practice on coding platforms daily")
        print("5. Analyze time and space complexity")
        print("6. Solve problems by category (arrays, strings, trees, etc.)")
        print("7. Participate in coding competitions")
        print("8. Review and optimize your solutions")
        
    def run(self):
        self.display_welcome()
        
        while True:
            self.display_menu()
            
            choice = input("\nChoose an option (0-10): ").strip()
            
            if choice == '0':
                print("\n👋 Thank you for using Python Mastery for DSA!")
                print("🎓 Keep practicing and happy coding!")
                print("\n📚 Recommended next steps:")
                print("• Start practicing on LeetCode, HackerRank, or Codeforces")
                print("• Join study groups and coding communities")
                print("• Build projects to apply your knowledge")
                print("• Prepare for technical interviews")
                break
                
            elif choice in self.modules:
                print(f"\n🚀 Launching {self.modules[choice].name}...")
                self.modules[choice].run()
                
            elif choice == 'help':
                self.display_learning_path()
                
            elif choice == 'progress':
                self.show_progress_tracker()
                
            elif choice == 'tips':
                self.show_study_tips()
                
            else:
                print("❌ Invalid choice. Please try again.")
                print("💡 Type 'help' for learning path or 'tips' for study advice")
                
            if choice != '0':
                input("\nPress Enter to return to main menu...")

def main():
    """Main function to run the Python Mastery App"""
    try:
        app = PythonMasteryApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please report this issue or restart the application.")

if __name__ == "__main__":
    main()
