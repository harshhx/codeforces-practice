t = int(input())

for _ in range(t):
	test = list(map(int,input().split()))
	a,b = test
	if a%b == 0:
		print(0)
	elif b>a:
		print(b-a)
	else:
		x = a%b
		print(b-x)
