# read in the values for each item
n, m = map(int, input().split())
items = list(map(int, input().split()))
# now solve the problem
# good luck :D
small = min(items)
final = n - small
print(final + 1)