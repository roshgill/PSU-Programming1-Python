"Learned how to use while loops"

#1. Write a Python program to get the Fibonacci series between 0 to 50

total_terms = (int(input("Please enter number of terms: ")))
term_0 = 0
term_1 = 1
count = 0

print(term_0, "\n")
print(term_1, "\n")

while count < total_terms:
    final_count = term_0 + term_1
    print(final_count, "\n")
    term_0 = term_1
    term_1 = final_count
    count = count + 1

#2. Write a Python program to print alphabet pattern 'D'

print("****", "\n")
print("*    *", "\n")
print("*    *", "\n")
print("*    *", "\n")
print("*   *", "\n")
print("****", "\n")


#3. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

int = 0
while(int < 6):
    if int == 3 or int == 6:
        int = int + 1
    else:
        print(int, "\n")
        int = int + 1

#4. Write a Python program to construct the following pattern, using a loop number

int = 1

while(int <= 9):
    count = int
    print_counter = 0
    while(print_counter < count):
        print (count , end="")
        print_counter = print_counter + 1
    print("\n")
    int = int + 1