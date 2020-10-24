
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x1 = sorted(x)
y1 = sorted(y)
sum = 0
for i in range(n):
	sum += (x1[i])*(y1[i])
print(sum)