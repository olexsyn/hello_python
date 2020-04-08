#!/usr/bin/python

# see https://wiki.archlinux.org/index.php/Desktop_notifications

import subprocess


def notify(title, mess):

	# for test
	print(title, ':', mess)

	subprocess.call(['notify-send', title, mess])
#def


notify("And I said", "Hello world!")

