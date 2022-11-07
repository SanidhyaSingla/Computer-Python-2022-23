"""
Class division on the bases of marks
Division A = 80-100
Division B = 60-79
Division C = 40-59
Division D = 0-39
"""

marks = int(input("Please enter the marks obtained:"))

if marks <= 100 or marks >= 80:
    print("You got DIVISION A")

if marks <= 79 or marks >= 60:
    print("You got DIVISION B")

if marks <= 59 or marks >= 40:
    print("You got DIVISION C")

if marks <= 39 or marks >= 0:
    print("You got DIVISION D")
