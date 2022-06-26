# Slicing = creating a substring by extracting elements from another string

name = 'Andrew Gaidai'    # A = 0, n = 1, d = 2, r = 3, etc.

first_name = name[:6]
print(first_name)

last_name = name[7:]
print(last_name)

funky_name = name[::2]    # start : end : step
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

website1 = 'https://google.com'
website2 = 'https://wikipedia.com'
slice = slice(8, -4)
print(website1[slice])
print(website2[slice])
