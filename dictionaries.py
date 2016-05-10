"""
CP1404 in-class examples: dictionaries
"""
__author__ = 'Lindsay Ward'

numbers = [1, 2, 3]

phonebook = {"Bob": "123456", "Jane": "755519"}
phonebook["T Mart"] = "123456"

print(phonebook)
print(phonebook["Jane"])

for name in phonebook:
    phonebook[name] = "47" + phonebook[name]
    print(name, " - ", phonebook[name])

print("47123456" in phonebook.values())

for name in sorted(list(phonebook.keys())):
    print(name, " - ", phonebook[name])

phonebook["Mr. T"] = phonebook["T Mart"]
del phonebook["T Mart"]

phonebook["Mr. T"] = phonebook.pop("T Mart")

print(phonebook)

new_ones = {"Jane": "000", "Derek": "911"}

phonebook.update(new_ones)

print(phonebook)

for name, number in phonebook.items():
    name += " Jr."
    number = "47" + number
    print(name, number)

print(phonebook)

words = "bob is hi no is bob".split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

print(word_counts.get("t", 0))

ages_dict = {"Billy": 21, "JJ": 3, "Jack": 156}

name = input("Name: ")
age = int(input("Age: "))
ages_dict[name] = age

for name, age in ages_dict.items():
    print("{:>8} - {:<3}".format(name, age))

