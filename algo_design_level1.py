"""
=============================================================
  LEVEL 1 — Procedures and Functions (All students)
  Identify, write, and call basic subroutines.
=============================================================
"""

# ----------------------------------------------------------
# TASK 1A: Identify the difference
# ----------------------------------------------------------
# Below are two subroutines. One is a PROCEDURE, one is a FUNCTION.
# Read them, then answer (in the comments below):

def greet_student(name):
    print(f"Welcome to class, {name}!")


def square(number):
    return number * number


# YOUR ANSWERS (fill in the blanks):
# greet_student is a: procedure  because: it doesn't do any calculations
# square is a:        function  because: it does calculations


# ----------------------------------------------------------
# TASK 1B: Call them and observe the output
# ----------------------------------------------------------
# 1. Call greet_student with your own name.
# 2. Call square with the number 7 and PRINT the result.
# 3. Try printing the result of greet_student("Alex") — what do you notice?

# YOUR CODE HERE:

print(greet_student("Alex"))
print(square(7))


# ----------------------------------------------------------
# TASK 1C: Write your own function
# ----------------------------------------------------------
# Write a function called calculate_grade(score) that:
#   - Takes a numerical score as input
#   - Returns "A" if score >= 90
#   - Returns "B" if score >= 75
#   - Returns "C" if score >= 60
#   - Returns "F" otherwise
#


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


# Test your function (uncomment these lines when ready):
print(calculate_grade(95))   # Expected: A
print(calculate_grade(80))   # Expected: B
print(calculate_grade(62))   # Expected: C
print(calculate_grade(40))   # Expected: F
