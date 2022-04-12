"Learned If-else statements."

#1. Write a Python program that reads two integers representing a month 
# and day and prints the season for that month and day.

month = (str(input("Input the month:")))
day = (str(input("Input the day:")))

if month == "December" or month == "January" or month == "February":
    print(month, '\n')
    print(day,'\n')
    print("Winter", '\n')

elif month == "March" or month == "April" or month == "May":
    print(month, '\n')
    print(day,'\n')
    print("Spring", '\n')

elif month == "June" or month == "July" or month == "August":
    print(month, '\n')
    print(day,'\n')
    print("Summer", '\n')

elif month == "September" or month == "October" or month == "November":
    print(month, '\n')
    print(day,'\n')
    print("Autumn", '\n')
else:
    print("Incorrect Inputs, Retry", "\n")

#2. Given three integers, print the smallest value.

int1 = (int(input("Input the first integer:")))
int2 = (int(input("Input the second integer:")))
int3 = (int(input("Input the third integer:")))

smallestint = int1
if (int2 < smallestint):
    smallestint = int2
if (int3 < smallestint):
    smallestint = int3
print(smallestint, "\n")

#3. For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero

x = (int(input("Enter an integer value:")))

if x > 0:
    print("1")
elif x < 0:
    print("-1")
else:
    print("0")

#4.Given three integers, determine how many of them are equal to each other.
# The program must print one of these numbers: 3 (if all are the same), 2 
# (if two of them are equal to each other and the third is different) or 0 
# (if all numbers are different).

int1 = (int(input("Input the first integer:")))
int2 = (int(input("Input the second integer:")))
int3 = (int(input("Input the third integer:")))
similar_counter = 0

if int1 == int2 and int1 != int3:
    similar_counter += 2
if int2 == int3 and int2 != int1:
    similar_counter += 2
if int3 == int1 and int3 != int2:
    similar_counter += 2
if int1 == int2 and int1 == int3:
    similar_counter += 3
print(similar_counter, "\n")

#5. Given the year number. You need to check if this year is a leap year.
# If it is, print LEAP, otherwise print COMMON.

year = (int(input("Enter the year:")))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP")
        else:
            print("COMMON")
    else:
        print("LEAP")
else:
    print("COMMON")

#6. Write a Python program to convert temperatures to and from celsius, fahrenheit.

tempstyle = (str(input("Please input if temp. is in celsius or fahrenheit:")))
temp = (float(input("Please inpute the temp value:")))

if tempstyle == "celsius":
    temp = (temp * 1.8) + 32
    print("Celsius to Farhenheit is:", temp)

elif tempstyle == "fahrenheit":
    temp = (temp - 32) * .5556
    print("Farenheit to Celsius is:", temp) 