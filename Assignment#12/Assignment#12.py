"Learned File handling"

#1. Write a Python program to read last n lines of a file.

def last_n_lines():
    n = (int(input("Please input the numbers of a file you would like to read in reverse: ")) * -1)
    open_file = open('sample_if.txt', "r")
    file = open_file.readlines()

    for line in file[n:]:
        print(line)
    open_file.close()

last_n_lines()
print("\n")

#2. Write a python program to find the longest words.

def longest_words():
    open_file = open('sample_if.txt')
    read_file = open_file.read()
    file = read_file.split()
    final_char = file[0]

    for i in file[1:]:
        if len(i) > len(final_char):
            final_char = i
    print("Longest word of is: " + final_char)
    open_file.close()

longest_words()
print("\n")

#3. Write a Python program to count the number of lines in a text file.

def count_lines():
    open_file = open('sample_if.txt', "r")
    read_file = open_file.readlines()
    count = 0

    for i in read_file[0:]:
        count += 1
    print("Number of lines in this file:", count)
    open_file.close()

count_lines()
print("\n")

#4. Write a Python program to count the frequency of words in a file.
# def frequency_words():
#     open_file = open('sample_if.txt')
#     read_file = open_file.read()
#     file = read_file.split()
#     duplicate_set = {}
#     for i in file[0:]:
#         duplicate_set.add(i)
#         for x in file[:]:
#     open_file.close()
# frequency_words()
# print("\n")

#5. Write a Python program to copy the contents of a file to another file

def copy_file():
    file_1 = open('sample_if.txt', 'r')
    file_2 = open('sample_2.txt','a')
    for words in file_1:
        file_2.write(words)
copy_file()