import random as rnd
from _flist import files

print('random: seed, sample')
print('-' * 30)

print('source list =', files)

rnd.seed()
files = rnd.sample(files,k=len(files))
# sample - для неизменяемых последовательностей
#      k - сколько выбрать случайных элементов

print('-' * 30)

i = 0
for file in files:
    i+=1
    print('%(num)03d_%(file)s' %{'num':i,'file':file})


