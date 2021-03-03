test = list(map(int,input().split()))
a,b = test

i = 1
while True:
	a = 3*a
	b = 2*b
	if a>b:
		break
	i += 1

print(i)