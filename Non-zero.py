t = int(input())

for _ in range(t):
	n = int(input())
	test = list(map(int,input().split()))
	sum,ans = 0,0
	for i in test:
		if i == 0:
			i += 1
			ans += 1
		sum += i
	if sum == 0:
		ans += 1
	print(ans)