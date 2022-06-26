# Lists are used to store multiple items in a single variable

food = ['pizza', 'salad', 'ice cream', 'cake']
print(food)
print(food[0])

food[0] = 'sushi'
print(food)

food.append('cookie')
print(food)

food.remove('salad')
print(food)

food.pop()    # remove the last element
print(food)

food.insert(0, 'salad')
print(food)

food.sort()
print(food)

food.clear()    # remove all elements
print(food)