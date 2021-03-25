t = int(input())

for _ in range(t):
	n,k = list(map(int,input().split()))
	s = input()
	s = list(s)
	if "*" not in s:
		print(0)
		continue
	first_star = 0
	last_found = False
	last_star = -1
	change = 0
	for i in range(len(s)):
		if s[i] == "*":
			s[i] = "X"
			first_star = i
			change += 1
			break
	for i in range(len(s)):
		if s[i] == "*":
			 last_star = max(last_star,i)
			 last_found = True
	if last_found:
		s[last_star] = "X"
		change += 1
	if "*" not in s[first_star:last_star]:
		print(change)
	else:
		cur = first_star
		for i in range(first_star+1,last_star,k):
			if s[i] == "*" and last_star-i<=k and i-cur<=k:
				s[i] = "X"
				cur = i

		print(s.count("X"))