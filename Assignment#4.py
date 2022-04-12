"Learned If-else statements."

#1. Write a program that takes a number.
#If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number.

num = (int(input("Input a number:")))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz", "\n")
elif num % 3 == 0:
    print("Fizz","\n")
elif num % 5 == 0:
    print("Buzz","\n")
else:
    print(num, "\n")   

#2. Write a Python program to display astrological sign for given date of birth.
#Expected Output:
#Input birthday: 15                                                      
#Input month of birth (e.g. march, july etc): may                        
#Your Astrological sign is : Taurus

bmonth = (str(input("Enter birth month:")))
bday = (int(input("Input birthday:")))

if bmonth == "January" or bmonth == "january":
    if bday >= 20:
        print("Aquarius", "\n")
    else:
        print("Capricorn","\n")
if bmonth == "February" or bmonth == "february":
    if bday >= 19:
        print("Pisces", "\n")
    else:
        print("Aquarius", "\n")
if bmonth == "March" or bmonth == "march":
    if bday >= 21:
        print("Aries", "\n")
    else:
        print("Pisces", "\n")
if bmonth == "April" or bmonth == "april":
    if bday >= 20:
        print("Taurus", "\n")
    else:
        print("Aries", "\n")
if bmonth == "May" or bmonth == "may":
    if bday >= 21:
        print("Gemini", "\n")
    else:
        print("Taurus", "\n")
if bmonth == "June" or bmonth == "june":
    if bday >= 21:
        print("Cancer", "\n")
    else:
        print("Gemini", "\n")
if bmonth == "July" or bmonth == "july":
    if bday >= 23:
        print("Leo", "\n")
    else:
        print("Cancer", "\n")
if bmonth == "August" or bmonth == "august":
    if bday >= 23:
        print("Virgo", "\n")
    else:
        print("Leo", "\n")
if bmonth == "September" or bmonth == "september":
    if bday >= 23:
        print("Libra", "\n")
    else:
        print("Virgo", "\n")
if bmonth == "October" or bmonth == "october":
    if bday >= 23:
        print("Scorpio", "\n")
    else:
        print("Libra", "\n")
if bmonth == "November" or bmonth == "november":
    if bday >= 22:
        print("Sagittarius", "\n")
    else:
        print("Scorpio", "\n")
if bmonth == "December" or bmonth == "december":
    if bday >= 22:
        print("Capricorn", "\n")
    else:
        print("Sagittarius", "\n")

#3. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
#Expected Output:
#Input the month (e.g. January, February etc.): july                     
#Input the day: 31                                                       
#Season is autumn

month = (str(input("Input the month:")))
day = (str(input("Input the day:")))

if month == "December" or month == "January" or month == "February":
    print("Winter", '\n')

elif month == "March" or month == "April" or month == "May":
    print("Spring", '\n')

elif month == "June" or month == "July" or month == "August":
    print("Summer", '\n')

elif month == "September" or month == "October" or month == "November":
    print("Autumn", '\n')
else:
    print("Incorrect Inputs, Retry", "\n")

#4. Write a Python program to check a triangle is equilateral, isosceles or scalene. 
#Note :
#An equilateral triangle is a triangle in which all three sides are equal.
#A scalene triangle is a triangle that has three unequal sides.
#An isosceles triangle is a triangle with (at least) two equal sides.
#Expected Output:
#Input lengths of the triangle sides:                                    
#x: 6                                                                    
#y: 8                                                                    
#z: 12                                                                   
#Scalene triangle

x = (float(input("Input first angle length:")))
y = (float(input("Enter second angle length:")))
z = (float(input("Enter third angle length:")))

if x == y or x == z:
    if x == z and x == y:
        print("Equilateral triangle", "\n")
    else:
        print("Isosceles triangle", "\n")
elif y == z:
    print("Isosceles triangle", "\n")
else:
    print("Scalence triangle", "\n")    

#5. Write a Python program to check a string represent an integer or not. 
#Expected Output:
#Input a string: Python                                                  
#The string is not an integer

str = (str(input("Input a string comprised of numbers:")))
i = 0
str2 = "0123456789"
final = 0

while i < len(str):
    counter = 0
    j = 0
    while j != 10:
        if str[i] == str2[j]:
            counter += 1
            j += 1
        else:
            j += 1
    if counter != 1:
        final += 1
    i += 1

if final == 0:
    print("The String represents an intger", "\n")
else:
    print("The String is not an integer", "\n")