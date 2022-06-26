# **kwargs = a parameter that will pack all arguments into a dictionary

def hello(**kwargs):
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')


hello(title='Mr.', first='Andrew', last='Gaidai')