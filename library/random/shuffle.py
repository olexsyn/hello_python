import random as rnd
from _flist import files

print('random: seed, shuffle')
print('-' * 30)

print('source list =', files)

rnd.seed()
files = list(files)  # tuple to list
rnd.shuffle(files)

print('-' * 30)

i = 0
for file in files:
    i+=1
    print('%(num)03d_%(file)s' %{'num':i,'file':file})


