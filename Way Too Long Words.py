def long_word(s):
	ans = ""
	a = str(len(s)-2)
	ans += s[0]
	ans += a
	ans += s[-1]
	return ans

t = int(input())

for _ in range(t):
	s = input()
	if len(s)>10:
		print(long_word(s))
	else:
		print(s)