n = int(input())
s = input()
r,g,b = 0,0,0

for i in range(1,len(s)):
	if s[i-1] == s[i]:
		if s[i] == "R":
			r += 1
		elif s[i] == "G":
			g += 1
		else:
			b += 1

print(r+g+b)
