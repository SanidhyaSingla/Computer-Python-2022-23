# leap year Calculator

a = int(input("Please enter a year:"))

if a%4 == 0:
    print(a, "is a leap year")
else:
    print(a, "is not a leap year")