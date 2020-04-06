#!/usr/bin/python

import sys
import os

sys.path.insert(0, os.getcwd() + '/lib')

from my_path_class import aPath


# --- MAIN --------------------------------------

# print(sys.path)

test1 = aPath('/root/dir1/dir2/file.ext')
#print(test1.path, '/', test1.file)
# test1.prn()
print(test1)


test2 = aPath('/root/dir1/dir2/dir3')
# test2.prn()
print(test2)

test3 = aPath('/root/dir1/dir2.dirext/')
test3.prn()

test4 = aPath('file.ext')
test4.prn()

test5 = aPath('~/file.ext')
test5.prn()