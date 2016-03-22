__author__ = 'Lindsay Ward'


# demo - using list of options to check input against
# choice = input("Choose: a, b, c or q: ").lower()
# while choice not in list("abcq"):
#     print("Error!")
#     choice = input("Choose: a, b, c or q: ").lower()
# print("Finished")

choice = input("Choose: a, b, c or q: ").lower()
while choice != 'q':
    if choice == 'a':
        print("One")
    elif choice == 'b':
        print("Two")
    elif choice == 'c':
        print("Three")
    else:
        print("Error")
    choice = input("Choose: a, b, c or q: ").lower()

print("-" * 20)
