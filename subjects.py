__author__ = 'Lindsay Ward'

# subjects = []
subjects = ['CP1404', 'CP1406', 'MA1000', 'CP2404']

# subject = input("Subject: ")
# while subject != '':
#     subjects.append(subject)
#     subject = input("Subject: ")

# print(subjects)

for subject in subjects:
    # print(subject)
    print(subject, end=" - ")
    # if subject[:2] == "CP1":
    if subject.startswith("CP"):
        print("Yeah!")
    else:
        print("Ohhh...")

