# Nested Loops = inner loop finishes all of it's iterations before the outer loop

rows = int(input('How many rows? '))
columns = int(input('How many columns? '))
symbol = input('Pick a symbol ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()
