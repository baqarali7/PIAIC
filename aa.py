'''
name  = input('Tell Me Your name')
print("Hello Mr. / Mrs.: " + name)


number1 = int (input("Give Me a Number: "))
number2 = int (input("Give Me a Number2: "))

print(number1+number2)



marks = int (input("Please let me know your marks:  "))
if marks> 50:

	print("Your can sit in front raws")

elif marks > 40:

	print("Your can sit in front four raws")

else:
	print("You can sit behind front four rows")

'''
num1 = int (input("Give Me a Number: "))
num2 = int (input("Give Me a Number2: "))
opr = input("Give me a opration to perform + for add - for Sub * for multiple / for divide")

if opr == '+':
	print(num1+num2)
elif opr == '-':
	print(num1-num2)
elif opr == '*':
	print(num1*num2)
elif opr == '/':
	print(num1/num2)
else:
	print("wrong input")
