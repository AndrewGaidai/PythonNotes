# Logical Operators (and, or, not) = used to check 2+ conditional statements

temp = int(input('What is the temperature outside? '))

if temp >= 0 and temp <= 30:    # and - both need to be True
    print('The temperature is good, go outside!')
elif temp <= 0 or temp >= 30:     # or - one needs to be True
    print('The temperature is bad, stay home!')
elif not(temp > 0):    # not - reverses condition
    print('The temperature is negative')
