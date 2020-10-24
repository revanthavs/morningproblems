# the floor() function might be useful
# for a floating point number x, floor(x) is the greatest integer <= x
from math import floor


# read in the input
numbers = list(map(int, input().split()))

# now "numbers" is a list containing all integers in the input


# solve the problem
ava = 0
total = len(numbers)
conditional_state = True
i = 0
sum_ = 0
while conditional_state:
	sum_ = sum_ + numbers[i]
	i += 1
	if i == total:
		conditional_state = False
ava = sum_/total
# output the solution
ava = int(ava)
print(ava)