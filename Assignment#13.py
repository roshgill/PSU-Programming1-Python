"Learned how to use dictionaries"

def add_key_dictionary():
    main_dictionary = {0:10, 1:20}
    print(main_dictionary)
    main_dictionary.update({2:30})
    print(main_dictionary)
    print("\n\n")

add_key_dictionary()

def concat_dictionaries():
    main_dictionary1 = {0:10, 1:20}
    main_dictionary2 = {5:100, 7:200}
    main_dictionary3 = {8:6, 9:54}
    main_dictionary4 = {98:104, 2:201}
    main_dictionary5 = {65:10, 432:20}
    new_dictionary = {}

    for i in (main_dictionary1, main_dictionary2, main_dictionary3, main_dictionary4, main_dictionary5):
        new_dictionary.update(i)
        print(new_dictionary)
    print("\n\n")

concat_dictionaries()

def key_dictionary_checker(key, dictionary_test):
    if key in dictionary_test:
        print(str(key) + " is in the dictionary")
    else:
        print("This key is not in the dictionary")

dictionary_test = {100:100, 2:200, 3:300}
key = 300
key_dictionary_checker(key, dictionary_test)