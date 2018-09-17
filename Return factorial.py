"Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers."
def factorial(num):
	return 1 if num < 2 else num * factorial(num - 1)
