a = list(map(int,input().split()))
n,k = a

scores = list(map(int,input().split()))

k_score = scores[k-1]

ans = 0

for i in scores:
	if i > 0 and i >= k_score:
		ans += 1

print(ans)