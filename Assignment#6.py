"Learned how to use loops inside other loops"

#A. Print Specific Number Pattern in Python

i = 1

while(i <= 9):
    substitute = i
    second_counter = 0
    while(second_counter < substitute):
        print(substitute , end=" ")
        second_counter = second_counter + 1
    print("\n")
    i = i + 1
print("\n")

#B. Print Specific Number Pattern in Python

i = 1

while(i <= 5):
    count = i
    s_counter = 1
    while (s_counter <= count):
        print(s_counter , end=" ")
        s_counter = s_counter + 1
    print("\n")
    i = i + 1
print("\n")

#C. Print Specific Number Pattern in Python

i = 1

while(i <= 5):
    
    count = i
    sub_count = count
    s_counter = 0
    
    while (s_counter < count):
        print(sub_count , end=" ")
        s_counter = s_counter + 1
        sub_count = sub_count - 1
    print("\n")
    i = i + 1