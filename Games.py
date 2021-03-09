n = int(input())
teams = []
for _ in range(n):
	test = list(map(int,input().split()))
	teams.append(test)
ans = 0
for i in teams:
	curr = i[0]
	for i in teams:
		if curr == i[1]:
			ans += 1
print(ans)