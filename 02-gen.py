def f():
	a = [1,2,3,4,5,6]
	i = 0
	while True:
		yield a[i]*2 + 1
		i += 1
		if (i > 5): i = 0


if __name__ == '__main__':
	iter = f()