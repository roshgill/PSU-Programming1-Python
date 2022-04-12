"""Learned how to get user inputs, mildly complex mathematical 
calculations, and mildy complexy printing"""

"""Python math module is defined as the most famous mathematical functions, 
which includes trigonometric functions, representation functions, 
logarithmic functions, etc."""
import math

#1. Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = (str(input("Enter your name:")))
age = (int(input("Enter the age you will be once your birthday has passed this year:")))

years_left_until_hundred = 100 - age
year_100 = 2021 + years_left_until_hundred
print(name, "will be a hundred years of age in", year_100, "\n", "\n")

#2. Write a Python program to print the following string in a specific format (see the output).

print("Twinkle, twinkle, little star")
print("      How I wonder what you are!")
print("            Up above the world so high,")
print("            Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("      How I wonder what you are", "\n")

#3. Write a Python program which accepts the radius of a circle from the user and compute the area

radius_of_circle = (float(input("Input the radius of the circle:")))
radius_of_circle = (radius_of_circle**2)
area_of_circle = math.pi * radius_of_circle
print("The area of the circle is:", area_of_circle, "\n")

#4. Write a Python program which accepts the user's first and last name and print them in reverse order
# with a space between them

first_name = (str(input("Please print your first name:")))
last_name = (str(input("Please input your last name:")))
print("Your name in reverse order is " + last_name + ' ' + first_name, "\n")

#5. Write a Python program to draw US Flag as follows

print("*  *  *  *  *  *  ======================================")
print("  *  *  *  *  *   ======================================")
print("*  *  *  *  *  *  ======================================")
print("  *  *  *  *  *   ======================================")
print("*  *  *  *  *  *  ======================================")
print("  *  *  *  *  *   ======================================")
print("*  *  *  *  *  *  ======================================")
print("  *  *  *  *  *   ======================================")
print("*  *  *  *  *  *  ======================================")
print("========================================================")
print("========================================================")
print("========================================================")
print("========================================================", "\n")