a = 20

def f():
	try:
		global a
		print(a)
		a = 10
		raise Error('wtf')
	except:
		print('ok')
	finally:
		print('finally')
		a = 30

if __name__ == '__main__':
	print(a)
	f()
	print(a)