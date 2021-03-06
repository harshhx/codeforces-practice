t = int(input())

for _ in range(t):
	test = list(map(int,input().split()))
	n,k = test
	v = list()
	for i in range(k+1,n+1):
		v.append(i)
	s = set()
	i = k-1
	while i>=1:
		if k-i not in s:
			v.append(i)
			s.add(i)
		i -=1
	print(len(v))
	for i in v:
		print(i,end=" ")
	print("")
