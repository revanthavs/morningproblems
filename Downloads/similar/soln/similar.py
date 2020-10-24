# Read in the input
user_input = list(map(int, input().split()))
# Solve the problem and output the result

if user_input[0] == user_input[1] == user_input[2]:
	print("same")
elif user_input[0] == user_input[1] or user_input[1] == user_input[2] or user_input[0] == user_input[2]:
	print("similar")
else:
	print("distinct")