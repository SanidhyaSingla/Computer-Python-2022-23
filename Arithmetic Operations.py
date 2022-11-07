"""
Arithmetic Operations
+ for addition
- for subtraction
* for multiplication
** for power
// for floor division(Getting quotient without float(decimal))
/ for normal division(Getting quotient with float(decimal))
"""
a = int(input("Please enter the first number:"))
b = int(input("Please enter the second number:"))
choice = input(
    "Please choose from the following Arithmetic Operations:\n+ for addition\n- for subtraction\n* for multiplication\n** for power\n// for floor division(Getting quotient without float(decimal))\n/ for normal division(Getting quotient with float(decimal))\nYour choice:")

if choice == "+":
    print(a + b)

elif choice == "-":
    print(a - b)

elif choice == "*":
    print(a * b)

elif choice == "**":
    print(a ** b)

elif choice == "//":
    print(a // b)

elif choice == "/":
    print(a / b)
