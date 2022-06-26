# while 1 > 0:
# print('Help! I am stuck in a loop!')    # infinite loop

name = ''
while len(name) == 0:
    name = input('Enter your name: ')
print('Hello ' + name)

apples = 0
while apples < 10:
    apples += 1
    print(str(apples) + ' apple(s) in a bag')
print('The bag is full')
