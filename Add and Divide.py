def solve(A,B):
	if not A:
		return(0)
	res = A+3
	ans = 0
	i = 0
	if B<2:
		i = B-2
	while i<res:
		b = B+i
		a = A
		while a:
			a = a//b
			ans += 1
		i += 1
		res = min(res,ans)
	return(res)




t = int(input())

for _ in range(t):
	A,B = list(map(int,input().split()))
	print(solve(A,B))
	