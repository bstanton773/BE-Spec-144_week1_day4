import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


#############
# Recursion #
#############

# Call Stack
# The call stack is a memory structure that tracks active function calls in a program, operating on a Last In, First Out (LIFO) basis.
import time



line_break()



line_break()


# Recursive functions are functions that call themselves, typically with smaller inputs, until they reach a base case.
# Base Case - Determines when the Recursion should stop. Without a base case, the function will call itself infinitely

# Factorial Function
# n! = 1 if n = 0, else n * (n - 1)!



line_break()

# File System - Searching for a document in a folder


file_system = [
    [
        "whiteboards",
        [
            "day1",
            "whiteboard1.py",
            "test1.py"
        ],
        [
            "day2",
            "whiteboard2.py",
            "test2.py"
        ],
    ],
    [
        "my-api",
        "requirements.txt",
        "README.md",
        [
            "app",
            "__init__.py",
            "routes.py",
            "models.py"
        ]
    ],
    "notes.py",
    [
        "personal",
        [
            "photos",
            "vacation.jpg",
            "cover.jpg"
        ],
        [
            "job_search",
            "resume.pdf",
            "cover-letter.pdf"
        ]
    ]
]



line_break()


# Potential Pitfalls
# Stack Overflow + Extra Overhead

# fibonacci - 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc
# fib(n) = fib(n-1) + fib(n-2) if n > 1, else fib(n) = 1



# In Class Exercise

# print('''
# You are working on a file management application, and your task is to implement a function that calculates the total size of all files within folder. This function should recursively traverse through the folders and sum up the sizes of all files encountered.

# 1. Define a Python function named **`calculate_total_folder_size`** that takes a single parameter: **`folder`** (a list representing the folder structure with file sizes).
# 2. Implement the recursive logic inside the **`calculate_total_folder_size`** function to traverse through the nested folders and calculate the total size of all files.
# 3. Use the provided file system analogy to guide your implementation.
# 4. Upon encountering a file (leaf node), add its size to a running total.
# 5. Recursively traverse through subfolders to include their files' sizes in the total.
# 6. Return the total size of all files in the file system structure.
# ''')


file_system = [
    [10, 20, 30],  # Folder 1 with files of sizes 10, 20, and 30
    [15, [25, 35]],  # Folder 2 with a file of size 15, and another folder with files of size 25, and 35
    40,  # File 1 with size 40
    [45, [55, 65]],  # Folder 3 with file of sizes 45, and another folder with file sizes 55, and 65
    70  # File 2 with size 70
]

