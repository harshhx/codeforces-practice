n = int(input())

owner  = {}

for _ in range(n):
	name = input()
	if name in owner:
		print("YES")
	else:
		owner[name] = True
		print("NO")