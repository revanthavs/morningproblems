# read the input
string1 = input()
# solve the problem
length = 0
i = 0
s = string1[::1]
llength = []
if string1 == string1[::-1]:
	if len(string1)%2 == 0:		
		for i in range(len(s)-1):
			string1 = ""
			string2 = ""
			string1 += s[i+1::1]
			string2 += string1[::-1]
			if string1 == string2:
				if len(string1)%2 != 0:
					llength.append(len(string1))
			#string2 += s[0:len(s)-i-1:1]
			#print(string2)
		for i in range(len(s)-1):
			string1 = ""
			string2 = ""
			string1 += s[0:len(s)-i-1:1]
			string2 += string1[::-1]
			if string1 == string2:
				if len(string1)%2 != 0:
					llength.append(len(string1))
		for i in range(len(s)//2):
			string1 = ""
			string2 = ""
			string3 = ""
			string1 += s[i+1::1]
			string2 += string1[0:len(string1)-i-1:1]
			string3 += string2[::-1]
			if string2 == string3:
				if len(string2) != 0:
					llength.append(len(string2))
		i = len(llength)-1
		while True:
			llength = sorted(llength)
			if llength[i]%2 != 0:
				print(llength[i])
				exit()
			i -= 1
	else:
		llength.append(len(string1))
for i in range(len(s)-1):
	string1 = ""
	string2 = ""
	string1 += s[i+1::1]
	string2 += string1[::-1]
	if string1 == string2:
		if len(string1)%2 != 0:
			llength.append(len(string1))
for i in range(len(s)-1):
	string1 = ""
	string2 = ""
	string1 += s[0:len(s)-i-1:1]
	string2 += string1[::-1]
	if string1 == string2:
		if len(string1)%2 != 0:
			llength.append(len(string1))
for i in range(len(s)//2):
	string1 = ""
	string2 = ""
	string3 = ""
	string1 += s[i+1::1]
	string2 += string1[0:len(string1)-i-1:1]
	string3 += string2[::-1]
	if string2 == string3:
		if len(string2) != 0:
			llength.append(len(string2))
print(max(llength))
"""
while (i<len(s)):
	if string1 == string2:
		length = len(string1)
		if length % 2 != 0:
			break
	if i % 2 == 0:
		string1 = string1[1::1]
		string2 = string1[::-1]
	else:
		string1 = string1[:len(string1)-1:1]
		string2 = string1[::-1]
	#if string1 == string2:
	#	length = len(string1)
	#	if length % 2 != 0:
	#		break
	i+=1
"""
"""
while (i<len(s)):
	if string1 == string2:
		llength.append(len(string1))
		string1 = string1[i::1]
		print(string1)
		string2 = string1[::-1]
		print(string2)
	else:
		string1 = string1[i+1::1]
		print(string1)
		string2 = string1[::-1]
	i += 1
print(*llength)
"""
"""		
while (i<len(s)):
	if string1 == string2:
		length = len(string1)
		if length % 2 != 0:
			break
	if i % 2 == 0:
		string1 = string1[1::1]
		string2 = string1[::-1]
	else:
		string1 = string1[:len(string1)-1:1]
		string2 = string1[::-1]
	#if string1 == string2:
	#	length = len(string1)
	#	if length % 2 != 0:
	#		break
	i+=1
"""		
#print(length)

# print the answer!
