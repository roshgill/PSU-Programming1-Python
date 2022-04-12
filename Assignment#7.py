"Fairly complex while loop usage"

#A.

i = 0

while (i < 5):
    count = 0
    count2 = i
    while(count <= count2):
        print("*", end=" ")
        count = count + 1
    print("\n")
    i = i + 1

#B. 

i = 1
space_counter = 5

while (i <= 5):
    print_space = space_counter - i
    printer = 0
    while(printer < print_space):
        print(" ", end=" ")
        printer = printer + 1
    printer = 0
    while(printer < i):
        print("*", end=" ")
        printer = printer + 1
    print("\n")
    i = i + 1

#C.

i = 1

while(i <= 5):
    print_at_num = 5 - i
    counter = 0
    while (counter < 5):
        if (counter == print_at_num):
            counter2 = counter
            while (counter2 < 5):
                print("*", end="  ")
                counter2 = counter2 + 1
            break
        print(" ", end=" ")
        counter = counter + 1
    print("\n")
    i = i + 1

#D.

i = 1
space_counter = 9

while (i <= 9):
    print_space = space_counter - i
    printer = 0
    while(printer < print_space):
        print(" ", end=" ")
        printer = printer + 1
    printer = 0
    while(printer < i):
        print("*", end=" ")
        printer = printer + 1
    print("\n")
    i = i + 2
