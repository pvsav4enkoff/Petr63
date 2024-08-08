for value in range(1,21):
    print(value)

even_numbers = list(range(1,1000001,1))
#print(even_numbers)
#print(even_numbers.count())
print(max(even_numbers))
print(min(even_numbers))
print(sum(even_numbers))

for value in range(1,21,2):
    print(value)

for value in range(3,31,3):
    print(value)

squares = [value**3 for value in range(1,11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli','jon','ivan','stepan','mihail']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print('-------')

for player in players[3:6]:
    print(player.title())

print('-------')

for player in players[6:]:
    print(player.title())