__author__ = 'Lindsay Ward'

# no exception handling
# age = int(input("Age: "))
# print("Next year you will be", age + 1)


def main():
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Invalid (must be >= 0)")
            else:
                valid_input = True
        except ValueError:  # or just  except:
            print("Invalid (not an integer)")
    print("Next year you will be", age + 1)


def add_one_to(value):
    """
    Add one to a value
    :param value: value to add one to
    :return: one more than the value
    """
    return value + 1


main()
