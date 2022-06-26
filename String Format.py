animal = 'cow'
item = 'moon'
print('The ' + animal + ' jumped over the ' + item)

print('The {} jumped over the {}'.format('cow', 'moon'))
print('The {1} jumped over the {0}'.format('cow', 'moon'))    # positional argument
print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))    # keyword argument

text = 'The {} jumped over the {}'
print(text.format(animal, item))

name = 'Andrew'
print('Hello, my name is {}'.format(name))
print('Hello, my name is {:<10}. Nice to meet you'.format(name))
print('Hello, my name is {:>10}. Nice to meet you'.format(name))
print('Hello, my name is {:^10}. Nice to meet you'.format(name))

number = 3.14159
print('The number pi is {:.2f}'.format(number))
