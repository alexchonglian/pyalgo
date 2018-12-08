def toStr(n, base):
	conv = "0123456789ABCDEF"
	if n < base:
		return conv[n]
	else:
		return toStr(n//base, base) + conv[n%base]

print(toStr(1453, 16))