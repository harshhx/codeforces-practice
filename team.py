t = int(input())
ans = 0
for _ in range(t):
	a = list(map(int,input().split()))
	if a.count(1)>=2:
		ans += 1
print(ans)