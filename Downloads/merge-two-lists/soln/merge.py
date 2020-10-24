# Get the input
left_line = list(input().split())
# now do something similar to get the list of vehicles in the right lane
right_line = list(input().split())

# Solve the problem
fine_line = []

if len(left_line) > len(right_line):
	for i in range(len(right_line)):
		fine_line.append(left_line[i])
		fine_line.append(right_line[i])
	for i in range(len(right_line),len(left_line)):
		fine_line.append(left_line[i])

if len(right_line) > len(left_line):
	for i in range(len(left_line)):
		fine_line.append(left_line[i])
		fine_line.append(right_line[i])
	for i in range(len(left_line),len(right_line)):
		fine_line.append(right_line[i])

if len(right_line) == len(left_line):
	for i in range(len(right_line)):
		fine_line.append(left_line[i])
		fine_line.append(right_line[i])

# Print the result
print(*fine_line)