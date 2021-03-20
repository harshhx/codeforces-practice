a = list(map(int,input().split()))
n,s = a

if n>s:
	print(1)
else:
	coins = []
	for i in range(1,n+1):
		coins.append(i)
	coins.reverse()
	i = 0
	ans = 0
	while s>0:
		ans += s//coins[i]
		s = s%coins[i]
		i += 1
	print(ans)