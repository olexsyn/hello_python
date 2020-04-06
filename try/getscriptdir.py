#!/usr/bin/python3

import inspect
import os
import sys

def get_script_dir(follow_symlinks=True):

	if (sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
		path = os.path.abspath(sys.executable)
		print('1',path)
	else:
		path = inspect.getabsfile(get_script_dir)
		print('2',path)

	if follow_symlinks:
		path = os.path.realpath(path)
		print('3',path)

	return os.path.dirname(path)

print(get_script_dir())
