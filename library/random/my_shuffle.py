import random as rnd
from _flist import files

# --- DEFS ---------------------------

def my_shuffle(src_list):

    new_list = []
    rnd.seed()
    cur_size = len(src_list)
    while cur_size:
        sel = rnd.randrange(cur_size)
        new_list.append(src_list.pop(sel))
        cur_size -= 1
    return new_list

#def

# --- MAIN ---------------------------

print('My Shuffle')
print('-' * 30)

print('source list =', files)

files = my_shuffle(list(files))

print('-' * 30)

i = 0
for file in files:
    i+=1
    print('%(num)03d_%(file)s' %{'num':i,'file':file})


