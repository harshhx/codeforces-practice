t = int(input())
ans = 0

for _ in range(t):
	s = input()
	if "+" in s:
		ans += 1
	elif "-" in s:
		ans -= 1
print (ans)