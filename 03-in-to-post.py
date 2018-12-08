def infixToPostfix(infix_expr):
	prec = {'*': 3,'/': 3,'+': 2,'-': 2,'(': 1}
	operands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	operators = '*/+-()'
	stack = []
	postfix = []
	for c in infix_expr:
		#print(c, stack)
		if c in operands:
			postfix.append(c)
		elif c == '(':
			stack.append(c)
		elif c == ')':
			while stack != [] and stack[-1] != '(':
				postfix.append(stack.pop())
			if stack != [] and stack[-1] == '(':
				stack.pop()
		elif c in operators:
			while stack != [] and prec[stack[-1]] >= prec[c]:
				postfix.append(stack.pop())
			stack.append(c)
	while stack != []:
		postfix.append(stack.pop())
	return ' '.join(postfix)

def infixToPrefix(infix_expr):
	return infixToPostfix(infix_expr[::-1])[::-1]


if __name__ == '__main__':
	assert infixToPostfix("A * B + C * D") == 'A B * C D * +'
	assert infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )") == 'A B + C * D E - F G + * -'
	assert infixToPostfix("( A + B ) * ( C + D )") == 'A B + C D + *'
	assert infixToPostfix("( A + B ) * C") == 'A B + C *'
	assert infixToPostfix("A + B * C") == 'A B C * +'
	assert infixToPostfix("(1) * ((2))) + 3 * 4") == '1 2 * 3 4 * +'
	print(infixToPrefix("A * B + C * D")) == '+ * A B * C D'
	print(infixToPrefix("A + B + C + D"))
