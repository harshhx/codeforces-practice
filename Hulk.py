n = int(input())

a = "I hate"
b = "I love"
ans = ""

for i in range(1,n+1):
	if i%2 != 0:
		ans += a
		ans += " that "
	else:
		ans += b
		ans += " that "

ans = ans[:-5]
ans += "it"

print(ans)