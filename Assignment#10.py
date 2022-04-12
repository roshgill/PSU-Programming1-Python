"Putting all basic skills together"

import math
# 1. Write a python program to print the square of all numbers from 0 to 10

for i in range(0,11):
    print(math.sqrt(i))
print("\n")


# 2. Write a python program to find the sum of all even numbers from 0 to 10

i = 0
evensum = 0
for i in range(0,11):
    if i % 2 == 0:
        evensum = i + evensum
print("The sum of all even numbers is:", evensum, "\n")


#3. Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’

a = (int(input("Please input first number: ")))
b = (int(input("Please input second number: ")))
c = (int(input("Please input third number: ")))
divisble_number = 0
i = 0

if a > b:
    increment = -1
    temp_a = a - 1
else:
    increment = 1
    temp_a = a + 1

for i in range(temp_a,b,increment):
    if i % c == 0:
        divisble_number += 1
print(divisble_number, "numbers are divisble by", c, "between", a, "and", b, "\n")

#4. Write a python program to get the following output

#1-----99

#2-----98

#3-----97

#. .

#. .

#. .

#98-----2

#99-----1

i = 0
for i in range(1,100):
    second_number = 100 - i
    print(i, end="")
    print("-----", end="")
    print(second_number)
print("\n")


#5. Write a python program to read four numbers (representing the four octets of an IP) and print the next five IP address

#Eg:

#Input:

#192 168 255 252

#----------Output---------

#192 168 255 253

#192 168 255 254

#192 168 255 255

#192 169 0 0

#192 169 0 1

a = (int(input("Please input first octet of an IP: ")))
b = (int(input("Please input second octet of an IP: ")))
c = (int(input("Please input third octet of an IP: ")))
d = (int(input("Please input fourth octet of an IP: ")))

for i in range(0,5):
    d = d + 1
    if d > 255:
        if c == 255:
            b = b + 1
            c = 0
            d = 0
        else:
            c = c + 1
            d = 0
    print(a, b, c, d)
print("\n")

#6. Write a python program to print the factorial of a given number

fact = (int(input("Please input number: ")))
i = 0
factorial_number = 1
fact = fact + 1

for i in range(1,fact):
    factorial_number = i * factorial_number 

print("factorial of given number is", factorial_number, "\n")

#7. Write a python program to print the first 10 numbers Fibonacci series

term_0 = 0
term_1 = 1
count = 0

print(term_0, "\n")
print(term_1, "\n")

for count in range(1,9):
    final_count = term_0 + term_1
    print(final_count, "\n")
    term_0 = term_1
    term_1 = final_count

print("\n")

#8. Write a python program to read a number and print a right triangle using "*"

#Eg :

#Input : 5

#----------Output---------

#*

#* *

#* * *

#* * * *

#* * * * *

numbered = (int(input("Please input number: ")))
numbered = numbered + 1
i = 0

for i in range(1, numbered):
    increment = 0
    while (increment < i):
        print("*", end=" ")
        increment = increment + 1
    print("\n")
print("\n")


#9. Write a python program to check given number is prime or not

prime = (int(input("Please input a number: ")))
prime_checker = 0
i = 0

if prime <= 1:
    print("Number is not a prime number")
elif prime == 2:
    print("Number is a prime number")
else:
    for i in range(2, prime):
        if prime % i == 0:
            print("Number is not a prime number")
            prime_checker = prime_checker + 1
            break 
    if prime_checker == 0:
        print("Number is a prime number", "\n")
print("\n")
        
#10. Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there.

prime_counter = 0
prime_verify = 0
i = 0

print(2)
prime_counter += 1

for i in range(3,101):
    prime_checker = i - 1
    not_prime_verify = 0
    for x in range(prime_checker,1,-1):
        if i % x == 0:
            not_prime_verify += 1
            break
    if not_prime_verify == 0:
        print(i)
        prime_counter += 1
print("There are", prime_counter, "prime numbers between 0-100", "\n")


#11. a, b, c = 0, 0, 0 . Write a python program to print all permutations using those three variables
#Output : 000 , 001 ,002, 003, 004, 0005 ,006, 007, 008, 009, 010, 011 …… 999

first_d = 0

while(first_d < 10):
    second_d = 0
    while(second_d < 10):
        third_d = 0
        while(third_d < 10):
            print(first_d, end="")
            print(second_d, end="")
            print(third_d, end=" ")
            third_d += 1
        second_d += 1
    first_d += 1

print("\n")


#12.

#From given list

#gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28, “Speakers”, 27.00,
#“Television”, 1000, “Laptop Case”, “Camera Lens”]

#a)create separate lists of strings and numbers.
 
#b)Sort the strings list in ascending order
 
#c)Sort the strings list in descending order
 
#d)Sort the number list from lowest to highest
 
#e)Sort the number list from highest to lowest

gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
numbers_list = []
strings_list = []

for x in gadgets:
    if type(x) == int:
        numbers_list.append(x)
    elif type(x) == float:
        numbers_list.append(x)
    else:
        strings_list.append(x)

print("The numbers list:", numbers_list)
print("The strings list:", strings_list)

sorted_strings_list = sorted(strings_list)
print(sorted_strings_list)

reverse_sorted_strings_list = sorted(strings_list, reverse=True)
print(reverse_sorted_strings_list)

sorted_numbers_list = sorted(numbers_list)
print(sorted_numbers_list)

reverse_sorted_numbers_list = sorted(numbers_list, reverse=True)
print(reverse_sorted_numbers_list)

print("\n")
#13.
#Get first, second best scores from the list.
#List may contain duplicates.
#Ex: [86,86,85,85,85,83,23,45,84,1,2,0] => should get 86, 85 """

numbered_list = [86,86,85,85,85,83,23,45,84,1,2,0]
new_sorted_numbered_list = sorted(numbered_list)

highest_num = new_sorted_numbered_list[-1]
new_sorted_numbered_list.remove(highest_num)

while highest_num == new_sorted_numbered_list[-1]:
    new_sorted_numbered_list.remove(new_sorted_numbered_list[-1])
second_highest_num = new_sorted_numbered_list[-1]

print(highest_num, second_highest_num)