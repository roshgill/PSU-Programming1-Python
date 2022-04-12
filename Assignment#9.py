"Learned how to use lists and for loops"

#1. Write a Python program to sum all the items in a list.

number_list = [] 
i = (int(input("How many numbers would you like to enter: ")))
 
for x in range(0, i):
    num = (int(input('Please enter a number: ')))
    number_list.append(num)

i = 0
for count in number_list:
    i = i + count
print(i, "\n")

#2. Write a Python program to multiplies all the items in a list.

number_list2 = [] 
i = (int(input("How many numbers would you like to enter: ")))
 
for x in range(0, i):
    number = (int(input('Please enter a number: ')))
    number_list2.append(number)

i = 1
for count2 in number_list2:
    i = (i*count2)
print(i, "\n")

#3. Write a Python program to get the largest number from a list. (You should not use max function but loop)

number_list3 = [] 
i = (int(input("How many numbers would you like to enter: ")))
 
for x in range(0, i):
    numbers = (int(input('Please enter a number: ')))
    number_list3.append(numbers)

count3 = 1
i = 0
largest_number = number_list3[0]
for count3 in number_list3:
    i = count3
    if largest_number < i:
        largest_number = i

print(largest_number, "\n")

#4. Write a Python program to get the smallest number from a list.  (You should not use min function but loop)

number_list4 = [] 
i = (int(input("How many numbers would you like to enter: ")))
 
for x in range(0, i):
    numberss = (int(input('Please enter a number: ')))
    number_list4.append(numberss)

count4 = 1
i = 0
smallest_number = number_list4[0]
for count4 in number_list4:
    i = count4
    if smallest_number > i:
        smallest_number = i

print(smallest_number, "\n")