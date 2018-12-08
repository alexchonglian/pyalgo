class Fraction:
	def __init__(self, num, den):
		self.num = num
		self.den = den

if __name__ == '__main__':
	f1 = Fraction(1,2)
	f2 = Fraction(1,2)
	print(f1 == f2)
	print(f1)