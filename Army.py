n = int(input())

army = list(map(int,input().split()))
a,b = list(map(int,input().split()))
army.append(0)
a -= 1
b -= 1
ans = 0
for i in range(a,b):
	ans += army[i]
print(ans)