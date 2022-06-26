# String (text)
name = 'Andrew'
print(type(name))
print('Hello, my name is', name)

# Integer (numerical)
age = 20
age += +1
print(type(age))
print('I am', age, "years old")
print('My age: ' + str(age))

# Float (numerical with a decimal portion)
height = 185.5
print(type(height))
print('My height is ' + str(height) + ' cm')

# Boolean (True or False)
human = True
print(type(human))
print('Am I human: ' + str(human))

# Multiple Assignments
name, age, height, human = 'Andrew', 21, 185.5, True
print(name, age, height, human)

Andrew = Nick = Daniel = John = 21
print(Andrew, Nick, Daniel, John)
