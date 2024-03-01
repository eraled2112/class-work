#problem 0
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)

#problem 1
a = {99, frozenset(frozenset('Albina')), 34}

#problem 2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.difference(farm_2))

#problem 3
a = {'moon', 'sun', 'star', 'galaxy', 'planet'}
a.add("earth")
print(a)
print(a.pop())

#problem 10
menu = {
    'lagman': 120,
    'plov': '120',
    'borsh': 100
}
menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
print(menu)

#problem 020
a = {'.add', '.update', '.remove', '.clear', '.difference', '.discard', '.intersection', '.intersection'}
