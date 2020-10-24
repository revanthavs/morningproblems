# Read in the input
n = int(input())
words = {}
for i in range(n):
	line = list(input().split())
	words[line[0]] = line[1]
fline = input()
s = ""
fwords = []
for i in range(len(fline)):
	s = s + fline[i]
	if s in words.keys():
		fwords.append(words[s])
		s = ""

print(*fwords)