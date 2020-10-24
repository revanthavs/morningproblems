# Read input here.

n = int(input())

# Solve problem here. Good luck!

some = n
x = 0
count = 1
while (x < 3):
	count = int(count * some)
	x += 1
	some = some - 1

#count = int(count)
count = int(count / 6)
count = int(count)
print(count)