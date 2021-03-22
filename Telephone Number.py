t = int(input())

for _ in range(t):
	n = int(input())
	s = input()
	i = 0
	while i<n:
		if s[i] == '8':
			break
		i += 1

	print ("YES" if n - i >= 11 else "NO")

	
	
