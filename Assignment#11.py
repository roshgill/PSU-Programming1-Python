"Learned how to create functions"

#1. Write a Python function to find the Max of three numbers.

def max_function(num1,num2,num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max

num1 = (int(input("Input number: ")))
num2 = (int(input("Input number: ")))
num3 = (int(input("Input number: ")))
max_number = max_function(num1,num2,num3)
print(max_number, "\n")

#2. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#xpected Output : 20

def sum_numbers(list1):
    summed_up = 0
    for i in list1:
        summed_up += i
    return summed_up

list1 = [8,2,3,0,7]
summed_up = sum_numbers(list1)
print(summed_up, "\n")


#3. Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336

def multiply_numbers(list2):
    multiply_up = 1
    for i in list2:
        multiply_up *= i
    return multiply_up

list2 = [8,2,3,-1,7]
multiplied_up = multiply_numbers(list2)
print(multiplied_up, "\n")


#4. Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reversing_string(str1):
    reverse = ''
    for i in str1:
        reverse = i + reverse
    return reverse

str1 = (str(input("Please input a string: ")))
reversed = reversing_string(str1)
print(reversed, "\n")


#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument

def factorial_number(num1):
    factorial_number = 1
    num1 = num1 + 1

    for i in range(1,num1):
        factorial_number = i * factorial_number 
    print("factorial of given number is", factorial_number, "\n")

factorial = int(input("Please input a number for factorial caluclation: "))
factorial_number(factorial)


#6. Write a Python function to check whether a number is in a given range

def range_checker(num2):
    a = (int(input("Please input number first range parameter")))
    b = (int(input("Please input number second range parameter")))
    
    if num2 in range(a,b):
        print("number is in range")
    else:
        print("number is not in range")

num2 = (int(input("Please input number to check if its in range")))
range_checker(num2)


#7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

def letter_calc(str3):
    upper = 0
    lower = 0
    for i in str3:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
    print ("No. of Upper case characters : ", upper)
    print ("No. of Lower case characters : ", lower)

str3 = (str(input("Please input a string: ")))
letter_calc(str3)


#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique(list3):
  list = []
  for i in list3:
    if i not in list:
      list.append(i)
  return list

list3 = [1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
print(unique(list3))



#9. Write a Python function that takes a number as a parameter and check the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def prime_checker(num11):
    prime_checker = 0
    i = 0

    if num11 <= 1:
        print("Number is not a prime number")
    elif num11 == 2:
        print("Number is a prime number")
    else:
        for i in range(2, num11):
            if num11 % i == 0:
                print("Number is not a prime number")
                prime_checker = prime_checker + 1
                break 
        if prime_checker == 0:
            print("Number is a prime number", "\n")
        print("\n")

num11 = (int(input("Please input number to check if its prime or not: ")))
prime_checker(num11)

#10. Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]

def even_checker(list55):
    count = 0
    for i in list55:
        if i % 2 == 0:
            print(i)
    print("\n")
    
list55 = [1,2,3,4,5,6,7,8,9,10]
even_checker(list55)