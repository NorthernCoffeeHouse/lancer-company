# Simple command-line calculator
def calculator():
	print("Welcome to Python Calculator!")
	print("Enter your calculation (e.g., 2 + 2) or 'q' to quit.")
	while True:
		expr = input('> ')
		if expr.lower() == 'q':
			print("Goodbye!")
			break
		try:
			result = eval(expr, {"__builtins__": None}, {})
			print("Result:", result)
		except Exception as e:
			print("Error:", e)

if __name__ == "__main__":
	calculator()
