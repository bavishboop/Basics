"""
Quiz System Module
Comprehensive quiz system covering all Python basics topics
"""

class QuizSystem:
    def __init__(self):
        self.questions = {
            'variables': [
                {
                    "question": "Which of the following is a valid variable name?",
                    "options": ["a) 2name", "b) my_name", "c) my-name", "d) my name"],
                    "answer": "b"
                },
                {
                    "question": "What is the result of type(3.14)?",
                    "options": ["a) <class 'int'>", "b) <class 'float'>", "c) <class 'str'>", "d) <class 'decimal'>"],
                    "answer": "b"
                },
                {
                    "question": "Which data type is immutable?",
                    "options": ["a) list", "b) dictionary", "c) tuple", "d) set"],
                    "answer": "c"
                }
            ],
            'operators': [
                {
                    "question": "What is the result of 10 % 3?",
                    "options": ["a) 3", "b) 1", "c) 0", "d) 3.33"],
                    "answer": "b"
                },
                {
                    "question": "Which operator has the highest precedence?",
                    "options": ["a) +", "b) *", "c) **", "d) //"],
                    "answer": "c"
                },
                {
                    "question": "What does 'in' operator check?",
                    "options": ["a) Variable existence", "b) Membership", "c) Type", "d) Value"],
                    "answer": "b"
                }
            ],
            'control_flow': [
                {
                    "question": "How many times will 'for i in range(5)' execute?",
                    "options": ["a) 4 times", "b) 5 times", "c) 6 times", "d) 0 times"],
                    "answer": "b"
                },
                {
                    "question": "What is the output of [x**2 for x in range(3)]?",
                    "options": ["a) [0, 1, 4]", "b) [1, 4, 9]", "c) [0, 2, 4]", "d) [1, 2, 3]"],
                    "answer": "a"
                },
                {
                    "question": "Which statement is used to handle exceptions?",
                    "options": ["a) try-catch", "b) try-except", "c) try-handle", "d) try-error"],
                    "answer": "b"
                }
            ],
            'data_structures': [
                {
                    "question": "Which method adds an element to a list?",
                    "options": ["a) add()", "b) append()", "c) insert()", "d) push()"],
                    "answer": "b"
                },
                {
                    "question": "How do you create a dictionary?",
                    "options": ["a) []", "b) ()", "c) {}", "d) //"],
                    "answer": "c"
                },
                {
                    "question": "What is the result of set([1,2,2,3])?",
                    "options": ["a) [1,2,2,3]", "b) {1,2,3}", "c) {1,2,2,3}", "d) Error"],
                    "answer": "b"
                }
            ],
            'file_handling': [
                {
                    "question": "Which mode opens a file for reading?",
                    "options": ["a) 'r'", "b) 'w'", "c) 'a'", "d) 'x'"],
                    "answer": "a"
                },
                {
                    "question": "What does the 'with' statement ensure?",
                    "options": ["a) File is opened", "b) File is closed", "c) File exists", "d) File is readable"],
                    "answer": "b"
                },
                {
                    "question": "Which method reads entire file?",
                    "options": ["a) readline()", "b) readlines()", "c) read()", "d) readall()"],
                    "answer": "c"
                }
            ]
        }
        
    def run_topic_quiz(self, topic):
        if topic not in self.questions:
            print("❌ Invalid topic!")
            return
            
        print(f"\n📝 {topic.upper()} QUIZ")
        print("="*40)
        
        score = 0
        questions = self.questions[topic]
        
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
        
        percentage = (score / len(questions)) * 100
        print(f"\n📊 Quiz Score: {score}/{len(questions)} ({percentage:.1f}%)")
        
        if percentage >= 80:
            print("🎉 Excellent work! You've mastered this topic!")
        elif percentage >= 60:
            print("👍 Good job! Review the concepts you missed.")
        else:
            print("📚 Keep practicing! Review the fundamentals.")
            
    def run_comprehensive_quiz(self):
        print("\n" + "="*60)
        print("🎓 COMPREHENSIVE PYTHON BASICS QUIZ")
        print("="*60)
        print("This quiz covers all topics from the Python basics course.")
        print("Let's test your knowledge! 🚀\n")
        
        all_questions = []
        for topic_questions in self.questions.values():
            all_questions.extend(topic_questions)
        
        import random
        random.shuffle(all_questions)
        
        score = 0
        total_questions = len(all_questions)
        
        for i, q in enumerate(all_questions, 1):
            print(f"Question {i}/{total_questions}: {q['question']}")
            for option in q['options']:
                print(f"  {option}")
            
            answer = input("Your answer (a/b/c/d): ").lower().strip()
            if answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is {q['answer']}")
            print()
        
        percentage = (score / total_questions) * 100
        print("="*60)
        print("📊 FINAL RESULTS")
        print("="*60)
        print(f"Total Score: {score}/{total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 90:
            print("🏆 OUTSTANDING! You're ready for DSA!")
            print("Your Python fundamentals are excellent!")
        elif percentage >= 75:
            print("🎉 GREAT JOB! You have a strong foundation!")
            print("You're well-prepared for DSA challenges!")
        elif percentage >= 60:
            print("👍 GOOD WORK! Review a few concepts and you'll be ready!")
            print("Consider revisiting the topics you struggled with.")
        else:
            print("📚 KEEP PRACTICING! Focus on the fundamentals.")
            print("Review all modules and try the quiz again.")
            
        print("\n💡 Recommendations:")
        if percentage < 100:
            print("- Review the questions you got wrong")
            print("- Practice with the interactive exercises")
            print("- Try the topic-specific quizzes")
        
        print("\n🚀 You're on your way to mastering Python for DSA!")
        
    def show_menu(self):
        print("\n📚 QUIZ SYSTEM")
        print("="*40)
        print("1. Variables & Data Types Quiz")
        print("2. Operators Quiz")
        print("3. Control Flow Quiz")
        print("4. Data Structures Quiz")
        print("5. File Handling Quiz")
        print("6. Comprehensive Quiz (All Topics)")
        print("7. Back to Main Menu")
        
    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose a quiz (1-7): ").strip()
            
            if choice == '1':
                self.run_topic_quiz('variables')
            elif choice == '2':
                self.run_topic_quiz('operators')
            elif choice == '3':
                self.run_topic_quiz('control_flow')
            elif choice == '4':
                self.run_topic_quiz('data_structures')
            elif choice == '5':
                self.run_topic_quiz('file_handling')
            elif choice == '6':
                self.run_comprehensive_quiz()
            elif choice == '7':
                break
            else:
                print("❌ Invalid choice. Please try again.")
                
            input("\nPress Enter to continue...")
