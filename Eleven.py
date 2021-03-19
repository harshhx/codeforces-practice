def fibonacci(n):
	if n<2:
		return [1]
	ans = [1,1]
	i = 0
	while i<n:
		i = ans[-2] + ans[-1]
		ans.append(i)
	return ans


n = int(input())

test = fibonacci(n)
ans = ""
for i in range(1,n+1):
	if i in test:
		ans += "O"
	else:
		ans += "o"

print(ans)