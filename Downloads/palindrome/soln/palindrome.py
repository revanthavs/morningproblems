string = input()
llength = []
for i in range(len(string)):
	for j in range(len(string)):
		string1 = ""
		string2 = ""
		if string[i] == string[j]:
			string1 = string[i:j+1]
			if len(string1)%2 != 0:
				string2 = string1[::-1]
			if string1 == string2:
				llength.append(len(string2))
print(max(llength))