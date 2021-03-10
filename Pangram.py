n = int(input())
s = input()
base = 26
s = s.lower()
a = list(s)
if len(set(a)) == base:
	print("YES")
else:
	print("NO")