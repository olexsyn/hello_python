import sys

if __name__ == '__main__':
	if len(sys.argv)<=2:
		print('please run:', sys.argv[0], 'param1 param2 ... paramN')
		sys.exit(1)

	i = 0
	for par in sys.argv:
		print('param', i, ':', par)
		i += 1

sys.exit(1)
