import sys

'''
$ python argv.py 3 5
Сумма целых чисел: 8

$ python argv.py 3.2 5.3
Сумма целых чисел: 8

$ python argv.py -3.2 5.3
Сумма целых чисел: 2

$ python argv.py -3.2 5.7
Сумма целых чисел: 3

'''

if __name__ == '__main__':
	if len(sys.argv)<=2:
		print('usage:', sys.argv[0], '<integer1> <integer2>')
		sys.exit(1)

	val1 = round(float(sys.argv[1]))
	val2 = round(float(sys.argv[2]))
	print('Сумма целых чисел:', val1+val2)
