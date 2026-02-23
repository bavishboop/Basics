"""
Object-Oriented Programming Module
Covers classes, objects, inheritance, polymorphism, and OOP principles
"""

class OOPModule:
    def __init__(self):
        self.name = "Object-Oriented Programming"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 OBJECT-ORIENTED PROGRAMMING")
        print("="*60)
        
        print("\n🔹 OOP CONCEPTS:")
        print("• Object: Instance of a class with data and behavior")
        print("• Class: Blueprint for creating objects")
        print("• Encapsulation: Bundling data and methods together")
        print("• Inheritance: Reusing code from parent classes")
        print("• Polymorphism: Same interface, different implementations")
        print("• Abstraction: Hiding complexity, showing essential features")
        
        print("\n🔹 CLASS DEFINITION:")
        print("class ClassName:")
        print("    def __init__(self, parameters):")
        print("        # Constructor/Initializer")
        print("        self.attribute = value")
        print("    ")
        print("    def method(self, parameters):")
        print("        # Method definition")
        print("        return result")
        
        print("\n🔹 CONSTRUCTOR (__init__):")
        print("• Special method called when creating object")
        print("• Initializes object attributes")
        print("• 'self' parameter refers to the instance")
        print("• Can have additional parameters")
        
        print("\n🔹 METHODS:")
        print("• Instance methods: operate on object data")
        print("• Class methods: operate on class data")
        print("• Static methods: don't need instance or class")
        print("• Property methods: like attributes, but are methods")
        
        print("\n🔹 INHERITANCE:")
        print("• Child class inherits from parent class")
        print("• Child gets all parent attributes and methods")
        print("• Can override parent methods")
        print("• Can extend with new attributes and methods")
        print("• Multiple inheritance: inherit from multiple classes")
        
        print("\n🔹 POLYMORPHISM:")
        print("• Same method name, different behavior")
        print("• Method overriding in child classes")
        print("• Duck typing: if it walks like a duck...")
        print("• Operator overloading: define behavior for operators")
        
        print("\n🔹 SPECIAL METHODS:")
        print("• __str__: String representation")
        print("• __repr__: Official representation")
        print("• __len__: Length of object")
        print("• __eq__: Equality comparison")
        print("• __lt__, __gt__: Less than, greater than")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 Basic Class Definition:")
        print("""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age}"

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())  # Hi, I'm Alice and I'm 25 years old
print(person2.celebrate_birthday())  # Happy birthday Bob! Now 31
        """)
        
        print("\n🔹 Class with Properties:")
        print("""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height

rect = Rectangle(5, 3)
print(rect.area)        # 15
print(rect.perimeter)    # 16
print(rect.is_square())  # False
        """)
        
        print("\n🔹 Inheritance Example:")
        print("""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow!"
    
    def purr(self):
        return f"{self.name} is purring"

# Using inherited classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.make_sound())  # Woof! Woof!
print(cat.make_sound())  # Meow!
print(dog.eat())         # Buddy is eating
print(cat.purr())        # Whiskers is purring
        """)
        
        print("\n🔹 Polymorphism Example:")
        print("""
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

def print_shape_info(shape):
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

# Same function, different behavior
circle = Circle(5)
square = Square(4)

print("Circle:")
print_shape_info(circle)
print("\\nSquare:")
print_shape_info(square)
        """)
        
        print("\n🔹 Special Methods Example:")
        print("""
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and 
                   self.author == other.author)
        return False
    
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)

print(str(book1))        # '1984' by George Orwell
print(len(book1))        # 328
print(book1 == book2)    # False
print(book1 > book2)     # True (more pages)
        """)
        
        print("\n🔹 Class and Static Methods:")
        print("""
class MathOperations:
    PI = 3.14159
    
    def __init__(self, value):
        self.value = value
    
    # Instance method
    def square(self):
        return self.value ** 2
    
    @classmethod
    def from_string(cls, num_str):
        return cls(float(num_str))
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathOperations.factorial(n - 1)

# Using different method types
math_obj = MathOperations(5)
print(math_obj.square())                    # 25

math_obj2 = MathOperations.from_string("10")
print(math_obj2.value)                      # 10.0

print(MathOperations.is_even(4))            # True
print(MathOperations.factorial(5))           # 120
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nExercise 1: Create a Bank Account class")
        print("Implement a class with deposit, withdraw, and balance check methods")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            return "Invalid withdrawal amount"
    
    def check_balance(self):
        return f"Account balance: ${self.balance}"
    
    def __str__(self):
        return f"Account {self.account_number} ({self.owner_name}): ${self.balance}"

# Test the BankAccount class
account = BankAccount("12345", "Alice Smith", 1000)
print(account.deposit(500))      # Deposited $500. New balance: $1500
print(account.withdraw(200))     # Withdrew $200. New balance: $1300
print(account.check_balance())   # Account balance: $1300
        """)
        
        print("\nExercise 2: Create a Vehicle hierarchy")
        print("Implement base Vehicle class and Car, Motorcycle subclasses")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def drive(self, miles):
        self.odometer += miles
        return f"Drove {miles} miles. Total: {self.odometer} miles"
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def honk(self):
        return "Beep beep!"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def honk(self):
        return "Honk honk!"
    
    def open_trunk(self):
        return "Trunk opened"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def honk(self):
        return "Beep!"
    
    def do_wheelie(self):
        return "Doing a wheelie!"

# Test the vehicle hierarchy
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Harley", "Sportster", 2021, 1200)

print(car.get_info())        # 2022 Toyota Camry
print(car.honk())            # Honk honk!
print(car.drive(100))        # Drove 100 miles. Total: 100 miles

print(motorcycle.get_info()) # 2021 Harley Sportster
print(motorcycle.honk())     # Beep!
print(motorcycle.do_wheelie()) # Doing a wheelie!
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "What is the purpose of __init__ method?",
                "options": ["a) Destroy object", "b) Initialize object", "c) Print object", "d) Compare objects"],
                "answer": "b"
            },
            {
                "question": "What does 'self' refer to in a class method?",
                "options": ["a) The class itself", "b) The current instance", "c) The parent class", "d) Nothing special"],
                "answer": "b"
            },
            {
                "question": "Which keyword is used to inherit from a parent class?",
                "options": ["a) inherits", "b) extends", "c) implements", "d) class Child(Parent):"],
                "answer": "d"
            },
            {
                "question": "What is polymorphism?",
                "options": ["a) Creating many objects", "b) Same interface, different implementations", "c) Hiding data", "d) Multiple inheritance"],
                "answer": "b"
            },
            {
                "question": "Which special method is called by print()?",
                "options": ["a) __print__", "b) __str__", "c) __repr__", "d) __display__"],
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
            print("🎉 Perfect score! You've mastered OOP concepts!")
        else:
            print("Keep practicing! Review classes, inheritance, and polymorphism.")
            
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
