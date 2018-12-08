def match(pars):
	s = []
	d = {'(':')','[':']','{':'}'}
	for i in pars:
		if i in '([{':
			s.append(i)
		elif i in '}])':
			if s == []:
				return False
			if d[s.pop()]!= i:
				return False
	return s == []

print(match('{{([][])}()}'))
print(match('[{()]'))
print(match('{{([][])}()}'))
print(match('[[{{(())}}]]'))
print(match('[][][](){}'))