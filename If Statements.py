# If Statement = a block of code that executes only if it's condition is True

age = int(input('How old are you? '))

if age < 18:
    print('You are a child')
elif age >= 18:
    print('You are an adult')
elif age == 21:
    print('You are as old as me')
else:
    print('How is that even possible?')
