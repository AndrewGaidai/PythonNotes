# Tuples are ordered and unchangeable

student = ('Andrew', 21, 'Male')
print(student.count('Andrew'))
print(student.index(21))

for i in student:
    print(i)

if 'Andrew' in student:
    print('Andrew is here')
    