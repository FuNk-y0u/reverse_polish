texts = input("TEXT> ")

operator_stack = []
operant_stack = []

operators = ["+","-","*","/","(",")"]
high = ["*","/"]
low = ["+","-"]
neut = [")","("]
for text in texts:
	if text in operators:
		if len(operator_stack) != 0:
			value = operator_stack.pop()
			if text == ")":
				if value not in neut:
					operant_stack.append(value)
				for i in range(len(operator_stack)):
					value = operator_stack.pop()
					if value not in neut:
						operant_stack.append(value)
			elif (value in low) and (text in high):
				operator_stack.append(value)
				operator_stack.append(text)
			elif (value in high) and (text in low):
				operant_stack.append(value)
				for i in range(len(operator_stack)):
					value = operator_stack.pop()
					operant_stack.append(value)
				operator_stack.append(text)
			else:
				operator_stack.append(value)
				operator_stack.append(text)
		else:
			operator_stack.append(text)
	else:
		operant_stack.append(text)

for x in range(len(operator_stack)):
	value = operator_stack.pop()

	if value not in neut:
		operant_stack.append(value)
print(operant_stack)
print(operator_stack)
while len(operant_stack) > 1:
	new_stack = []
	ext = False
	x = 0
	while not ext:
		if operant_stack[x] in operators:
			if operant_stack[x] == "+":
				new_stack.pop()
				new_stack.pop()
				new_stack.append(int(operant_stack[x-1]) + int(operant_stack[x-2]))
			elif operant_stack[x] == "-":
				new_stack.pop()
				new_stack.pop()
				new_stack.append(int(operant_stack[x-2]) - int(operant_stack[x-1]))
			elif operant_stack[x] == "*":
				new_stack.pop()
				new_stack.pop()
				new_stack.append(int(operant_stack[x-2]) * int(operant_stack[x-1]))
			elif operant_stacl[x] == "/":
				new_stack.pop()
				new_stack.pop()
				new_stack.append(int(operant_stack[x-2]) / int(operant_stack[x-1]))
			for i in range(x+1,len(operant_stack)):
				new_stack.append(operant_stack[i])
			ext = True
		else:
			new_stack.append(operant_stack[x])
		x+=1
	operant_stack = new_stack
print(operant_stack)
