# Good luck! Write your solution below.

user_input = list(map(int, input().split()))

i = 0
j = 1
k = 0
count = 0
length = []
z = len(user_input)
while (i < len(user_input)-1):
	count = 0
	if user_input[i] == user_input[j]:
		count += 1
		k = j
		while (len(user_input)-1 != k):
			if user_input[k] == user_input[k+1]:
				count += 1
			else:
				break
				i = k
				j = k + 1
			k += 1
		length.append(count)
		if len(user_input)-1 == k:
			break
		#print(f"{i} and {j}")
	i += 1
	j += 1
	if len(user_input)-1 == i:
		break

try:
	n = max(length)
except ValueError:
	n = 0
n += 1
print(n)