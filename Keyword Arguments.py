# keyword arguments = unlike positional arguments, they are preceded with an identifier and the order doesn't matter

def hello(first_name, last_name, age):    # positional arguments
    print('Hello ' + first_name + ' ' + last_name)
    print('You are ' + str(age) + ' years old')


def hello2(last_name='Gaidai', first_name='Andrew', age=21):    # keyword arguments
    print('Hello ' + first_name + ' ' + last_name)
    print('You are ' + str(age) + ' years old')


hello('Andrew', 'Gaidai', 21)
hello2()
