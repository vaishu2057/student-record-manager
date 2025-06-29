"""Leap Year Check"""

year=int(input("enter year:"))
if(year%4==0):
    print("leap year")
else:
    print("non leap year")
    
    #Calculate electricity bill based on the following rules:

#For the first 100 units: ₹1.5/unit

#101 to 200 units: ₹2/unit

#Above 200 units: ₹3/unit

#If total bill exceeds ₹500, add ₹50 fixed charge

units = float(input("Enter units consumed: "))
total_bill = 0

if units <= 100:
    total_bill = units * 1.5
elif units <= 200:
    total_bill = (100 * 1.5) + (units - 100) * 2
else:
    total_bill = (100 * 1.5) + (100 * 2) + (units - 200) * 3

# Add fixed charge if total bill exceeds ₹500
if total_bill > 500:
    total_bill += 50

print("Total Electricity Bill: ₹", total_bill)

"""Grade Calculator
Given marks out of 100, print:

A (90–100)

B (80–89)

C (70–79)

D (60–69)

F (below 60)"""

marks=int(input("enter marks:"))
if(marks>=90 and marks<=100):
    print("A")
elif(marks>=80 and marks<=89):
    print("B")
elif(marks>=70 and marks<=79):
    print("C")
elif(marks>=60 and marks<=69):
    print("D")
else:
    print("F")
"""Triangle Type Checker
Take 3 side lengths. Check if they can form a triangle. If yes, determine:

Equilateral / Isosceles / Scal"""
side1=int(input("enter side1:"))
side2=int(input("enter side2:"))
side3=int(input("enter side3:"))
if(side1==side2==side3):
    print("equilateral triangle")
elif(side1==side2!=side3):
    print("isosceles triangle")
else:
    print("scalene triangle")