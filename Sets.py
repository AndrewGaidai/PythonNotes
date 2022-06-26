# Sets are unordered and unindexed with no duplicate values

utensils = {'fork', 'spoon', 'knife'}
utensils.add('napkin')
utensils.remove('spoon')
print(utensils)

for i in utensils:
    print(i)

dishes = {'bowl', 'plate', 'cup'}
utensils.update(dishes)
print(utensils)