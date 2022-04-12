"Learned string manipulation"

#1. Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

str1 = str(input("Please enter first string: "))
str2 = str(input("Please enter second string: "))

print((str2[:2]+str1[2:]) + " " + (str1[:2]+str2[2:]))
print("\n")

#2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
#If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given 
#string is less than 3, leave it unchanged.
#    Sample String : 'abc'
#     Expected Result : 'abcing'
#     Sample String : 'string'
#     Expected Result : 'stringly'
 
str3 = (str(input("Please input string: ")))

if len(str3) < 3:
    print("Please enter a word with more than 2 characters")
elif str3[-3:] == "ing":
    newstr = str3[:] + "ly"
    print(newstr)
else:
    newstr = str3[:] + "ing"
    print(newstr) 
print("\n")

#3. Write a Python program to find the first appearance of the substring 
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', 
# replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'

str4 = (str(input("Please input a string: ")))

find1 = str4.find("not")
find2 = str4.find("poor")
mainlen = len(str4)

if find1 > 0 and find2 > 0 and find1 < find2:
    str4 = str4[:(find1)] + "good" + str4[(find2)+4:]
    print(str4)
else:
    print(str4) 
print("\n")

#4. Write a Python program to remove the nth index character from a nonempty string.

str5 = (str(input("Please input a string: ")))
index = (int(input("Please enter nth index character to remove: ")))

if index > len(str5):
    print(str5)
else:
    print(str5[:index] + str5[index+1:])
print("\n")

#5. Write a Python script that takes input from the user and displays that input back in 
# upper and lower cases.

str6 = (str(input("Please input a string: ")))

print(str6.upper())
print(str6.lower())
print("\n")

#6. Write a Python function to create the HTML string with tags around the word(s).
#      Sample function and result :
#      input: 'i', 'Python'     
#
#      output: '<i>Python</i>'
#
#      input: 'b', 'Python Tutorial'
#
#      output: <b>Python Tutorial </b>

str7 = (str(input("Please enter string: ")))
html = (input("Please enter the HTML char: "))

print("<" + html + ">" + str7 + "</" + html + ">")
print("\n")