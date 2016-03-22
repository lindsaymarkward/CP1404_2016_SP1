__author__ = 'Lindsay Ward'

"""
Write:
Ask the user for their subjects, one by one
until they enter ''
print them

Like: You are doing CP1404, CP1406, CU1010

"""

subjects = []
subject = input("Subject: ")
while subject != '':
    subjects.append(subject)
    subject = input("Subject: ")
print("You are doing ", end='')

# print subjects with no comma after the last one

# for subject in subjects[:-1]:
#     print(subject, ",", sep='', end=' ')
# if subjects:
#     print(subjects[-1])
# or just use:

print(", ".join(subjects))

