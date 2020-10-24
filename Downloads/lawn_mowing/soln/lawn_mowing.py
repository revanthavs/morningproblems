# Good luck! You've got this!

l,w = map(int,input().split())
total = 0
if l > w:
	r = w/2
	first = float(r * 2)
	for i in range(1,3):
		total += float(4 * (l/2) * w * i)
if w > l:
	r = l/2
	first = float(r * 2)
	for i in range(1,3):
		total += float(4 * (w/2) * l * i)

if l == w:
	r = w/2
	first = float(r*2)
	for i in range(1,5):
		total += float(4 * (l/2) * (w/2) * i)

total = int(total + first)
print(total)