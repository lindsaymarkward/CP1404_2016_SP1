__author__ = 'Lindsay Ward'


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
