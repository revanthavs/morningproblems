# read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())



# solve the problem
area =0
area = abs(x2-x1) * abs(y2-y1)
# output the result
print(area)