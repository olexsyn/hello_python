from random import randrange, randint

print('random: randrange, randint')
print('-' * 30)

print('randrange(10) =',    randrange(10))
print('randrange(10,20) =', randrange(10,20))
print('randint(3,5) =',     randint(3,5))

team1 = randrange(10)
team2 = randrange(10)
print()
print('Score:')
print('Team1 -', team1)
print('Team2 -', team2)
