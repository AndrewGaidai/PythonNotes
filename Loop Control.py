while True:
    name = input('Enter your name: ')
    if name !="":
        break    # break = terminate the loop

phone_number = '123-456-789'

for i in phone_number:
    if i == "-":
        continue    # continue = skip to the next iteration of the loop
    print(i, end='')

for i in range(1, 21):
    if i == 13:
        pass    # pass = does nothing, acts like a placeholder
    else:
        print(i)

