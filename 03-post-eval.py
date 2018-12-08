import operator as op

def postEval(expr):
	operands = '1234567890'
	operators = {'*': op.mul, '/': op.truediv, '+': op.add, '-': op.sub}
	stack = []
	for c in expr:
		if c in operands:
			stack.append(c)
		elif c in operators:
			i2 = int(stack.pop())
			i1 = int(stack.pop())
			result = operators[c](i1, i2)
			stack.append(result)
	return stack[0]

if __name__ == '__main__':
	print(postEval('1 2 * 3 4 * +'))