#!/usr/bin/python

from re import search, sub


# --- DEFS --------------------------------------

def split_path(fullpath):
    '''
    Splits path to file or directory in parts. Works only
    with a string. Doesn't define real object type (file
    or dir) and it existing.
    Return a tuple of parts.

    Example for file "/root/dir1/dir2/file.ext":
        fullpath = "/root/path/to/file.ext"
        path     = "/root/path/to"
        file     = "file.ext"
        filename = "file"
        fileext  = "ext"

    Example for dir "/root/dir1/dir2/dir3":
        fullpath = "/root/dir1/dir2/dir3"
        path     = "/root/dir1/dir2"
        file     = "dir3"
        filename = "dir3"
        fileext  = ""

    '''

    # if path ends with a slash - delete it
    fullpath = sub('/$', '', fullpath)

    # last of /
    found = search('^(.+)/(.+)$', fullpath)
    if found:
        path = found.group(1)
        file = found.group(2)
    else:
        path = ''
        file = fullpath

    # last of .
    found = search('^(.+)\.(.+)$', file)
    if found:
        filename = found.group(1)
        fileext  = found.group(2)
    else:
        filename = file
        fileext  = ''

    return {
            'fullpath': fullpath,
            'path':     path,
            'file':     file,
            'filename': filename,
            'fileext':  fileext
           }
#

def print_result(res):
    '''
    Just print a tuple

    '''
    print()
    print('fullpath =', res['fullpath'])
    print('path     =', res['path'])
    print('file/dir =', res['file'])
    print('filename =', res['filename'])
    print('fileext  =', res['fileext'])
#


# --- MAIN --------------------------------------

test1 = '/root/dir1/dir2/file.ext'
test2 = '/root/dir1/dir2/dir3'
test3 = '/root/dir1/dir2.dirext/'
test4 = 'file.ext'
test5 = '~/file.ext'

res = split_path(test1)
print_result(res)

res = split_path(test2)
print_result(res)

res = split_path(test3)
print_result(res)

res = split_path(test4)
print_result(res)

res = split_path(test5)
print_result(res)
