
condition = True
n = 0
max_number = 0
while condition:
	try :	
		line_input = list(map(float, input().split()))
		max_number = max(line_input)
		print(f"max: {max_number}")
	except EOFError:
		condition = False
