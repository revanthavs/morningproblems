
line = input().split()
chocolates = int(line[0])
jars = int(line[1])
count = 0
i = 0
# write your code here

while (i < jars):
	a = input().split()
	first = int(a[0])
	second = int(a[1])
	if second - first >= chocolates:
		count += 1
	i += 1

print(count)