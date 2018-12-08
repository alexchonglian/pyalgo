def match(s):
	i = 0
	for c in s[:-1]:
		if c == '(':
			i += 1
		elif c == ')':
			i -= 1
			if i <= 0:return False
	return i == 1 and s[-1] == ')'

if __name__ == '__main__':
	assert match('(())(()()())') == False
	assert match('(()()()())') == True
	assert match('(((())))') == True
	assert match('(()((())()))') == True
	assert match('((((((())') == False
	assert match('()))') == False
	assert match('(()()(()') == False