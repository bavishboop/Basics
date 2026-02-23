"""
Algorithms and Problem Solving Module
Covers fundamental algorithms, problem-solving strategies, and computational thinking
"""

class AlgorithmsModule:
    def __init__(self):
        self.name = "Algorithms and Problem Solving"
        
    def display_content(self):
        print("\n" + "="*60)
        print("📚 ALGORITHMS AND PROBLEM SOLVING")
        print("="*60)
        
        print("\n🔹 PROBLEM-SOLVING STRATEGIES:")
        print("• Understand the problem thoroughly")
        print("• Break down into smaller subproblems")
        print("• Plan the solution before coding")
        print("• Start with a simple approach")
        print("• Test with different inputs")
        print("• Optimize for time and space complexity")
        
        print("\n🔹 SEARCHING ALGORITHMS:")
        print("• Linear Search: Check each element sequentially")
        print("• Binary Search: Divide and conquer on sorted data")
        print("• Time Complexity: Linear O(n), Binary O(log n)")
        
        print("\n🔹 SORTING ALGORITHMS:")
        print("• Bubble Sort: Compare adjacent elements")
        print("• Selection Sort: Find minimum and swap")
        print("• Insertion Sort: Build sorted array one by one")
        print("• Merge Sort: Divide, sort, and merge")
        print("• Quick Sort: Partition and recursively sort")
        
        print("\n🔹 RECURSION:")
        print("• Function calls itself")
        print("• Base case to stop recursion")
        print("• Recursive case to continue")
        print("• Stack memory usage")
        print("• Useful for divide and conquer problems")
        
        print("\n🔹 DYNAMIC PROGRAMMING:")
        print("• Break complex problems into subproblems")
        print("• Store results of subproblems (memoization)")
        print("• Build up solution from smaller problems")
        print("• Fibonacci, knapsack, longest common subsequence")
        
        print("\n🔹 GREEDY ALGORITHMS:")
        print("• Make locally optimal choices")
        print("• Hope for global optimum")
        print("• Not always optimal, but often good")
        print("• Fractional knapsack, activity selection")
        
        print("\n🔹 TIME COMPLEXITY:")
        print("• O(1): Constant time")
        print("• O(log n): Logarithmic time")
        print("• O(n): Linear time")
        print("• O(n log n): Linearithmic time")
        print("• O(n²): Quadratic time")
        print("• O(2^n): Exponential time")
        
    def show_examples(self):
        print("\n" + "="*60)
        print("💡 PRACTICAL EXAMPLES")
        print("="*60)
        
        print("\n🔹 Linear Search:")
        print("""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index i
    return -1  # Not found

# Test
numbers = [5, 3, 8, 1, 9, 2]
print(linear_search(numbers, 8))  # 2
print(linear_search(numbers, 7))  # -1
        """)
        
        print("\n🔹 Binary Search:")
        print("""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Test (requires sorted array)
sorted_numbers = [1, 2, 3, 5, 8, 9]
print(binary_search(sorted_numbers, 8))  # 4
print(binary_search(sorted_numbers, 7))  # -1
        """)
        
        print("\n🔹 Bubble Sort:")
        print("""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test
numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers.copy()))  # [11, 12, 22, 25, 34, 64, 90]
        """)
        
        print("\n🔹 Recursion Examples:")
        print("""
# Factorial using recursion
def factorial(n):
    if n <= 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive case

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n  # Base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Test
print(factorial(5))     # 120
print(fibonacci(6))     # 8
        """)
        
        print("\n🔹 Dynamic Programming - Fibonacci:")
        print("""
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    # Create array to store results
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Memoization version
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Test
print(fibonacci_dp(10))      # 55
print(fibonacci_memo(10))   # 55
        """)
        
        print("\n🔹 Greedy Algorithm - Activity Selection:")
        print("""
def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_end = float('-inf')
    
    for activity in activities:
        start, end = activity
        if start >= last_end:
            selected.append(activity)
            last_end = end
    
    return selected

# Test: (start_time, end_time)
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
selected = activity_selection(activities)
print(selected)  # Maximum non-overlapping activities
        """)
        
        print("\n🔹 Two Pointers Technique:")
        print("""
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []  # No solution

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Test
sorted_arr = [1, 2, 3, 4, 6, 8, 11]
print(two_sum(sorted_arr, 10))  # [2, 5] (3 + 7 = 10)

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # [5, 4, 3, 2, 1]
        """)
        
    def interactive_exercise(self):
        print("\n" + "="*60)
        print("🎯 INTERACTIVE EXERCISE")
        print("="*60)
        
        print("\nExercise 1: Find the maximum element in an array")
        print("Write a function to find the maximum value in a list")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def find_max(arr):
    if not arr:
        return None
    
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Alternative using built-in
def find_max_builtin(arr):
    return max(arr) if arr else None

# Test
numbers = [3, 7, 2, 9, 1, 5]
print(find_max(numbers))          # 9
print(find_max_builtin(numbers))  # 9
        """)
        
        print("\nExercise 2: Check if a string is a palindrome")
        print("Write a function to check if a string reads the same forwards and backwards")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Alternative using slicing
def is_palindrome_slicing(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

# Test
print(is_palindrome("racecar"))        # True
print(is_palindrome("A man, a plan...")) # True
print(is_palindrome("hello"))          # False
        """)
        
        print("\nExercise 3: Count frequency of elements")
        print("Write a function to count how many times each element appears")
        
        input("\nPress Enter to see the solution...")
        
        print("\n💡 SOLUTION:")
        print("""
def count_frequencies(arr):
    frequency = {}
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# Alternative using collections.Counter
from collections import Counter

def count_frequencies_counter(arr):
    return Counter(arr)

# Test
numbers = [1, 2, 3, 2, 1, 4, 2, 5, 1]
print(count_frequencies(numbers))
# {1: 3, 2: 3, 3: 1, 4: 1, 5: 1}

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_frequencies_counter(words))
# Counter({'apple': 3, 'banana': 2, 'orange': 1})
        """)
        
    def run_quiz(self):
        print("\n" + "="*60)
        print("📝 QUICK QUIZ")
        print("="*60)
        
        questions = [
            {
                "question": "What is the time complexity of binary search?",
                "options": ["a) O(n)", "b) O(log n)", "c) O(n²)", "d) O(1)"],
                "answer": "b"
            },
            {
                "question": "Which sorting algorithm has the best average case complexity?",
                "options": ["a) Bubble Sort", "b) Selection Sort", "c) Merge Sort", "d) Insertion Sort"],
                "answer": "c"
            },
            {
                "question": "What is the main characteristic of a greedy algorithm?",
                "options": ["a) Always finds optimal solution", "b) Makes locally optimal choices", "c) Uses recursion", "d) Requires sorted input"],
                "answer": "b"
            },
            {
                "question": "What is the base case in recursion?",
                "options": ["a) The recursive call", "b) The condition that stops recursion", "c) The first case tested", "d) The final result"],
                "answer": "b"
            },
            {
                "question": "Which technique stores results of subproblems to avoid recomputation?",
                "options": ["a) Greedy approach", "b) Divide and conquer", "c) Dynamic programming", "d) Backtracking"],
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
            print("🎉 Perfect score! You've mastered algorithms and problem solving!")
        else:
            print("Keep practicing! Review searching, sorting, and complexity analysis.")
            
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
