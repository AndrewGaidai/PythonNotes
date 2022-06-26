# Dictionaries are changeable and unordered

capitals = {'USA': 'Washington DC',
            'China': 'Beijing',
            'Ukraine': 'Kyiv'}

print(capitals['Ukraine'])
print(capitals.get('Germany'))    # Not to encounter an error
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Boston'})
capitals.pop('China')

for key, value in capitals.items():
    print(key, value)
