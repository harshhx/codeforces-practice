n = int(input())
ans = 0

for _ in range(n):
	test = list(map(int,input().split()))
	p,q = test
	if q-p >=2:
		ans += 1

print(ans)